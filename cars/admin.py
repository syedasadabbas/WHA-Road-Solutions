from django.contrib import admin
from .models import Car, CarImage, UserDetail, AppointmentBooking

# Register your models here.
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(UserDetail)
admin.site.register(AppointmentBooking)

# Fetch all cars
cars = Car.objects.all()

# Print each car with its associated images
for car in cars:
    print(car.car_title, car.images.all())  # This should show the related images
