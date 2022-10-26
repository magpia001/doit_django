from django.urls import path
from .views import index, single_post_page

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', single_post_page, name='post_detail')
]
