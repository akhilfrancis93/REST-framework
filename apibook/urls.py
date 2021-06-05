"""bookapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import book_list,book_details,BookListView,BookDetailView,BookMixinView,BookDetailMixinView,LoginApi

urlpatterns = [
    path("books",book_list,name="books"),
    path("books/<int:id>",book_details,name="bookdetails"),
    path("cbooks",BookListView.as_view(),name="cbooks"),
    path("cbooks/<int:id>",BookDetailView.as_view(),name="cdetails"),
    path("mbooks",BookMixinView.as_view(),name="mbooks"),
    path("mbooks/<int:pk>",BookDetailMixinView.as_view(),name="mdetail"),
    path("login",LoginApi.as_view(),name="login")
]
