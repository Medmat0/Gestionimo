from asyncio.windows_events import NULL
from time import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from .models import  User
from num2words import num2words
from .form import *
from django.views.generic import View
from .process import html_to_pdf
from decimal import Decimal
from django.utils import timezone
from datetime import datetime




 

def choixis4(choix):
  global prix2
  prix2=choix

def choixis5(choix):
  global honoraire2
  honoraire2 = choix

def choixis6(choix):
  global type2
  type2 = choix

def choixis2(choix2):
    global choix_prod 
    choix_prod= choix2

def choixis9(choix9):
    global nombre
    nombre = choix9


# authentification 
def index(request):
   if(request.method == "POST"):
    name = request.POST.get('name')
    pasw = request.POST.get('pswd')
    print(name)
    print(pasw)
    user1= User.objects.get(username = "admin")
    if user1 is not None:
     print(user1.username)
    user = authenticate(request, username = name ,  password = pasw)
    print(user)
    if user is None :
      context = {"eror ": "Invalid username or password"}
      print("echoé")
    else:
        user1= User.objects.get(username = name)
        image = user1.photos
       
        print(image.url)
        nomuser = user1.username
        print(nomuser)
        
        context = {"succes": "Welcome",
                    "url"  : image.url,
                     "name" : nomuser,      }
        print("hello")
        return render(request,'login/Produit.html', context   )
   else:
      print("eror") 
  
   return render(request,'login/Authen.html')




def Menu(request):
   return render(request,'login/Menu.html')




def formst(request):
   entrepot = Entrepotform()
   Produit1 = Produitform()
   Surface1 = SurfaceForm()
   surface1 = Surface()
   Localcom = LocalcomForm()
   Localcomf = LocalCommercial()
   terrain = TerrainForm()
   Contact = formC()
   Terrain_tab = Terrain()
   Entrepot_tab = Entrepot()
   photo = PhotosForm()
   photoT = Photo()
   ged = GED()
   gedForm = GedForm()
   
   bureau = Bureau()
   global choix1 
   global eror 
   eror = " "
   if 'contact' in request.POST: 
      print("button pressed")
   if(request.method == "POST" and 'contact' in request.POST):
      formcontact = formC(request.POST)
      if formcontact.is_valid():
         formcontact.save()
         print('done contact')
      else : print(formcontact.errors)
   if (request.method == "POST" and 'prod' in request.POST):
   
      form = Produitform(request.POST)
      choix = request.POST.get('typeBien')
      nb = int (request.POST.get('nombrePieces'))
      
      
      if form.is_valid():
        form.save()
        
        print("done")
        print(choix)
        context = { 'Produit': Produit1,
              'choix': choix,
              'Entrepot': entrepot,
              'Localcom': Localcom,
              'Terrain': terrain,
              'Surface': Surface1,
              'photo'  : photo,
              'ged' : gedForm,
              'nbr': range(nb),}
       
        choixis(choix)
        choixis9(nb)
         #formchoix1 = formchoix
        return render(request,'login/Formstest.html',context)

      else :
            
            eror =form.errors
   
   elif ( request.method== "POST" and 'send1' in request.POST ):
      print("choix est :" +choix1)
      last_product = Produit.objects.last()

      if ('TERRAIN' == choix1 ): 
        for i in range(nombre):
           surface1.nom = request.POST.get('nom')
           print( request.POST.get('nom'))
           surface1.taille = request.POST.get('taille')
           surface1.produit = Produit.objects.last()
           surface1.save()
        Terrain_tab.product = last_product
        Terrain_tab.coefEmpriseSol = request.POST.get('coefEmpriseSol')
        Terrain_tab.coefEspaceVert = request.POST.get('coefEspaceVert')
        Terrain_tab.hauteurMaxConstruction = request.POST.get('hauteurMaxConstruction')
        Terrain_tab.prixConstruction = request.POST.get('prixConstruction')
        Terrain_tab.save()
      elif ('ENTREPOT' == choix1) :
       print("im here")
       for i in range(nombre):
           surface1.nom = request.POST.get('nom')
           surface1.taille = request.POST.get('taille')
           surface1.produit = Produit.objects.last()
           surface1.save()
       Entrepot_tab.product = last_product
       Entrepot_tab.typeConstruction = request.POST.get('typeConstruction')
       Entrepot_tab.HauteurSousPlafond = request.POST.get('HauteurSousPlafond')
       Entrepot_tab.ChargesCopropriete = request.POST.get('ChargesCopropriete')
       Entrepot_tab.save()

      elif ('LOCAL_COMMERCIAL' == choix1 ): 
          for i in range(nombre):
             surface1.nom = request.POST.get('nom')
             print( request.POST.get('nom'))
             surface1.taille = request.POST.get('taille')
             surface1.product = last_product
             surface1.save()

          Localcomf.product = last_product
          Localcomf.emplacement = request.POST.get('emplacement')
          Localcomf.parking = request.POST.get('parking')
          Localcomf.detailsParking = request.POST.get('detailsParking')
          Localcomf.lineaireVitrine = request.POST.get('lineaireVitrine')
          date1 = request.POST.get('derniereActivite')
          date2 = datetime.strptime(date1, "%Y-%m-%d").date()

          Localcomf.derniereActivite = date2
          Localcomf.save()
      if ( 'BUREAU' == choix1):
        for i in range(nombre):
           surface1.nom = request.POST.get('nom')
           surface1.taille = request.POST.get('taille')
           surface1.produit = Produit.objects.last()
           surface1.save()
          
        bureau.product = Produit.objects.last()
        bureau.save()
        
        
     # else:
        # print("form null ") 
   elif ( request.method== "POST" and 'commentaire1' in request.POST ):
     produit = Produit.objects.latest('typeBien')

     comme = request.POST.get('commentaire')
     titre = request.POST.get('TitreAnnonce')
     produit.TitreAnnonce = titre
     produit.commentaire = comme
     produit.save() 
            
  
   elif ( request.method== "POST" and 'photos' in request.POST ):
       photoT.image = request.FILES['image']
       photoT.date_created = datetime.now
       photoT.produit = Produit.objects.last()
       photoT.save()
         
   elif(request.method == "POST" and 'ged'in request.POST):
        ged.fichier = request.FILES['fichier']
        ged.date_created = datetime.now
        ged.produit = Produit.objects.last()
        ged.save()


   
   else : 
      print("button not save")
   dataImage = Photo.objects.all() 
   dataGestion = GED.objects.all()
   con = { 'Produit' : Produit1,
           'Contact' : Contact,
            'photo'  : photo,
            'dataImage': dataImage,
            'ged': gedForm,
            'dataGestion': dataGestion,
            'eror': eror }
   return render(request,'login/Formstest.html', con)

   
