from django.contrib import admin
from .models import Car, CarImage, UserDetail, AppointmentBooking

# Customizing the CarAdmin class to add search functionality
class CarAdmin(admin.ModelAdmin):
    search_fields = ['vin', 'car_registration']  # Add VIN and Car Registration to the search fields

# Register your models with the customized CarAdmin
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
admin.site.register(UserDetail, CarAdmin)
admin.site.register(AppointmentBooking, CarAdmin)

# # Fetch all cars
# cars = Car.objects.all()

# # Print each car with its associated images
# for car in cars:
#     print(car.car_title, car.images.all())  # This should show the related images
