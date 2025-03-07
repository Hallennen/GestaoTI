"""
URL configuration for app project.

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
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import login_view, AplicationView, logout_view, DetailProfileView, DetailFeriasView, DetailFolgasView,CreateView, UpdateProfileView,recuperacao_senha, CreateProfile
from aplication.views import ViewSolicitacao, EditSolicitacao, ViewGeral, ViewRouter, VacationView, DeleteFeriasView, ListProfile


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout' ),
    path('reset/', recuperacao_senha, name='recuperacao_senha' ),

    #user default
    path('profile/<int:pk>/', DetailProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', UpdateProfileView.as_view(), name='edit-profile'),    
    path('aplication/', AplicationView.as_view(), name='aplication' ),
    path('folgas/<int:pk>/', DetailFolgasView.as_view(), name='rest'),
    path('ferias/<int:pk>/', DetailFeriasView.as_view(), name='vacation'),



    #gestor
    path('listprofile/',ListProfile.as_view(), name='listprofile'),
    path('createprofile/',CreateProfile.as_view(), name='createprofile'),
    path('solicitacao/',ViewSolicitacao.as_view(), name='viewsolicitacao'),
    path('solicitacao/<int:pk>', EditSolicitacao.as_view(), name='editsolicitacao'),
    path('visaogeral/', ViewGeral.as_view(), name='viewgeral'),
    path('ferias/', VacationView.as_view(), name='vacation_list'),
    path('ferias/<int:pk>/delete/', DeleteFeriasView, name='excluirvacation'),
    
    

    ## VOLANTE / GESTOR
    path('roteiro/', ViewRouter.as_view(), name='router'),





    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
