"""booktime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from main import forms 
from .  import views
from main import models
urlpatterns = [
    # path('admin/', admin.site.urls),
    path(
        "address/",
        views.AddressListView.as_view(),
        name="address_list"
    ),
    path(
        "address/create/",
        views.AddressCreateView.as_view(),
        name="address_create"
    ),
    path(
        "address/<int:pk>",
        views.AddressUpdateView.as_view(),
        name="address_update"
    ),
    path(
        "address/<int:pk>/delete",
        views.AddressDeleteView.as_view(),
        name="address_delete"
    ),
     path(
        "product/<slug:slug>/",
        DetailView.as_view(
            template_name="product_detail.html",
            model=models.Product),
        name="product",
    ),
    path(
            "products/<slug:tag>/",
            views.ProductListView.as_view(),
            name="products"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            form_class=forms.AuthenticationForm
        ),
        name="login"
    ),
    path(
            "signup/",
            views.SignupView.as_view(),
            name="signup"        
    ),
    path(
            "about-us/", 
            TemplateView.as_view(template_name="about.html")
    ),
    path(
            "contact-us/", 
            views.ContactUsView.as_view(),
            name="contact_us"
    ),
    path(
            "", 
            TemplateView.as_view(template_name="home.html")),    
    # path("")
]
