from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usersDetail.urls')),  
    path('api/', include('patientsDetail.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
