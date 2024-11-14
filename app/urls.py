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
from accounts.views import login_view, AplicationView, logout_view, DetailProfileView, DetailFeriasView, DetailFolgasView,CreateView, UpdateProfileView, teste
from aplication.views import EditSolicitacao


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout' ),

    path('profile/<int:pk>/', DetailProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', UpdateProfileView.as_view(), name='edit-profile'),
    path('profile/create/', CreateView.as_view(), name='create'),
    
    path('aplication/', AplicationView.as_view(), name='aplication' ),


    path('folgas/<int:pk>/', DetailFolgasView.as_view(), name='rest'),
    #gestor
    path('solicitacao/', EditSolicitacao.as_view(), name='editsolicitacao'),
    
    path('ferias/<int:pk>/', DetailFeriasView.as_view(), name='vacation'),


    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
