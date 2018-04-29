
# When Debug True
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # include Main App urls
    path('', include('app.urls')),

    # Include Url From Weblog app
    path('blog/',include('weblog.urls')),

    # Summer note Editor
    path('summernote/', include('django_summernote.urls')),


]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     import debug_toolbar

     urlpatterns = [
                       re_path(r'^__debug__/', include(debug_toolbar.urls)),
                   ] + urlpatterns