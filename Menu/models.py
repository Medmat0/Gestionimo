

from email.policy import default
from socketserver import ThreadingUDPServer
from unicodedata import category
from cv2 import multiply
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from socketserver import ThreadingUDPServer
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime


#classe utilisateur (login et mdp)



class User(AbstractUser):

    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=20)
    codePostal = models.CharField(max_length=20)
    photos = models.ImageField(upload_to ='uploads/', default ='/images/madrid.png' )



    def AjouterContact(Contact):
        pass

#classe administrateur

class Admin(User):
    class Meta:
        pass


    def AjouterEmploye():
        pass
    def SupprimerEmploye():
        pass
    def AttribuerDroitsEmploye():
        pass

#classe de propriétaire

class Contact(models.Model):
    class Meta:
        pass
    
    GENRE_CHOICES = (("HOMME", "Homme"), ("FEMME", "Femme"))

    genre = models.CharField( choices=GENRE_CHOICES, max_length=10, blank=True)
    prenom =models.CharField(max_length=100,null=True)
    nom=models.CharField(max_length=100,null=False )
    mail=models.CharField(max_length=100,null=True)
    telephone=models.CharField(max_length=100,null=True)
    societe=models.CharField(max_length=100,null=True)
    adresse=models.CharField(max_length=100,null=True)
    codePostal=models.CharField(max_length=100,null=True)
    ville= models.CharField(max_length=100,null=True)
    statut=models.CharField(max_length=100,null=True)
    capitalSocial=models.CharField(max_length=100,null=True)
    numRCS=models.CharField(max_length=100,null=True)
    villeRCS=models.CharField(max_length=100,null=True)
   
   
    def __str__(self):
      return self.nom +' Prenom : ' + self.prenom



#classe pour chaque pièce du produit




#classe pour stocker les phots

    #il faut une clé étrangère représentant le produit

#classe pour stocker les docs




    #il faut une clé étrangère représentant le produit


#classe pour stocker les liens des portails internet

class Transfert(models.Model):

    link = models.URLField()

#classe de Produit (standard)
 

class Produit(models.Model):
    class Meta:
        pass
    CHOIX_ADDRESS = (("OUI", "oui"), ("NO", "non"))
    ETAPE_CHOICES = (("EN_COURS", "en cours"), ("EN_ATTENTE", "en attente"), ("EXPIRE", "expiré"))
    CHOIX_BIEN = (("BUREAU", "Bureau"), ("LOCAL_COMMERCIAL","Local Commercial"), ("TERRAIN","Terrain"), ("ENTREPOT","Entrepôt"))
    CHOIX_MANDAT = (("EXCLUSIVE", "exclusive"), ("NON_EXCLUSIVE", "non exclusive"))
    CHOIX_CAT = (("LOCATION", "location"), ("VENTE", "vente"))
    
    #general
    metier = models.CharField(max_length=50)
    categorie = models.CharField(choices=CHOIX_CAT, max_length=10, default=None)
    etape = models.CharField(max_length=10, choices=ETAPE_CHOICES, default=None)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    typeMandat = models.CharField(choices=CHOIX_MANDAT, max_length=20, default=None)
    proprietaire = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=20)
    codePostal = models.CharField(max_length=20)
    affichAdresse = models.CharField(choices=CHOIX_ADDRESS, max_length=10, default="OUI")
    prixNetVendeur = models.DecimalField(max_digits=5, decimal_places=2)
    prixAffiche = models.DecimalField(max_digits=5, decimal_places=2)
    honoraire = models.DecimalField(max_digits=5, decimal_places=2)
    montantHonoraire = models.DecimalField(max_digits=5, decimal_places=2)

    #information
    surfaceTotale = models.DecimalField(max_digits=5, decimal_places=2)
    typeBien = models.CharField(choices=CHOIX_BIEN, max_length=50, default=None)
    nombrePieces = models.IntegerField(default=0)
    tailleTerrain = models.DecimalField(max_digits=5, decimal_places=2)
    
    #commentaire 
    commentaire = models.TextField(blank=True)
    TitreAnnonce = models.CharField(max_length=30,blank=True)
    
    def __str__(self):
        return 'categorie : ' + self.categorie +' , type de bien :  '+ self.typeBien

    def AjouterProduit(self, ):
        pass

    def SupprimerProduit(self, ):
        pass

    def AfficherProduit(self, ):
        pass

    def ModifierProduit(self, ):
        pass

    def AfficherAdresse(self, ):
        pass

#photos

class Photo(models.Model):

    image = models.ImageField(upload_to ='produit/',)
    date_created = models.DateTimeField(auto_now_add=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE , related_name="photos_set")

# GED
class GED(models.Model):
    
    fichier = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE )

