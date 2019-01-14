#from django.urls import path
from django.conf.urls import include,url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^hello-view/', views.my_first_API.as_view())
	#path('admin/', admin.site.urls)

    ]
