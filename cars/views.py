from rest_framework import generics
from .models import Car, CarImage, UserDetail, AppointmentBooking
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from datetime import datetime


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['car_make', 'car_type', 'fuel_type', 'car_status']
    ordering_fields = ['car_price', 'built_date', 'odometer']

    def get_queryset(self):
        queryset = super().get_queryset()

        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)

        if price_min is not None:
            queryset = queryset.filter(car_price__gte=price_min)
        if price_max is not None:
            queryset = queryset.filter(car_price__lte=price_max)

        return queryset

# @csrf_exempt
# def reserve_car(request):
#     if request.method == 'POST':
#         print(request.headers['Content-Type'])
#         try:
#             data = json.loads(request.body)
#             print(data)  # Print the received data for debugging
#             # Handle the data (e.g., save to the database, etc.)
#             return JsonResponse({'status': 'success', 'message': 'Reservation received'}, status=200)  # Explicit success status
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)  # Invalid JSON error
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)  # Invalid method error


@csrf_exempt
def reserve_car(request):
    if request.method == 'POST':
        # Extract data from request.POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        street_address = request.POST.get('street_address')
        suburb = request.POST.get('suburb')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        licence = request.POST.get('licence')
        licence_expiry = request.POST.get('licence_expiry')
        option = request.POST.get('option')

        # Extract car details
        car_type = request.POST.get('car_type')
        car_price = request.POST.get('car_price')
        car_make = request.POST.get('car_make')
        car_color = request.POST.get('car_color')
        car_registration = request.POST.get('car_registration')
        car_vin = request.POST.get('car_vin')
        car_picture = request.FILES.get('car_picture')  # Assuming the image is sent in the request

        # Handle file uploads for license images
        licence_front_image = request.FILES.get('licence_front_image')
        licence_back_image = request.FILES.get('licence_back_image')

        # Define the upload directory
        upload_dir = '/home/ghosta4/WHO-Road-Solutions/cars/images'  # Change to your desired path
        os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Function to save uploaded files (license images)
        def save_file(uploaded_file):
            if uploaded_file:
                file_path = os.path.join(upload_dir, uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

        # Save each uploaded file
        save_file(licence_front_image)
        save_file(licence_back_image)

        # Create a new UserDetail object
        user_detail = UserDetail(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            dob=dob,
            age=age,
            street_address=street_address,
            suburb=suburb,
            state=state,
            postcode=postcode,
            licence_number=licence,
            licence_expiry_date=licence_expiry,
            option=option,
            car_type=car_type,
            car_price=car_price,
            car_make=car_make,
            car_color=car_color,
            car_registration=car_registration,
            car_vin=car_vin,
            car_picture=car_picture,
            licence_front_image=licence_front_image,
            licence_back_image=licence_back_image,
        )

        # Save the user detail to the database
        user_detail.save()

        return JsonResponse({'status': 'success', 'message': 'Reservation received'}, status=200)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def car_images_view(request, car_name):
    try:
        # Split the car_name format: 'car_make car_model (car_registration)'
        # Example car_name: "Toyota Echo (TOYOTA598733001)"
        car_make_model, car_registration = car_name.rsplit('(', 1)
        car_make, car_model = car_make_model.split()
        car_registration = car_registration.strip(')')

        # Find the car based on car_make, car_model, and car_registration
        car = Car.objects.get(car_make=car_make, car_model=car_model, car_registration=car_registration)

        # Retrieve all images associated with this car
        images = CarImage.objects.filter(car=car)

        # Prepare the response data
        image_data = []
        for image in images:
            image_data.append({
                'id': image.id,
                'url': image.image.url,  # This will return the URL of the image
                'car': str(car),  # This returns 'car_make car_model (car_registration)'
            })

        return JsonResponse({'car': str(car), 'images': image_data})

    except Car.DoesNotExist:
        return JsonResponse({'error': 'Car not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

@csrf_exempt
def reserve_appointment(request):
    if request.method == 'POST':
        # Extract data from request.POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        street_address = request.POST.get('street_address')
        suburb = request.POST.get('suburb')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        licence = request.POST.get('licence')
        licence_expiry = request.POST.get('licence_expiry')
        option = request.POST.get('option')

        # Handle file uploads for license images
        licence_front_image = request.FILES.get('licence_front_image')
        licence_back_image = request.FILES.get('licence_back_image')

        # Define the upload directory
        upload_dir = '/home/ghosta4/WHO-Road-Solutions/appointments/images'  # Change to your desired path
        os.makedirs(upload_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Function to save uploaded files (license images)
        def save_file(uploaded_file):
            if uploaded_file:
                file_path = os.path.join(upload_dir, uploaded_file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

        # Save each uploaded file
        save_file(licence_front_image)
        save_file(licence_back_image)

        # Create a new UserDetail object
        user_detail = AppointmentBooking(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            dob=dob,
            age=age,
            street_address=street_address,
            suburb=suburb,
            state=state,
            postcode=postcode,
            licence=licence,
            licence_expiry=licence_expiry,
            option=option,
            licence_front_image=licence_front_image,
            licence_back_image=licence_back_image,
        )

        # Save the user detail to the database
        user_detail.save()

        return JsonResponse({'status': 'success', 'message': 'Reservation received'}, status=200)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
