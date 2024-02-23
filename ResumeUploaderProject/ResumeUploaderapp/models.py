from django.db import models

STATE_CHOICES = (
    ('Andhra pradesh', 'Andhra Pradesh'),
    ('Telangana', 'Telangana'),
    ('Karnataka', 'Karnataka'),
    ('Punjab', 'Punjab'),
    ('Tamil nadu', 'Tamil Nadu'),
    ('Madhya pradesh', 'Madhya Pradesh')
)

class Resume(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
