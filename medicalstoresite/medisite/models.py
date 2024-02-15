from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta,date
from django.utils import timezone

# Create your models here.
class MedicineDetails(models.Model):
    """Model representing a medicine details."""
    name = models.CharField(max_length=200, help_text='Enter a medicine name')
    quantity=models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    mfg_date = models.DateField(default=timezone.now)
    exp_date = models.DateField(default=datetime.now() + timedelta(days=365))
    def __str__(self):
        """String for representing the Model object."""
        return self.name
   
    def get_absolute_url(self):
        """Returns the url to access a detail record for this medicine."""
        return reverse('medicinedetails_details', args=[str(self.pk)])