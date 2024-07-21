from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
DISTRICT_CHOICES =(
    ('Alipurduar','Alipurduar'),
    ('Bankura','Bankura'),
    ('Birbhum','Birbhum'), 
    ('Cooch Behar','Cooch Behar'), 
    ('Dakshin Dinajpur','Dakshin Dinajpur'), 
    ('Darjeeling','Darjeeling'), 
    ('Hooghly','Hooghly'), 
    ('Howrah','Howrah'), 
    ('Jalpaiguri','Jalpaiguri'), 
    ('Jhargram','Jhargram'), 
    ('Kalimpong','Kalimpong'), 
    ('Kolkata','Kolkata'), 
    ('Malda','Malda'), 
    ('Murshidabad','Murshidabad'), 
    ('Nadia','Nadia'), 
    ('North 24 Parganas',' North 24 Parganas '), 
    ('Paschim Bardhaman',' Paschim Bardhaman'), 
    ('Paschim Medinipur','Paschim Medinipur '), 
    ('Purba Bardhaman',' Purba Bardhaman'), 
    ('Purba Medinipur',' Purba Medinipur'), 
    ('Purulia','Purulia'), 
    ('South 24 Parganas','South 24 Parganas'), 
    ('Uttar Dinajpur',' Uttar Dinajpur'),
)

class Customer(AbstractUser):
    USER = (
        (1 , 'Admin'),
        (2 , 'Co-Ordinator'),
        # (3 , 'Student'),

    )

    user_type = models.CharField(choices=USER, max_length=50 ,default = 1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Student(models.Model):
    
    district = models.CharField(choices=DISTRICT_CHOICES , max_length=50 )
    center_codes = models.CharField(max_length = 2,default= "")
    student_name  = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length = 100)
    school_name = models.TextField()
    classes = models.CharField(max_length = 2)
    mobile_number = models.CharField(max_length= 15)
    roll_no = models.CharField(max_length = 15,default="")

    def __str__(self):
        return self.student_name + "    " + self.district
    
class Co_Ordinator(models.Model):
    admin = models.OneToOneField(Customer, on_delete=models.CASCADE)
    district = models.CharField(choices=DISTRICT_CHOICES ,max_length = 20)

    def __str__(self):
        return self.admin.username