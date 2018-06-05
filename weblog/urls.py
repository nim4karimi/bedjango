from django.urls import path, re_path


from .views import PostListView , PostDetailView

urlpatterns = [
    # Post List View
    path('',PostListView.as_view(), name='post-list'),

    # Post Detail View
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail')
]

