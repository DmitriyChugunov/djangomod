from django.urls import path

from .views import shop, myForm, NewsView, ProductView, PostsView, DownloadView

urlpatterns = [
    path('', shop),
    path('appointment', myForm),
    path('news', NewsView),
    path('dilivery', ProductView),
    path('posts/all', PostsView),
    path('download', DownloadView),
]