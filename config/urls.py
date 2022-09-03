from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('services.urls')),
    path("users/", include('users.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
