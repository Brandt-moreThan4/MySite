
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('blog-external/', include('scrapey.urls', namespace='scrapey')),
    path('manage/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

