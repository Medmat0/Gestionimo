from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('Menu', views.Menu , name='Menu'),
    path('Form', views.formst , name="formst"),
    path('Affichage', views.Affichage , name="Affichage"),   
    path('mandat/', views.formMandat, name='mandat'),
    path('demande/', views.formDemande, name='demande'),
    path('offre/', views.formOffre, name='offre'),
    path('estimation/', views.estimationPage, name="estimation"),
    path('mandatPDF/', views.GenerateMandatPDF.as_view(), name="pdfcreate"),
    path('mandatPDF2/', views.GenerateMandatPDF2.as_view(), name="pdfcreate2"),
    path('offrePDF/', views.OffreAchatPDF.as_view(), name="pdfcreateAchat"),
    path('mandatPDF2/', views.GenerateMandatPDF2.as_view(), name="pdfcreate2"),
    path('estimationPDF/', views.GenerateEstimationPDF.as_view(), name="estimationpdf"),
]
