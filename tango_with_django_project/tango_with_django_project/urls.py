from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('', views.index, name='index'),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
