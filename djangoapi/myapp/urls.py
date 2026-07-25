
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('login/', views.login_form, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    
    

    ]
