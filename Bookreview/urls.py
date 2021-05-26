"""Bookreview URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bookreviews.views import index, adminlogin, adminloginentered, viewvendordata, activatevendor, logout, \
    viewbooklist, viewuserdata, activateuser, svm, navie, adminpage
from bookvendor.views import vendorlogin, vendorregister, vendorlogincheck, uploadbook, bookpage
from user.views import userlogin, userlogincheck, userregister, reviewofbooks, usersearchresult1, search, \
    usersearchresult, viewdetails, userpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^vendorlogin/',vendorlogin,name="vendorlogin"),
    url(r'^vendorregister/',vendorregister,name="vendorregister"),
    url(r'^vendorlogincheck/',vendorlogincheck,name="vendorlogincheck"),
    url(r'^adminlogin/',adminlogin,name="adminlogin"),
    url(r'^adminloginentered/',adminloginentered,name="adminloginentered"),
    url(r'^viewvendordata/',viewvendordata,name="viewvendordata"),
    url(r'^activatevendor/',activatevendor,name="activatevendor"),
    url(r'^logout/',logout,name="logout"),
    url(r'^uploadbook/',uploadbook,name="uploadbook"),
    url(r'^viewbooklist/',viewbooklist,name="viewbooklist"),
    url(r'^userlogin/',userlogin,name="userlogin"),
    url(r'^userlogincheck/',userlogincheck,name="userlogincheck"),
    url(r'^userregister/',userregister,name="userregister"),
    url(r'^viewuserdata/',viewuserdata,name="viewuserdata"),
    url(r'^activateuser/',activateuser,name="activateuser"),
    url(r'^reviewofbooks/',reviewofbooks,name="reviewofbooks"),
    url(r'^usersearchresult1/',usersearchresult1,name="usersearchresult1"),
    url(r'^search/',search,name="search"),
    url(r'^usersearchresult/',usersearchresult,name="usersearchresult"),
    url(r'^viewdetails/',viewdetails,name="viewdetails"),
    url(r'^svm/',svm,name="svm"),
    url(r'^navie/',navie,name="navie"),
    url(r'^adminpage/',adminpage,name="adminpage"),
    url(r'^userpage/',userpage,name="userpage"),
    url(r'^bookpage/',bookpage,name="bookpage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
