from django.db import models

# Create your models here.

class Driver(models.Model):
    """
    Represents a driver in the Uber Clone application.
    
    Attributes:
        ph_no (int): The phone number of the driver.
        name (str): The name of the driver.
        password (str): The password of the driver.
        email (str): The email address of the driver.
        ratings (Decimal): The ratings of the driver.
        curr_lat (Decimal): The current latitude of the driver.
        curr_long (Decimal): The current longitude of the driver.
    """
    ph_no = models.IntegerField(blank=False, null=False)
    name = models.CharField(blank=False, null=False)
    password = models.CharField(blank=False, null=False)
    email = models.CharField(blank=False, null=True)
    city = models.CharField(blank=False, null=False) # city of the driver from Google Maps API
    state = models.CharField(blank=False, null=False) # state of the driver from Google Maps API
    country = models.CharField(blank=False, null=False) # For future use
    ratings = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    curr_lat = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    curr_long = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    
    """_summary_
    To be done: Force the driver to share location for live tracking
    """
    @callable
    def offer(self, driver_id):
        return False
    
    """_summary_
    Enables the driver to notify nearby riders that he/she is ready for picking a ride
    
    Returns:
        int: id of the driver who offers a ride
    """