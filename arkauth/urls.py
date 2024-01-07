from django.urls import path
from arkauth import views

urlpatterns = [
   path('signup/',views.signup,name='signup'),
   path('login/',views.handlelogin,name='handlelogin'),
   path('logout/',views.handlelogout,name='handlelogout'),
   path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
   path('request_reset_email/',views.RequestRestEmailView.as_view(),name='request_reset_email'),
   path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password')
]