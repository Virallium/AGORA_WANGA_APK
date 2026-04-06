from django.db import models
class Services(models.Model):
    Idservices=models.AutoField(primary_key=True)
    Icon=models.ImageField(upload_to='services/')
    titre=models.CharField(max_length=100, default="lll")
    description=models.CharField(max_length=200,default='ddd' )
    def __str__(self):
        return self.titre
    
    
class Actus(models.Model):
    IdAct=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='actus/', default='actus/')
    mot_cle=models.CharField(max_length=100, default='kkk')
    titre=models.CharField(max_length=100, default='kkk')
    datepubliee=models.DateField(auto_created=True, default='23/12/2007')
    description=models.CharField(max_length=200, default='kkk')
    def __str__(self):
        return f"{self.mot_cle},{self.titre},{self.datepubliee}"
    
class Evenement(models.Model):
    IdEv=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='evenements/')
    titre=models.CharField(max_length=100, default='kkk')
    dateEv=models.DateField(default='23/12/2007')
    description=models.CharField(max_length=200, default='kkk')
    nbrpersonnes=models.IntegerField(default=12)
    def __str__(self):
        return f"{self.titre},{self.dateEv},{self.nbrpersonnes}"
    
class Question(models.Model):
    IdQuest=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100, default='kkk')
    datepubliee=models.DateField(auto_created=True)
    message=models.CharField(max_length=400, default='kkk')
    nbrpersonnes=models.IntegerField(default=21)
    def __str__(self):
        return f"{self.titre}, {self.message}"
class membres(models.Model):
    denomination=models.CharField(max_length=25, default='kkk')
    nom=models.CharField(max_length=25, default='kkk')
    prenom=models.CharField(max_length=25, default='kkk')
    postnom=models.CharField(max_length=25, default='kkk')
    img=models.ImageField(upload_to='membres/', default='membres/')
    localisation=models.CharField(max_length=25, default='kkk')
    specificite=models.CharField(max_length=100, default='kkk')
    def __str__(self):
        return f"{self.nom} {self.postnom} {self.specificite}"

class Admin(models.Model):
    IdAdmin=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=25, default='kkk')
    postnom=models.CharField(max_length=25, default='kkk')
    prenom=models.CharField(max_length=25, default='kkk')
    IdQuest=models.ForeignKey("Question", verbose_name="Id Question", on_delete=models.CASCADE)
    Idservices=models.ForeignKey("Services", verbose_name="Id Services", on_delete=models.CASCADE)
    IdAct=models.ForeignKey("Actus", verbose_name="Actus", on_delete=models.CASCADE)
    IdEv=models.ForeignKey("Evenement", verbose_name="Id Evenements", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

