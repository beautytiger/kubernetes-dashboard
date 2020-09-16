from django.shortcuts import render

from kubernetes import client


v1 = client.CoreV1Api()


def index(request):
    return render(request, "cluster.html")


def list_pods(request):
    pods = v1.list_pod_for_all_namespaces(async_req=False)
    context = {
        "title": "pod 列表",
        "items": pods.items,
    }
    return render(request, "namespaced-items.html", context)


def list_nodes(request):
    nodes = v1.list_node()
    context = {
        "title": "节点列表",
        "items": nodes.items,
    }
    return render(request, "cluster-items.html", context)


def list_namespace(request):
    namespaces = v1.list_namespace()
    context = {
        "title": "namespace 列表",
        "items": namespaces.items,
    }
    return render(request, "namespace.html", context)


def list_persistent_volume(request):
    pv = v1.list_persistent_volume()
    context = {
        "title": "pv 列表",
        "items": pv.items,
    }
    return render(request, "cluster-items.html", context)


def list_events(request):
    events = v1.list_event_for_all_namespaces()
    context = {
        "title": "events 列表",
        "items": events.items,
    }
    return render(request, "namespaced-items.html", context)



