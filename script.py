import subprocess

def run_command(command, shell=True, capture_output=False):
    print(f"\n>>> Running: {command}")
    process = subprocess.run(command, shell=shell, capture_output=capture_output, text=True)
    if process.returncode != 0:
        print(f"❌ Command failed: {command}")
        if capture_output:
            print(process.stderr)
        exit(process.returncode)
    if capture_output:
        return process.stdout.strip()
    print("✅ Done")
    return None

commands = [
    "minikube start --driver=kvm2 --memory=8192 --cpus=4",
    "cd /mnt/c/programs/suu/SUU-Project",
    "px deploy --check=false -y",
    "px demo deploy px-sock-shop -y",
    "kubectl create namespace monitoring",
    "helm upgrade --install grafana grafana/grafana -f grafana-values.yaml -n monitoring",
]

for cmd in commands:
    run_command(cmd)

print("\n🔍 Getting Grafana pod name:")
pod_name = run_command(
    'kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" '
    '-o jsonpath="{.items[0].metadata.name}"',
    capture_output=True
)
print(f"Grafana Pod Name: {pod_name}")

print("⏳ Waiting for Grafana pod to be ready...")
run_command(f"kubectl wait --for=condition=Ready pod/{pod_name} -n monitoring --timeout=120s")

print("\n🔐 Getting Grafana admin password:")
password = run_command(
    'kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode',
    capture_output=True
)
print(f"Admin password: {password}")

print("\n🚀 Forwarding port 3000 to Grafana pod (access at http://localhost:3000):")
run_command(f"kubectl --namespace monitoring port-forward {pod_name} 3000")



# grafana pixie url address work.getcosmic.ai:443