from django.urls import path
from.views import *

app_name="expedition"


urlpatterns = [
  path('home/',home,name="home"),
  path('welcome/<str:name>',welcome, name="welcome"),
  path('list/',listExpeditions,name="list"),
  path('details/<int:pk>/', detailsExpedition, name="details"),
 path('supprimer/<int:pk>/', supprimerExpedition, name='supprimer'),
 path('expedition_list/', Exception_list.as_view(), name='expedition_list'),
   path('expedition_details_class/<int:pk>/',
         Exception_details.as_view(),
         name='expedition_details_class'),

 path(
    'expedition_delete/<int:pk>/',
    Expedition_delete.as_view(),
    name='expedition_delete_class'
),

 path(
    'expedition_create/',
    Expedition_create.as_view(),
    name='expedition_create_class'
),
  path(
      'expedition_update/<int:pk>/',
      Expedition_update.as_view(),
      name='expedition_update_class'
  ),


]



