from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.fetch_patients_api, name='fetch_patients_api'),
    path('patients/<int:pk>/', views.fetch_patient_api, name='fetch_patient_api'),
    path('patients/add/', views.add_patient_api, name='add_patient_api'),
    path('patients/update/<int:pk>/', views.update_patient_api, name='update_patient_api'),
    path('patients/delete/<int:pk>/', views.delete_patient_api, name='delete_patient_api'),
    path('patients/predict_image/', views.upload_raw_generate_cam_and_predictions, name='upload_raw_generate_cam_and_predictions'),
    path('patients/doctor/<int:pk>/', views.fetch_patients_doctor_api, name ='fetch_patients_doctor_api')
]