from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

namespace = "test-auto"
pod_name = "nginx-test"

v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
print(f" Pod '{pod_name}' deleted from namespace '{namespace}'.")
