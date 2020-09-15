from django.urls import path

from . import views


urlpatterns = [
    path('<str:namespace>/', views.index, name='namespace_index'),
    path('<str:namespace>/deploments', views.list_deployments, name='deployments'),
    path('<str:namespace>/statefulsets', views.list_statefulsets, name='statefulsets'),
    path('<str:namespace>/configmaps', views.list_configmaps, name='configmaps'),
    path('<str:namespace>/secrets', views.list_secrets, name='secrets'),
    path('<str:namespace>/pvcs', views.list_pvcs, name='pvcs'),
    path('<str:namespace>/daemonsets', views.list_daemonsets, name='daemonsets'),
    path('<str:namespace>/ingresses', views.list_ingresses, name='ingresses'),
    path('<str:namespace>/replicasets', views.list_replicasets, name='replicasets'),
    path('<str:namespace>/pods', views.list_pods, name='pods'),
    path('<str:namespace>/events', views.list_events, name='events'),
]
