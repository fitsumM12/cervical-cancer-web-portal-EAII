from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import patientsDetail
from .serializers import PatientsDetailSerializer
from .predictor import *
import os
from django.conf import settings
from PIL import Image
import numpy as np
from .predictor import create_model, load_weights
from django.contrib.auth.decorators import login_required

# Apply IsAuthenticated permission for all views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_patients_api(request):
    patients = patientsDetail.objects.all()
    serializer = PatientsDetailSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_patients_doctor_api(request, pk):
    patients = patientsDetail.objects.filter(doctor_id=pk)
    serializer = PatientsDetailSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_patient_api(request, pk):
    patient = patientsDetail.objects.get(pk=pk)
    serializer = PatientsDetailSerializer(patient)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_patient_api(request, pk):
    patient = patientsDetail.objects.get(pk=pk)
    serializer = PatientsDetailSerializer(patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_patient_api(request, pk):
    patient = patientsDetail.objects.get(pk=pk)
    patient.delete()
    return Response(status=204)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_patient_api(request):
    serializer = PatientsDetailSerializer(data=request.data)
    if serializer.is_valid():
        patient = serializer.save()
        response_data = {
            'id': patient.id,
            **serializer.data
        }
        return Response(response_data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_raw_generate_cam_and_predictions(request):
    if 'image' not in request.FILES:
        return Response({'error': 'No image file found'}, status=400)

    image_file = request.FILES.get('image')
    image_path = os.path.join(settings.MEDIA_ROOT_RAW, image_file.name)
    with open(image_path, 'wb') as f:
        for chunk in image_file.chunks():
            f.write(chunk)

    image = Image.open(image_path)
    image = image.resize((299, 299))
    image = np.array(image) / 255.0

    model = create_model()
    load_weights(model)
    
    # Make predictions using the model
    prediction = predict(model, np.expand_dims(image, axis=0))
    
    response_data = {
        'image_url': image_path,
        'predictions': prediction.tolist()
    }
    
    return Response(response_data, status=200)
