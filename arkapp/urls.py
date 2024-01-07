


from django.urls import path
from arkapp import views

urlpatterns = [
   path('',views.home,name='home'),
   path('checkout/',views.checkout,name='checkout'),
   path('finished/',views.finished,name='finished'),
]
