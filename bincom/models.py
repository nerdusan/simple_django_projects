from django.db import models

# Create your models here.
class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField(primary_key = True)
    polling_unit_uniqueid = models.CharField(max_length = 50)
    party_abbreviation = models.CharField(max_length = 4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length = 50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length = 50)

    def __str__(self):
        return self.polling_unit_uniqueid

# pu_choices = list(range(8, 28))

# class MyModel(models.Model):
#   pu = models.CharField(max_length=2, choices=pu_choices, default=8)
