
# When Debug True
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # Include Url From Weblog app
    path('',include('weblog.urls')),

    # Summer note Editor
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)