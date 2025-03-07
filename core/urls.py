from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projetos/', views.projetos, name='projetos'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('miaudotefotos/', views.miaudotefotos, name='miaudotefotos'),
    path('contactsuccess', views.contato_sucesso, name='contactsuccess'),
    path('calendariofotos/', views.calendariofotos, name='calendariofotos'),
    path('personalfotos/', views.personalfotos, name='personalfotos'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
