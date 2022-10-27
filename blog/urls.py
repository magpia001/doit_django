from django.urls import path
# from .views import index, single_post_page
from .views import PostList, PostDetail

urlpatterns = [
    # path('', index, name='index'),  # FBV 방식의 call
    path('', PostList.as_view(), name='post_list'),  # CBV 방식의 call

    # path('<int:pk>/', single_post_page, name='post_detail')
    path('<int:pk>/', PostDetail.as_view(), name='post_detail')
]
