from django.db import models
from usersDetail.models import usersDetail
from django.utils import timezone


class patientsDetail(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=110)
    job = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    record_date = models.DateField(default=timezone.now)
    region = models.CharField(max_length=100, blank=True)
    zone = models.CharField(max_length=100, blank=True)
    kebele = models.CharField(max_length=100, blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    prediction = models.JSONField(null=True)
    doctor_id= models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(patientsDetail.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id +=1
            self.id = new_id
        super(patientsDetail, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    