def choixis(choix2):
    global choix1 
    choix1= choix2
# ajouter recherche et ajout dans le menu du prod 

def Affichage(request):
   Product = Produit.objects.all
   Photos = Photo.objects.all
   #Product.photos_set.all()
   
   if(request.method == 'POST'):
      search = request.POST.get('search')
   context = { "Produit": Product,
               "Photos" : Photos,}
   return render(request,'login/affichage.html', context)


   
# Create your views here.
def formMandat(request):

  Mandat1 = MandatForm()
  global choix, date1,date2, prix2, honoraire2, type2, last_mandat, prod_mandat
  choix = Produit.objects.last()

  date1 = datetime.now()
  date2 = date1.strftime("%Y-%m-%d")

  if (request.method == "POST" and "prod" in request.POST):
    print("hi")
    prod = request.POST.get('product')
    print(prod)
    choix= Produit.objects.get(pk = prod)
    prix = choix.prixAffiche
    honoraire = choix.honoraire
    type1 = choix.typeMandat
    print(prix)
    print(honoraire)
    print(type1)
    data1 = {'Mandat' : Mandat1,
            'prix' : prix,
            'honoraire' : honoraire,
            'date' : date2,
              }

    choixis4(prix)
    choixis5(honoraire)
    choixis6(type1)
    return render(request,'Transaction/mandat.html',data1)

  elif (request.method == "POST" and "mandat" in request.POST):
    print("hello")
  
    mandat_tab = Mandat()
    mandat_tab.product = choix
    mandat_tab.prix = prix2
    mandat_tab.honoraire = honoraire2
    mandat_tab.date = date2
    mandat_tab.save()
    print("saved1")

    print(type2)
      
    data2 = {'Mandat' : Mandat1,
            'typeMandat': type2
           }
    return render(request,'Transaction/mandat.html',data2)
  else : 
      print("button not save")


  con = { 'Mandat' : Mandat1,
        
          
       }          
  return render(request,'Transaction/mandat.html', con)




