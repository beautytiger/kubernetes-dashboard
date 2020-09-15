from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='cluster_index'),
    path('pods/', views.list_pods, name='list_pods'),
    path('nodes/', views.list_nodes, name='list_nodes'),
    path('namespaces/', views.list_namespace, name='list_namespaces'),
    path('events/', views.list_events, name='list_events'),
    path('pv/', views.list_persistent_volume, name='list_pv'),
]
