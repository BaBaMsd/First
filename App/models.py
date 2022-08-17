from datetime import datetime
from distutils.command.upload import upload
import os
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
def get_name(instence, filename):
    nom = filename
    cd = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = '%s%s' % (cd, nom)
    return os.path.join('uploads/',filename)

class Etudiant(models.Model):
    nom_etu = models.CharField(max_length=25)
    prenom_etu = models.CharField(max_length=25)
    dt_nai_etu = models.DateField()
    dt_iscri_etu = models.DateField()
    lieu_nai_etu = models.CharField(max_length=25)
    sexe_etu = models.CharField(max_length=25)
    adresse_etu = models.TextField(max_length=25)
    image_etu = models.ImageField(upload_to = get_name, blank=True, null=True )
    classe_etu = models.CharField(max_length=25)
    an_sco = models.CharField(max_length=25)
    nom_ag = models.CharField(max_length=25, default="")
    num_ag = models.CharField(max_length=25, default="")

class Frais(models.Model):
    etu = models.CharField(max_length=25)
    prix = models.IntegerField()
    dt_pay = models.DateField()
    ann_sco = models.CharField(max_length=25, default="")

class Etu_classe(models.Model):
    class_nom = models.CharField(max_length=25)
    ann_sco = models.CharField(max_length=25)

class AnneScolaire(models.Model):
    ann_sco_nom = models.CharField(max_length=25)

class Absence(models.Model):
    dt_abs = models.DateField()
    ann_sco = models.CharField(max_length=25)
    justification = models.CharField(max_length=30)
    etu_id = models.CharField(max_length=30)

class Matier(models.Model):
    matier_nom = models.CharField(max_length=25)

class Note(models.Model):
    etu_nt = models.CharField(max_length=25)
    an_nt = models.CharField(max_length=25)
    cl_nt = models.CharField(max_length=25)
    matier_nt = models.CharField(max_length=25)
    dev_nt = models.FloatField(max_length=10)
    ex_nt = models.FloatField(max_length=10)


    