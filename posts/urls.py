from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPosts),
    path('api/show/all', views.showPostsApi),
    path('api/show/<int:id>', views.showPostApi)
    ]