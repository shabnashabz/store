from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('new_page', views.new_page, name='new_page'),
     path('new_page.html', RedirectView.as_view(url='new_page', permanent=True)),
   
]


    
