from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from .views import PostListView , PostDetailView

urlpatterns = [
    # Post List View
    path('',PostListView.as_view(), name='post-list'),

    # Post Detail View
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail')
]



#
# if settings.DEBUG==False:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
# if settings.DEBUG==True:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]