
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

namespace = "test-auto"
pods = v1.list_namespaced_pod(namespace=namespace)

for pod in pods.items:
    if "nginx" in pod.metadata.name:
        print(f"➡️ Pod: {pod.metadata.name} | Status: {pod.status.phase}")
        if pod.status.phase == "Running":
            print("nginx Pod is Running.")
