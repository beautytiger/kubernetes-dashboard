from django.shortcuts import render

from kubernetes import client

corev1 = client.CoreV1Api()
appv1 = client.AppsV1Api()
extv1 = client.ExtensionsV1beta1Api()


def index(request, namespace="default"):
    context = {
        "namespace": namespace,
    }
    return render(request, "namespaced.html", context)


def list_deployments(request, namespace="default"):
    deployments = appv1.list_namespaced_deployment(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "deployment 列表",
        "items": deployments.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_statefulsets(request, namespace="default"):
    statefulsets = appv1.list_namespaced_stateful_set(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "statefulset 列表",
        "items": statefulsets.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_configmaps(request, namespace="default"):
    configmaps = corev1.list_namespaced_config_map(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "configmap 列表",
        "items": configmaps.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_secrets(request, namespace="default"):
    secrets = corev1.list_namespaced_secret(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "secrets 列表",
        "items": secrets.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_pvcs(request, namespace="default"):
    pvcs = corev1.list_namespaced_persistent_volume_claim(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "pvc 列表",
        "items": pvcs.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_daemonsets(request, namespace="default"):
    daemonsets = extv1.list_namespaced_daemon_set(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "daemonset 列表",
        "items": daemonsets.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_ingresses(request, namespace="default"):
    ingresses = extv1.list_namespaced_ingress(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "ingress 列表",
        "items": ingresses.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_replicasets(request, namespace="default"):
    replicasets = extv1.list_namespaced_replica_set(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "ingress 列表",
        "items": replicasets.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_pods(request, namespace="default"):
    pods = corev1.list_namespaced_pod(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "pod 列表",
        "items": pods.items,
    }
    return render(request, "namespaced-objects.html", context)


def list_events(request, namespace="default"):
    events = corev1.list_namespaced_event(namespace=namespace)
    context = {
        "namespace": namespace,
        "title": "event 列表",
        "items": events.items,
    }
    return render(request, "namespaced-objects.html", context)