#------ Exclusif ---- # 
class GenerateMandatPDF(View):
     def get(self, request, *args, **kwargs):
        global mandat_obj, produit_pk, contact_pk, date1, date2
        mandat_obj = Mandat.objects.last()
        produit_pk = mandat_obj.product
        #produit_obj = Produit.objects.get(pk = produit_pk)
        contact_pk = produit_pk.proprietaire
        #contact_obj = Contact.objects.get(pk = contact_pk)

        date1 = datetime.now()
        date2 = date1.strftime("%d/%m/%Y")
         
        # getting the template
        context=  {'numMandat': mandat_obj.pk, 
                   'nomSociete': contact_pk.societe,
                   'capitalSocial': contact_pk.capitalSocial,
                   'codePostalSiege': contact_pk.codePostal,
                   'adresseSociete': contact_pk.adresse,
                   'villeSociete': contact_pk.ville,
                   'numRCS': contact_pk.numRCS,
                   'villeRCS': contact_pk.villeRCS,
                   'nomContact': contact_pk.nom,
                   'prenomContact': contact_pk.prenom,
                   'adresseProduit': produit_pk.adresse,
                   'codePostalProduit': produit_pk.codePostal,
                   'villeProduit': produit_pk.ville,
                   'prixAffiche': produit_pk.prixAffiche,
                   'prixAfficheLettre': num2words(produit_pk.prixAffiche, lang='fr'),
                   'dateToday': date2,
                   }
        pdf = html_to_pdf('Transaction/mandatPDF.html', context)
       
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
#--- Non exclusif --- #
class GenerateMandatPDF2(View):
     def get(self, request, *args, **kwargs):
        global mandat_obj, produit_pk, contact_pk, date1, date2
        mandat_obj = Mandat.objects.last()
        produit_pk = mandat_obj.product
        
        contact_pk = produit_pk.proprietaire
       

        date1 = datetime.now()
        date2 = date1.strftime("%d/%m/%Y")
         
        # getting the template
        context=  {'numMandat': mandat_obj.pk, 
                   'nomSociete': contact_pk.societe,
                   'capitalSocial': contact_pk.capitalSocial,
                   'codePostalSiege': contact_pk.codePostal,
                   'adresseSociete': contact_pk.adresse,
                   'villeSociete': contact_pk.ville,
                   'numRCS': contact_pk.numRCS,
                   'villeRCS': contact_pk.villeRCS,
                   'nomContact': contact_pk.nom,
                   'prenomContact': contact_pk.prenom,
                   'adresseProduit': produit_pk.adresse,
                   'codePostalProduit': produit_pk.codePostal,
                   'villeProduit': produit_pk.ville,
                   'prixAffiche': produit_pk.prixAffiche,
                   'prixAfficheLettre': num2words(produit_pk.prixAffiche, lang='fr'),
                   'dateToday': date2,
                   }
        pdf = html_to_pdf('Transaction/mandatPDF2.html', context)
       
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#----- Offre ---- #
def formOffre(request):
   Offre1 = OffreForm()
   #Produit = ProductForm()
   Achat_f = AchatForm()
   Location_f = LocationForm()
   location_tab = Location()
   achat_tab = Achat()
   global choix1, choix_prod

   if (request.method == "POST" and 'offre' in request.POST):
      prod = request.POST.get('product')
      print(prod)
      choix3= Produit.objects.get(pk = prod)
      choix = choix3.categorie
      print("le choix est " + choix)
      honoTTC = choix3.honoraire * Decimal( 1.20)
      default_dataL ={'dateVisite': timezone.now,
                      'honoraireHT': choix3.honoraire,
                      'honoraireTTC': honoTTC,
                      'loyerPropose': choix3.prixAffiche,
                      'montant': 0,
                      'taux': 0,
                      'duree': 0,
                      'apport': 0
                       }
      
      offre_tab = Offre()
      offre_tab.product = choix3
      offre_tab.save()
        
      print("done")
        
      context = { 'Offre': Offre1,
              'choix': choix,
              'Achat': Achat_f,
              'Location': Location_f,
              'dic': default_dataL,
              }
       
      choixis(choix)
      choixis2(choix3)

         
      return render(request,'   /offre.html',context)
    
   elif ( request.method== "POST" and 'send' in request.POST ):
        print("hey")
        if(choix1 == 'LOCATION' ):
                last_offer = Offre.objects.last()
              
                #formchoix = LocationForm(request.POST or None)
                location_tab.offer = last_offer
                location_tab.dateVisite = request.POST.get('dateVisite')
                location_tab.honoraireHT = request.POST.get('honoraireHT')
                location_tab.honoraireTTC = request.POST.get('honoraireTTC')
                location_tab.loyerPropose = request.POST.get('loyerPropose')
                location_tab.charges = request.POST.get('charges')
                ch_acq= request.POST.get('chargesAcquereur')
                if ch_acq == 'on':
                    ch_acq = True
                else:
                    ch_acq = False
                location_tab.chargesAcquereur = ch_acq
                
                ch_V= request.POST.get('chargesVendeur')
                if ch_V == 'on':
                    ch_V = True
                else:
                    ch_V = False
                location_tab.chargesVendeur = ch_V


                location_tab.bail = request.POST.get('bail')
                location_tab.dureeBail = request.POST.get('dureeBail')
                location_tab.depotGranti = request.POST.get('depotGranti')
                location_tab.taxeFrontiere = request.POST.get('taxeFrontiere')
                
                fin= request.POST.get('financement')
                if fin == 'on':
                    fin = True
                else:
                    fin = False
                location_tab.financement = fin


                location_tab.montant = request.POST.get('montant')
                location_tab.taux = request.POST.get('taux')
                location_tab.duree = request.POST.get('duree')

                perCons= request.POST.get('permisConstruction')
                if perCons == 'on':
                    perCons = True
                else:
                    perCons = False
                location_tab.permisConstruction = perCons

                droitPre= request.POST.get('droitPreemption')
                if droitPre == 'on':
                    droitPre = True
                else:
                    droitPre = False
                location_tab.droitPreemption = droitPre


                facSub= request.POST.get('faculteSubstitution')
                if facSub == 'on':
                    facSub = True
                else:
                    facSub = False
                location_tab.faculteSubstitution = facSub


                location_tab.save()
                print("okay")
                context2 = {'Offre': Offre1,
                            'last_offer': last_offer,
                }
                return render(request,'Transaction/offre.html', context2)

                
        elif( choix1 == 'VENTE'):
                #formchoix = AchatForm(request.POST)
                last_offer = Offre.objects.last()
                achat_tab.offer = last_offer
                achat_tab.dateVisite = request.POST.get('dateVisite')
                achat_tab.honoraireHT = request.POST.get('honoraireHT')
                achat_tab.honoraireTTC = request.POST.get('honoraireTTC')
                achat_tab.prixPropose = request.POST.get('prixPropose')
                achat_tab.indemnite = request.POST.get('indemnite')
                achat_tab.activite = request.POST.get('activite')
                achat_tab.delaiValidite = request.POST.get('delaiValidite')

                fin= request.POST.get('financement')
                if fin == 'on':
                    fin = True
                else:
                    fin = False
                achat_tab.financement = fin


                achat_tab.montant = request.POST.get('montant')
                achat_tab.taux = request.POST.get('taux')
                achat_tab.duree = request.POST.get('duree')
                achat_tab.apport = request.POST.get('apport')

                perCons= request.POST.get('permisConstruction')
                if perCons == 'on':
                    perCons = True
                else:
                    perCons = False
                achat_tab.permisConstruction = perCons

                droitPre= request.POST.get('droitPreemption')
                if droitPre == 'on':
                    droitPre = True
                else:
                    droitPre = False
                achat_tab.droitPreemption = droitPre


                facSub= request.POST.get('faculteSubstitution')
                if facSub == 'on':
                    facSub = True
                else:
                    facSub = False
                achat_tab.faculteSubstitution = facSub


                achat_tab.save()
                print("okay")
                context3 = {'Offre': Offre1,
                            'last_offer': last_offer,
                }
                return render(request,'Transaction/offre.html', context3)


         
        else:
            print( " failed xD")
        
        
   else : 
      print("button not save")
   con = { 'Offre' : Offre1,
 }
   return render(request,'Transaction/offre.html', con)


