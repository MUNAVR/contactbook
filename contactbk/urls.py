from django.urls import path
from.import views

urlpatterns=[
     path('',views.ct),
     path('ct',views.create),
     path('view',views.display),
     path('dtl',views.delete),
     path('mid',views.updatenam),
     path('mid2',views.updatenum)



]