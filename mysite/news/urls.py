from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.HomeNews.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', views.ViewNews.as_view(), name='view_news'),
    path('news/add-news/', views.AddNews.as_view(), name='add_news'),
]
