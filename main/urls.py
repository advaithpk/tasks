from django.urls import path
from . import views

urlpatterns = [
    path('newtask',views.newtask,name='newtask'),
    path('main', views.main, name='main'),
    path('pending', views.pending, name='pending'),
    path('completed', views.completed, name='completed'),
    path('update_or_delete_entry', views.update_or_delete_entry, name='update_or_delete_entry'),
    path('logout', views.logout, name = 'logout'),
]