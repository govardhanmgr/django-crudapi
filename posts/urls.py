from django.urls import path
from . import views



urlpatterns = [
    path("",views.PostListCreateView.as_view(),name="get products"),
    # path("<int:post_id>", views.PostReadUpdateDeleteView.as_view(), name="post_details"),
    path("<int:pk>", views.PostReadUpdateDeleteView.as_view(), name="post_details"),

    path("update/<int:post_id>",views.update_post, name="update_details"),
    path("delete/<int:post_id>", views.delete_post,name="delete_post")
]

