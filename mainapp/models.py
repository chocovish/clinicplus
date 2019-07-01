from django.db import models
# Create your models here.

blgp = (('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-"'))
sexch = (('M','Male'),('F','Female'),('O','Other'))

class Patient(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,choices=sexch)
    phone = models.CharField(max_length=14,unique=True)
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=blgp)

    def __str__(self):
        return self.name



class VisitDetail(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateField(auto_now_add=True)
    disease_info = models.CharField(max_length=1000,blank=True,null=True)
    treatment = models.CharField(max_length=600,blank=True,null=True)
    report = models.CharField(max_length=200,blank=True,null=True)
    remarks = models.CharField(max_length=600,blank=True,null=True)
    
    def __str__(self):
        return self.patient.name