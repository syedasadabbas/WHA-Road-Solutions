from django.db import models

class Car(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Convertible', 'Convertible'),
        # Add more car types as needed
    ]
    
    TRANSMISSION_TYPES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    
    FUEL_TYPES = [
        ('Petrol', 'Petrol - Unleaded ULP'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        # Add more fuel types if needed
    ]
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('rent_to_own', 'Rent to Own'),
    ]
    
    # Basic Car Info
    built_date = models.DateField()
    car_make = models.CharField(max_length=50, default='Toyota')
    car_model = models.CharField(max_length=50, default='Echo')
    car_type = models.CharField(max_length=50, choices=CAR_TYPES, default='Sedan')
    doors = models.PositiveIntegerField(default=4)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_TYPES, default='Automatic')
    capacity = models.DecimalField(max_digits=3, decimal_places=1, default=1.5)
    cylinders = models.PositiveIntegerField(default=4)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPES, default='Petrol')
    gears = models.PositiveIntegerField(default=4)
    odometer = models.PositiveIntegerField(default=234568)
    car_colour = models.CharField(max_length=30, default='White')
    car_registration = models.CharField(max_length=50, unique=True)
    vin = models.CharField(max_length=17, unique=True)
    car_picture = models.ImageField(upload_to='cars/images/', blank=True, null=True)
    car_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Car price in the local currency")
    car_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    car_title = models.CharField(max_length=200)
    car_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.car_make} {self.car_model} ({self.car_registration})'


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)  # Related name for car images
    image = models.ImageField(upload_to='cars/gallery/')  # Field for storing car gallery images
    
    def __str__(self):
        return f"{self.car.car_make} {self.car.car_model} ({self.car.car_registration})"
    
    class Meta:
        ordering = ['id']  # Ensure images are ordered by their id

class UserDetail(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    dob = models.DateField()  # Date of Birth
    age = models.PositiveIntegerField()

    # Address Information
    street_address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    # Licence Information
    licence_number = models.CharField(max_length=20)
    licence_expiry_date = models.DateField()

    # Option (Choices Field)
    RENT_OPTION_CHOICES = [
        ('rent', 'Rent'),
        ('rent_to_own', 'Rent to Own'),
        ('purchase', 'Purchase'),
    ]
    option = models.CharField(max_length=20, choices=RENT_OPTION_CHOICES, default='rent')
    # Add fields for license images
    licence_front_image = models.ImageField(upload_to='licenses/front/', blank=True, null=True)
    licence_back_image = models.ImageField(upload_to='licenses/back/', blank=True, null=True)

    car_type = models.CharField(max_length=100, null=True)
    car_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    car_make = models.CharField(max_length=100, null=True)
    car_color = models.CharField(max_length=50, null=True)
    car_registration = models.CharField(max_length=50, null=True)
    car_vin = models.CharField(max_length=50, null=True)
    car_picture = models.ImageField(upload_to='cars/', blank=True, null=True)

    # Timestamp for Submission
    submission_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.id} - {self.first_name} {self.last_name}'


class AppointmentBooking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    street_address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    licence = models.CharField(max_length=255)
    licence_expiry = models.DateField()
    option = models.CharField(max_length=50)  # purchase car / rent car / rent to own car
    licence_front_image = models.ImageField(upload_to='licence_images/front')
    licence_back_image = models.ImageField(upload_to='licence_images/back')
    booking_date = models.DateTimeField(auto_now_add=True)  # Automatically sets the time when the appointment is created
    appointment_booked_time = models.DateTimeField(auto_now_add=True)  # Save when the appointment was booked

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone}"