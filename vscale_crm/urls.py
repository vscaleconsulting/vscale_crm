"""vscale_crm URL Configuration

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
from leads.views import LandingPageView, UserCreateView, ContactListView, ContactView, CreateContactView, ContactDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='home-page'),
    path('contacts/add', CreateContactView.as_view(), name='contact-create'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('admin/', admin.site.urls),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<pk>', ContactView.as_view(), name='contact-info'),
    path('contacts/<pk>/delete', ContactDeleteView.as_view(), name='contact-delete'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name='logout-page'),
]
