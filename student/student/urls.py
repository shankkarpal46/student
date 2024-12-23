"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from user import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-student/',views.StudentCreateView.as_view(),name="register-student"),
    path('register-user/',views.User_Register.as_view(),name="register-user"),
    path('display-student/',views.Student_ListView.as_view(),name="display-student"),
    path('update-student/<str:pk>',views.Student_UpdateView.as_view(),name= "update-student"),
    path('delete-student/<str:pk>',views.DeleteView.as_view(),name = "delete-student"),
    path('',views.User_Login.as_view(),name = "login"),
    path('logout/',views.User_Logout.as_view(),name = "logout"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)