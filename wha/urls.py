"""
URL configuration for who project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cars/', CarListView.as_view(), name='cars'),  # API to list cars with filters
    path('api/reserve/', reserve_car, name='reserve_car'),
    path('api/appointment/', reserve_appointment, name='reserve_appointment'),
    path('api/car-images/<str:car_name>/', car_images_view, name='car-images'),
    path('cars/', car_list_with_images, name='car_list_with_images'),
    path('cars/<int:car_id>/', car_detail_and_image_crud, name='car_detail_and_image_crud'),
    path('cars/image/delete/<int:image_id>/', delete_car_image, name='delete_car_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)