from django.db import models

# Create your models here.
class Book(models.Model):
    rider_id = models.IntegerField(null=False)
    driver_id = models.IntegerField(null=False)
    
    def create_booking(self, driver_id: int, rider_id: int):
        b = Book(driver_id = driver_id, rider_id = rider_id)
        if b.clean():
            b.save()