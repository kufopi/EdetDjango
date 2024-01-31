from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser 
import datetime
from dateutil.relativedelta import relativedelta
# Create your models here.

SESS = [tuple([str(x)+'/'+str(x+1),str(x)+'/'+str(x+1)]) for x in range (2019,2070,1)]
PGLEVEL_CHOICES = (
    ('600','600'),
    ('700','700'),
    ('800','800'),
)#[tuple([x,x]) for x in range(600,900,100)]


UGLEVEL_CHOICES = (
    ('100','100'),
    ('200','200'),
    ('300','300'),
    ('400','400'),
    ('500','500'),
)



GENDER = (
    
    ('Female','Female'),
    ('Male','Male')
    
    )

BLOOD_GROUP = (
    ('A','A'),
    ('B','B'),
    ('AB','AB'),
    ('O','O')
    
    )

CATEGORY = (
    ('University Staff','University Staff'),
    ('Ventures Staff','Ventures Staff'),
    ('Undergrad','Undergrad'),
    ('Postgrad','Postgrad'),

)

DEPT =(
    ('Mass Comm','Mass Comm'),
    ('Law','Law'),
    ('Bio-Chem','Bio-Chem'),
    ('Civil-Eng','Civil-Eng'),
    ('Nursing','Nursing'),
)



class User(AbstractUser):
    
    staff_id  = models.CharField( help_text='Matric Id if student',max_length=50)
    first_name  = models.CharField( max_length=50)
    middle_name  = models.CharField( max_length=50,blank=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices= GENDER, max_length=6)
    blood_group  = models.CharField(choices= BLOOD_GROUP,max_length=3)
    category = models.CharField(choices= CATEGORY, max_length=30)
    passport = models.ImageField(help_text='White background', upload_to='user/passport',)



    

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    

    
    
    # def save(self):
    #     super().save()

    #     img = Image.open(self.passport.path) # Open image
        
    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.passport.path) # Save it again and override the larger image





class Session(models.Model):
    academic_session = models.CharField(choices=SESS, max_length=50)

    

    class Meta:
        verbose_name = ("Session")
        verbose_name_plural = ("Sessions")
        ordering = ['-academic_session',]

    def __str__(self):
        return self.academic_session

    def get_absolute_url(self):
        return reverse("Session_detail", kwargs={"pk": self.pk})

class UniversityStaff(models.Model):
    fellow = models.ForeignKey("User", on_delete=models.CASCADE)

    staff_id  = models.CharField( max_length=50)
    first_name  = models.CharField( max_length=50)
    middle_name  = models.CharField( max_length=50,blank=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices= GENDER, max_length=6)
    designation  = models.CharField(help_text='As written in appointment letter', max_length=50)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    blood_group  = models.CharField(choices= BLOOD_GROUP,max_length=3)
    passport = models.ImageField( upload_to='staff/passport',default='programmer.png')
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("UniversityStaff")
        verbose_name_plural = ("Universities")
        ordering= ['-created_at',]

    def __str__(self):
        return self.fellow.surname

    def get_absolute_url(self):
        return reverse("UniversityStaff_detail", kwargs={"pk": self.pk})


class Postgrad(models.Model):
    fellow = models.ForeignKey("User", on_delete=models.CASCADE)

    staff_id  = models.CharField(help_text='Matric Id if student', max_length=50)
    first_name  = models.CharField( max_length=50)
    middle_name  = models.CharField( max_length=50,blank=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices= GENDER, max_length=6)
    level  = models.CharField(choices=PGLEVEL_CHOICES, max_length=10)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    blood_group  = models.CharField(choices= BLOOD_GROUP,max_length=3)
    department  = models.CharField(choices= DEPT, max_length=20,default='Nursing')
    #passport = models.ImageField( upload_to='staff/passport',)
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("Postgrad")
        verbose_name_plural = ("Postgrads")
        ordering= ['-created_at',]

    def __str__(self):
        return self.fellow.surname

    def get_absolute_url(self):
        return reverse("Postgrad_detail", kwargs={"pk": self.pk})

class Undergrad(models.Model):
    fellow = models.ForeignKey("User", on_delete=models.CASCADE)

    matric_id  = models.CharField( max_length=50)
    first_name  = models.CharField( max_length=50)
    middle_name  = models.CharField( max_length=50,blank=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices= GENDER, max_length=6)
    level  = models.CharField(choices=UGLEVEL_CHOICES, max_length=10)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    blood_group  = models.CharField(choices= BLOOD_GROUP,max_length=3)
    department  = models.CharField(choices= DEPT, max_length=20,default='Nursing')
    passport = models.ImageField( upload_to='undergrad/passport',)
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("Undergrad")
        verbose_name_plural = ("Undergrads")
        ordering= ['-created_at',]

    def __str__(self):
        return self.fellow.surname

    def get_absolute_url(self):
        return reverse("Postgrad_detail", kwargs={"pk": self.pk})


class VentureStaff(models.Model):
    fellow = models.ForeignKey("User", on_delete=models.CASCADE)

    staff_id  = models.CharField( max_length=50)
    first_name  = models.CharField( max_length=50)
    middle_name  = models.CharField( max_length=50,blank=True)
    surname = models.CharField( max_length=50)
    gender = models.CharField(choices= GENDER, max_length=6)
    designation  = models.CharField(help_text='As written in appointment letter', max_length=50)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    blood_group  = models.CharField(choices= BLOOD_GROUP,max_length=3)
    passport = models.ImageField( upload_to='staff/passport',default='programmer.png')
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = ("VentureStaff")
        verbose_name_plural = ("Ventures")
        ordering= ['-created_at',]

    def __str__(self):
        return self.fellow.surname

    def get_absolute_url(self):
        return reverse("VentureStaff_detail", kwargs={"pk": self.pk})
