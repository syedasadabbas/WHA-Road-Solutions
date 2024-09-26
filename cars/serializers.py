from rest_framework import serializers
from .models import Car, CarImage

# Serializer for CarImage (for the gallery)
class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']

# Serializer for Car
class CarSerializer(serializers.ModelSerializer):
    car_gallery = CarImageSerializer(many=True, read_only=True)  # Nested car_gallery serializer

    class Meta:
        model = Car
        fields = [
            'id', 'built_date', 'car_make', 'car_model', 'car_type', 'doors',
            'transmission', 'capacity', 'cylinders', 'fuel_type', 'gears',
            'odometer', 'car_colour', 'car_registration', 'vin', 'car_picture',
            'car_price', 'car_status', 'car_title', 'car_description', 'car_gallery'
        ]