from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class diabetes_disease_model(models.Model):

    Pregnancies=models.CharField(max_length=300)
    Glucose=models.CharField(max_length=300)
    BloodPressure=models.CharField(max_length=300)
    SkinThickness=models.CharField(max_length=300)
    Insulin=models.CharField(max_length=300)
    BMI=models.CharField(max_length=300)
    DiabetesPedigreeFunction=models.CharField(max_length=300)
    Age=models.CharField(max_length=300)



class diabetes_disease_prediction(models.Model):

    Pregnancies = models.CharField(max_length=300)
    Glucose = models.CharField(max_length=300)
    BloodPressure = models.CharField(max_length=300)
    SkinThickness = models.CharField(max_length=300)
    Insulin = models.CharField(max_length=300)
    BMI = models.CharField(max_length=300)
    DiabetesPedigreeFunction = models.CharField(max_length=300)
    Age = models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)
    Status= models.CharField(max_length=300)



class detection_results_model(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio_model(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