# -------- Demande ----------#
def formDemande(request):
  Demande1 = DemandeForm()
  Contactf = formC()
  demandtab = Demande()

  if (request.method == "POST"):
       demandtab.category = request.POST.get("Categorie")
       demandtab.typeproduit = request.POST.get("type")
       demandtab.nombrepices = request.POST.get("nombtrpieces")
       demandtab.surface = request.POST.get("surface")
       demandtab.prixmax = request.POST.get("Budget-max")
       demandtab.prixmin = request.POST.get("Bugdet-min")
       demandtab.ville = request.POST.get("ville")
       demandtab.codePostal = request.POST.get("codepostal")
       demandtab.save()

       lechoix = Produit.objects.get('category' == request.POST.get("Categorie")
                                    , 'typeBien' == request.POST.get("type") ,
                                     'prixAffiche' >= request.POST.get("Bugdet-min") and 'prixAffiche' <= request.POST.get("Budget-max"),
                                      'codePostal' == request.POST.get("codepostal"))
       return render(request,'Transaction/demande.html', {'choix' : lechoix})
      
  elif(request.method == "POST" and 'contact' in request.POST):
      formcontact = formC(request.POST)
      if formcontact.is_valid():
         formcontact.save()
         print('done contact')
      else : print(formcontact.errors)
  else : 
      print("button not save")

  con = { 'Demande' : Demande1,
          'Contact' : Contactf}
  return render(request,'Transaction/demande.html', con)


