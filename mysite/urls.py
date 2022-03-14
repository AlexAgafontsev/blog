from django.urls import path
<<<<<<< HEAD
from . import views
from django.urls import include


=======
from mysite import views
>>>>>>> origin/main




urlpatterns = [
    path('', views.index, name="home"),
    path('blog', views.blog, name="blog"),
<<<<<<< HEAD
    path('post/<int:pk>/', views.post_page, name="post_page"),
    path('all_users', views.all_users, name="all_users"),
    path('user/<int:pk>/', views.user_page, name="user_page"),
    path('profile', views.profile, name="profile")
=======
    path('post/<int:pk>/', views.post_page),
    path('author<int:pk>', views.author_page),
>>>>>>> origin/main
]

urlpatterns += [
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
urlpatterns +=[
    path('reg', views.registr, name ='reg')
]

<<<<<<< HEAD
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
=======

>>>>>>> origin/main

