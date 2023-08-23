from django.db import models

# Create your models here.
class contact(models.Model):

    name=models.CharField(max_length=20)
    phone_number=models.BigIntegerField()

    def __str__(self) :
        return self.name
    
    class Meta:
        db_table='contactbk_contact'
        verbose_name_plural='1.contactbooks'

