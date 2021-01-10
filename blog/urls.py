from django.urls import path
from blog.views import blog, PostDetailView, searchBlog
urlpatterns = [
    path("", blog, name='blog'), 
    path("<slug>", PostDetailView.as_view(), name='post'),
    path("q/", searchBlog, name='search'),
]
