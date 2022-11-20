from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Адміністрування Youtube clone"
admin.site.site_title = "Адміністрування Youtube clone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
