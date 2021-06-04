from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls'))
]