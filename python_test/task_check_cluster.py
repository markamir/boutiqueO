# task1_check_cluster.py
from kubernetes import client, config

config.load_kube_config()
v1 = client.CoreV1Api()

print("➡️ API Kubernetes accessible.")

nodes = v1.list_node()
for node in nodes.items:
    for condition in node.status.conditions:
        if condition.type == "Ready" and condition.status == "True":
            print(f"✅ Node '{node.metadata.name}' is Ready.")
