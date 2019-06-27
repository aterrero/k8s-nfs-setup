import os
import sys

os.system("git clone https://github.com/redhatxl/k8s-prometheus-grafana.git")
os.system("docker pull prom/node-exporter")
os.system("docker pull prom/prometheus:v2.0.0")
os.system("docker pull grafana/grafana:4.2.0")

if sys.argv[1] ==  "master":
    os.system("kubectl create -f k8s-prometheus-grafana/node-exporter.yaml")
    os.system("kubectl create -f k8s-prometheus-grafana/prometheus/rbac-setup.yaml")
    os.system("kubectl create -f k8s-prometheus-grafana/prometheus/configmap.yaml")
    os.system("kubectl create -f k8s-prometheus-grafana/prometheus/prometheus.deploy.yml")
    os.system("kubectl create -f k8s-prometheus-grafana/prometheus/prometheus.svc.yml")
    os.system("kubectl create -f k8s-prometheus-grafana/grafana/grafana-deploy.yaml")
    os.system("kubectl create -f k8s-prometheus-grafana/grafana/grafana-svc.yaml")
    os.system("kubectl create -f k8s-prometheus-grafana/grafana/grafana-ing.yaml")
