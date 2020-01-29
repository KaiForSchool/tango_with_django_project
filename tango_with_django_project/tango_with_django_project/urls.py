from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('', views.index, name='index'),
]
