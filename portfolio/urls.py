from django.contrib import admin
from django.urls import path, include
from core.views import projetos
from core.views import contact
from core.views import home
from core.views import curriculo 
from core.views import miaudotefotos  
from core.views import contactsuccess
from core.views import calendariofotos
from core.views import personalfotos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projetos/', projetos, name='projetos'),
    path('contact/', contact, name='contact'),
    path('curriculo/', curriculo, name='curriculo'),
    path('', home, name='home'),
    path('miaudotefotos/', miaudotefotos, name='miaudotefotos'),
    path('contactsuccess', contactsuccess, name='contactsuccess'),
    path('calendariofotos/', calendariofotos, name='calendariofotos'),
    path('personalfotos/', personalfotos, name='personalfotos'),
        # Incluindo as URLs do app core
]