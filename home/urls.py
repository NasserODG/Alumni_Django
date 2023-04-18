from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:publication_id>/comment', views.add_Comment, name='add_Comment'),
    path('detail/<int:publication_id>/', views.detail_pub, name='detail_pub')
]
