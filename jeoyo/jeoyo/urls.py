"""jeoyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path, path
from django.conf.urls import include
from rest_framework import routers
#from main.views import UserViewSet, UserAPI, RegisterAPI, LoginAPI, ServiceAPI
from django.conf import settings
from django.conf.urls.static import static
#이걸루
from main import views

routers = routers.DefaultRouter()
routers.register('User', views.UserViewSet)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/User/', views.UserAPI.as_view()),
    re_path('api/Register/', views.RegisterAPI.as_view()),
    re_path('api/Login/', views.LoginAPI.as_view()),
    # re_path('api/Logout/', views.LogoutAPI.as_view()),
    re_path('api/Service/', views.ServiceAPI.as_view()),
    re_path('api/ServiceList/', views.ServiceListAPI.as_view()),
    re_path('api/AuctionList/', views.AuctionListAPI.as_view()),
    re_path('api/ServiceEndAPI/', views.ServiceEndAPI.as_view()),
    re_path('api/SearchServiceByUidAPI/', views.SearchServiceByUidAPI.as_view()),
    re_path('api/UsecreditAPI/', views.UsecreditAPI.as_view()),
    ## 프론트단
    path('', views.IndexView.as_view()), #main
    path('login/', views.Login.as_view()), #login
    path('logout/', views.Logout.as_view()), #logout
    path('register/',views.Register.as_view()),
    path('proser/create',views.Create.as_view()),
    path('proser/list',views.List.as_view()),
    path('proser/detail',views.Detail.as_view()),
    path('mypage',views.Mypage.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가