class OffreAchatPDF(View):
   def get(self, request, *args, **kwargs):
        global achat_obj, offre_obj, contact_obj, user_obj, produit_obj, date1, date2
        achat_obj = Achat.objects.last()
        offre_obj = achat_obj.offer
        produit_obj = offre_obj.product
        contact_obj = produit_obj.proprietaire
        user_obj = produit_obj.utilisateur

        date1 = datetime.now()
        date2 = date1.strftime("%d/%m/%Y")
         
        # getting the template
        context=  {
                   'codePostalSiege': contact_obj.codePostal,
                   'adresseSociete': contact_obj.adresse,
                   'villeSociete': contact_obj.ville,
                   'nomContact': contact_obj.nom,
                   'prenomContact': contact_obj.prenom,
                   'nomUser': user_obj.last_name,
                   'prenomUser': user_obj.first_name,
                   'bien': produit_obj.typeBien,
                   'adresseProduit': produit_obj.adresse,
                   'codePostalProduit': produit_obj.codePostal,
                   'villeProduit': produit_obj.ville,
                   'dateVisite': achat_obj.dateVisite,
                   'montant': achat_obj.montant,
                   'taux': achat_obj.taux,
                   'duree': achat_obj.duree,
                   'apport': achat_obj.apport,
                   'prixPropose': achat_obj.prixPropose,
                   'prixAfficheLettre': num2words(achat_obj.prixPropose, lang='fr'),
                   'dateToday': date2,
                   }
        pdf = html_to_pdf('Transaction/offrePDF.html', context)
       
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




def estimationPage(request):
   Estimationf = EstimationForm()
   
   global choix1 

   
   if (request.method == "POST" and 'estimation' in request.POST):
      form = EstimationForm(request.POST)
      
      if form.is_valid():
        form.save()
        print("done")
        
        context = { 'Estimation': Estimationf}
       
        return render(request,'Transaction/estimation.html',context)

      else : print(form.errors)
   else : 
      print("button not save")
   con = { 'Estimation': Estimationf}
   return render(request,'Transaction/estimation.html', con)


class GenerateEstimationPDF(View):
   def get(self, request, *args, **kwargs):
        global Estimation_obj, contact_obj, user_obj, produit_obj, date1, date2
        Estimation_obj = Estimation.objects.last()
        produit_obj = Estimation_obj.product
        contact_obj = produit_obj.proprietaire
        user_obj = produit_obj.utilisateur

        date1 = datetime.now()
        date2 = date1.strftime("%d/%m/%Y")
         
        # getting the template
        context=  {
                   'codePostalSiege': contact_obj.codePostal,
                   'adresseSociete': contact_obj.adresse,
                   'villeSociete': contact_obj.ville,
                   'nomContact': contact_obj.nom,
                   'prenomContact': contact_obj.prenom,
                   'nomUser': user_obj.last_name,
                   'prenomUser': user_obj.first_name,
                   'bien': produit_obj.typeBien,
                   'adresseProduit': produit_obj.adresse,
                   'codePostalProduit': produit_obj.codePostal,
                   'villeProduit': produit_obj.ville,
                   'comment': produit_obj.commentaire,
                   'prixPropose': produit_obj.prixAffiche,
                   'prixAfficheLettre': num2words(produit_obj.prixAffiche, lang='fr'),
                   'dateToday': date2,
                   }
        pdf = html_to_pdf('Transaction/estimationPDF.html', context)
       
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

