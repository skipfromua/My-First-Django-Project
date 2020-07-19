from django.urls import path
from .views import MainView, NewsView, commentary_view


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/page/<int:page_number>', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', commentary_view, name='post_detail'),
]
