from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, DetailView
from WeNews.models import Articles
from . import views

urlpatterns = [	
    path("", ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], 
    template_name = "WeNews/index.html")),
    url("(?P<pk>\d+)", DetailView.as_view(model=Articles, 
    template_name = "WeNews/post.html"))
]