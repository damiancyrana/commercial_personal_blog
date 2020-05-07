from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='table_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.specific_post, name='specific_post'),
]
