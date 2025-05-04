import subprocess

def run_command(command, shell=True):
    print(f"\n>>> Running: {command}")
    process = subprocess.run(command, shell=shell)
    if process.returncode != 0:
        print(f"❌ Command failed: {command}")
        exit(process.returncode)
    print("✅ Done")

commands = [
    "minikube start --driver=kvm2 --memory=8192 --cpus=4",
    "cd /mnt/c/programs/suu/SUU-Project",
    "kubectl apply -f templates/release/kubernetes/manifests.yaml",
    "px deploy --check=false",
    "kubectl apply -f collector.yaml",
    "kubectl create namespace monitoring",
    "helm upgrade --install grafana grafana/grafana -f grafana-values.yaml -n monitoring",
    "kubectl apply -f prometheus.yaml -n monitoring",
]

for cmd in commands:
    run_command(cmd)
