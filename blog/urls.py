from django.urls import path
from blog.views import HomePageView, BlogPageView, PostPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<int:id>/", PostPageView.as_view(), name="post")
]
