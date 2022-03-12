from django.urls import path
from mysite import views




urlpatterns = [
    path('', views.index, name="home"),
    path('blog', views.blog, name="blog"),
    path('post/<int:pk>/', views.post_page),
    path('author<int:pk>', views.author_page),
]

urlpatterns += [
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
urlpatterns +=[
    path('reg', views.registr, name ='reg')
]



