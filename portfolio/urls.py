from django.contrib import admin
from django.urls import path, include
from core.views import projetos
from core.views import contact
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projetos/', projetos, name='projetos'),
    path('contact/', contact, name='contact'),
    path('', home, name='home'),  # Incluindo as URLs do app core
]