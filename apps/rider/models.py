from django.db import models
from driver.models import Driver
# Create your models here.

class Rider(models.Model):
    """
    Represents a rider in the Uber Clone application.

    Attributes:
        ph_no (int): The phone number of the rider.
        name (str): The name of the rider.
        password (str): The password of the rider.
        email (str): The email address of the rider.
        curr_lat (Decimal): The current latitude of the rider's location.
        curr_long (Decimal): The current longitude of the rider's location.
    """
    ph_no = models.IntegerField(blank=False, null=False)
    name = models.CharField(blank=False, null=False)
    password = models.CharField(blank=False, null=False)
    email = models.CharField(blank=False, null=True)
    city = models.CharField(blank=False, null=False) # city of the rider from Google Maps API
    state = models.CharField(blank=False, null=False) # state of the rider from Google Maps API
    country = models.CharField(blank=False, null=False) # For future use
    curr_lat = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    curr_long = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    """_summary_
    Force user to turn on location for live tracking
    """
    def search(self, rider_id):
        return False