# surface
class Surface(models.Model):
        
    nom = models.CharField(max_length=50)
    taille = models.FloatField(default=0)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE )


#classe si le produit est un entrepot et elle hérite de la classe Produit

class Entrepot(models.Model):
    class Meta:
        pass
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    HauteurSousPlafond = models.DecimalField(max_digits=5, decimal_places=2)
    typeConstruction = models.CharField(max_length=50)
    ChargesCopropriete = models.DecimalField(max_digits=5, decimal_places=2)
     
     
    def __str__(self):
      return self.typeConstruction

#classe si le produit est un bureau et elle hérite de la classe Produit

class Bureau(models.Model):
    class Meta:
        pass
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)

#classe si le produit est un local commercial et elle hérite de la classe Produit

class LocalCommercial(models.Model):
    class Meta:
        pass
    CHOIX_PARK = (("OUI", "oui"), ("NO", "non"))

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    lineaireVitrine = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=50)
    derniereActivite = models.DateField(null=True)
    parking = models.CharField(choices=CHOIX_PARK, max_length=10, default="NON")
    detailsParking = models.TextField()

    def __str__(self):
       return self.lineaireVitrine 
    
    

#classe si le produit est un terrain et elle hérite de la classe Produit

class Terrain(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    hauteurMaxConstruction = models.FloatField(default=0)
    coefEmpriseSol = models.IntegerField(default=0)
    prixConstruction = models.DecimalField(max_digits=5, decimal_places=2)
    coefEspaceVert = models.IntegerField(default=0)

# new

class Demande(models.Model):
    class Meta:
        pass

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    resume = models.TextField(default=None)
    ville = models.CharField(max_length=20, default=None)
    codePostal = models.CharField(max_length=20, default=None)
    prixmax = models.DecimalField(max_digits=5, decimal_places=2 , default=None)
    nombrepices = models.DecimalField(max_digits=5, decimal_places=2 , default=None)
    surface = models.DecimalField(max_digits=5, decimal_places=2 , default=None)
    prixmin = models.DecimalField(max_digits=5, decimal_places= 2, default=None)
    typeproduit = models.CharField(max_length=20, default= None)
    category = models.CharField(max_length=20, default=None)
        
    


class Mandat(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    honoraire = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    date=models.DateField(default=datetime.date.today)

class Offre(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)


class Achat(models.Model):
    class Meta:
        pass

    offer = models.ForeignKey(Offre, on_delete=models.CASCADE)
    dateVisite = models.DateTimeField(default=timezone.now)
    honoraireHT = models.DecimalField(max_digits=5, decimal_places=2)
    honoraireTTC = models.DecimalField(max_digits=5, decimal_places=2)
    prixPropose = models.DecimalField(max_digits=5, decimal_places=2)
    indemnite = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    activite = models.CharField(max_length=50)
    delaiValidite = models.DateTimeField(default=timezone.now)
     # conditions suspensives

    financement = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=5, decimal_places=2)
    taux = models.DecimalField(max_digits=5, decimal_places=2)
    duree = models.IntegerField()
    permisConstruction = models.BooleanField(default=False)
    droitPreemption = models.BooleanField(default=False)
    faculteSubstitution = models.BooleanField(default=False)

class Location(models.Model):
    class Meta:
        pass

    CHOIX_BAIL = (("DEROGATOIRE", "dérogatoire"), ("COMMERCIAL", "commercial"), ("PROFESSIONNEL", "professionnel"))

    offer = models.ForeignKey(Offre, on_delete=models.CASCADE)
    dateVisite = models.DateTimeField(default=timezone.now)
    honoraireHT = models.DecimalField(max_digits=5, decimal_places=2)
    honoraireTTC = models.DecimalField(max_digits=5, decimal_places=2)
    loyerPropose = models.DecimalField(max_digits=5, decimal_places=2)
    charges = models.DecimalField(max_digits=5, decimal_places=2)
    chargesAcquereur = models.BooleanField(default=False)
    chargesVendeur = models.BooleanField(default=False)
    bail = models.CharField(choices=CHOIX_BAIL, max_length=20, default=None)
    dureeBail = models.IntegerField()
    depotGranti = models.DecimalField(max_digits=5, decimal_places=2)
    taxeFrontiere = models.DecimalField(max_digits=5, decimal_places=2)
     # conditions suspensives

    financement = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=5, decimal_places=2)
    taux = models.DecimalField(max_digits=5, decimal_places=2)
    duree = models.IntegerField()
    permisConstruction = models.BooleanField(default=False)
    droitPreemption = models.BooleanField(default=False)
    faculteSubstitution = models.BooleanField(default=False)

class Estimation(models.Model):
    class Meta:
        pass

    product = models.ForeignKey(Produit, on_delete=models.CASCADE)









