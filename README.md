# k8s-nfs-setup

Hello Team, with this repository we will be able to build a 3 node kubernetes cluster
that incorporates the Kubernetes Networking Model using Flannel and NFS to easily create Kubernetes Persistent Volumes, additionally
Grafana and Prometheus are installed for resource usage monitoring.

The shared folder is /root/shared

Assumptions are:

* 3 xl170 bare metal machines using the emulab-ops/UBUNTU18-64-OSCN-R image from CloudLab.

* The installation is being run as root.

* The master node can ssh into the worker nodes.

* The workers file has been modified with the IPv4 Addresses of your current worker nodes.

* The master file has been modified with the IPv4 Address of your current master node.

* Permissions on the install.sh file are modified to allow it to be executed.
    
Other than that, just running the install.sh file on your master node should get everything working

As stated in https://github.com/zsl3203/summer/blob/master/prometheus%20%2B%20grafana%20for%20k8s.md
After the installation is complete, to finish the setup of grafana follow these steps:

1- Run this command:
    
    kubectl get svc -n kube-system
    
    
   To get the port being used by grafana, then on your browser connect to that port on your master node
   For instance: 123.123.123.123:30123
   
2- Add a data source like this:

    Type: Prometheus
    
    Url: http://prometheus:9090
    
    Access: proxy
    
3- Import this dashboard:

    https:///dashboards/315


As note, the profile used to build this installation is called clusterTest6 and is available at CloudLab.
