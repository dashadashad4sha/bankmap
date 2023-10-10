from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('banks.urls')),
]

urlpatterns += doc_urls

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
