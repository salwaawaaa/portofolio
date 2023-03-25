from django.urls import path 
from. import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('posts/', views.Posts, name="posts"),
    path('post/<str:pk>/', views.Post, name="Post"),
    path('profile/', views.Profile, name="profile"),

    #crud path
    path('create_Post/', views.createPost,name="create_Post"),
    path('update_Post/<str:pk>/', views.updatePost,name="update_Post"),
    path('delete_Post/<str:pk>/', views.deletePost,name="deletete_Post"),
]