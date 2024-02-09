from django.db import models
from driver.models import Driver
from rider.models import Rider
# Create your models here.
class Match(models.Model):
    pass
    def match(self, driver_id, rider_id):
        """
        Matches a driver with a rider based on their IDs.

        Args:
            driver_id (int): The ID of the driver.
            rider_id (int): The ID of the rider.

        Returns:
            bool: True if the driver and rider are successfully matched, False otherwise.
        """
        """
        Things to consider here:
        1. The driver should be available.(offering a ride)
        2. The rider should be available.(searching for a ride)
        3. The driver and rider must be in the same city.
        4. They should be at minimum distance from each other.
        5. Or they should within a radius of xkm from each other.
        6. The driver should have a good rating.
        Respect to change in future
        """
        
    def pickBestPair(self):
        """
        How to pick the best pair
        Query the database?
        Driver.objects.get(id).state == rider.objects.get(id).state
        Driver.objects.get(id).city == rider.objects.get(id).city
        Driver.objects.get(id).curr_lat --near-- rider.objects.get(id).curr_lat
        Driver.objects.get(id).curr_long --near-- rider.objects.get(id).curr_long(in a radius or a algorithm to calculate distance and find the minimal one)
        Driver.objects.get(id).ratings > x
        
        """
        return (rider_id, driver_id)