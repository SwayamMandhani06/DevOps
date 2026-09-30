# DevOps Assignment 8 — Kubernetes Resource Management & Ansible Configuration Management

## Student Details
- **Name:** Swayam Mandhani
- **PRN / Roll No.:** 123B1B184
- **Class:** B.Tech Computer Engineering
- **Division / Batch:** C / C2
- **Subject:** DevOps (BCE27PE01)
- **Assignment:** 8
- **Report Document:** [123B1B184_Assignment_8_DevOps.pdf](Report/123B1B184_Assignment_8_DevOps.pdf)

---

## Title
**Comprehensive Kubernetes Workload Management and Automated Configuration Management using Ansible**

## Aim
To study and practically implement advanced Kubernetes workload and resource primitives—including Namespaces, Pods, Deployments, Service types (ClusterIP, NodePort, LoadBalancer, ExternalName), ConfigMaps, Secrets, and Persistent Volumes/Claims—and to demonstrate automated configuration management using Ansible to provision, configure, and maintain NGINX web servers on multiple Linux managed nodes with verified idempotency.

## Objectives
1. **Kubernetes Cluster & Namespace Isolation**: Provision and manage isolated environments in a local Kubernetes cluster using namespaces.
2. **Workload Lifecycle Management**: Deploy and scale containerized application workloads using standalone Pods and declarative Deployments.
3. **Service Discovery & Networking**: Configure and compare four Kubernetes Service types: ClusterIP, NodePort, LoadBalancer, and ExternalName.
4. **Configuration & Secret Decoupling**: Separate non-confidential configuration (ConfigMaps) and sensitive credentials (Secrets) from application code.
5. **Stateful Storage Persistence**: Configure persistent volumes (PV) and volume claims (PVC) with host path storage.
6. **Ansible Control & Managed Node Architecture**: Set up an Ansible control node in WSL2 Ubuntu and containerized managed nodes (Server-1 and Server-2) via Docker.
7. **Inventory Management & Ad-hoc Commands**: Organize managed hosts using INI inventory and execute connectivity checks via SSH.
8. **Automated Playbook Execution & Idempotency**: Author, validate, and execute an Ansible playbook to install NGINX, start services, and deploy a custom web page, verifying idempotency on repeated execution.

---

## Tools & Environment

| Component | Tool / Technology | Version / Details | Purpose |
|---|---|---|---|
| **Container Runtime** | Docker Desktop | v29.x (Windows 11) | Hosts local Kubernetes and Ansible managed containers |
| **Orchestration** | Kubernetes | v1.30+ (`desktop-control-plane`) | Container orchestration engine |
| **Cluster CLI** | `kubectl` | Client v1.30+ | Cluster management and manifest application |
| **Control Node OS** | WSL2 Ubuntu | Ubuntu 24.04 LTS (Kernel 6.x) | Ansible Control Node execution environment |
| **Automation Engine** | Ansible Core | v2.20.1 | Agentless configuration management engine |
| **Runtime Language** | Python | 3.12 / 3.14 (WSL & nodes) | Ansible runtime dependency |
| **Remote Access** | OpenSSH | OpenSSH Server & Client | Secure remote shell communication |
| **Web Server** | NGINX | `nginx:latest` / Ubuntu APT package | Application workload for K8s and Ansible nodes |

---

## Architecture & Workflows

### 1. Kubernetes Architecture (Part A)
```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Kubernetes Cluster (Docker Desktop)                  │
│                     Namespace: assignment8                             │
│                                                                        │
│  ┌───────────────────────┐             ┌────────────────────────────┐  │
│  │   ConfigMap           │             │   Secret                   │  │
│  │   (app-config)        │             │   (db-secret)              │  │
│  └───────────────────────┘             └────────────────────────────┘  │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │   Persistent Volume (assignment8-pv) [1Gi, RWO, Retain]          │  │
│  │             ▲                                                    │  │
│  │             │ Bound                                              │  │
│  │   Persistent Volume Claim (assignment8-pvc) [1Gi, RWO]           │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌───────────────────────┐             ┌────────────────────────────┐  │
│  │   Standalone Pod      │             │   Deployment (3 Replicas)  │  │
│  │   (nginx-pod)         │             │   (nginx-deployment)       │  │
│  └───────────────────────┘             └─────────────┬──────────────┘  │
│                                                      │                 │
│         ┌────────────────────────────────────────────┴───────────┐     │
│         ▼                             ▼                          ▼     │
│  ┌──────────────┐              ┌──────────────┐           ┌──────────┐ │
│  │ nginx-pod-1  │              │ nginx-pod-2  │           │nginx-pod3│ │
│  └──────┬───────┘              └──────┬───────┘           └────┬─────┘ │
│         │                             │                        │       │
│         └─────────────────────────────┼────────────────────────┘       │
│                                       ▼                                │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                         Service Types                            │  │
│  │  1. NodePort:     nginx-nodeport      (Port: 80 -> NodePort:31678)│  │
│  │  2. ClusterIP:    nginx-clusterip     (Cluster-internal: 10.96.x)│  │
│  │  3. LoadBalancer: nginx-loadbalancer  (External IP / Ingress)    │  │
│  │  4. ExternalName: external-service    (CNAME -> example.com)     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### 2. Ansible Configuration Management Architecture (Part B)
```text
┌────────────────────────────────────────────────────────────────────────┐
│                   WSL2 Ubuntu (Ansible Control Node)                   │
│         - Ansible Core v2.20.1 | Python 3.12+ | OpenSSH Client         │
│         - Inventory: inventory.ini ([webservers])                      │
│         - Playbook: install-nginx.yml                                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                         SSH Communication over Port Forwarding
                                    │
              ┌─────────────────────┴─────────────────────┐
              │ SSH Port: 2221                            │ SSH Port: 2222
              ▼                                           ▼
┌───────────────────────────┐               ┌───────────────────────────┐
│ Server-1 (Managed Node)   │               │ Server-2 (Managed Node)   │
│ - Docker Container        │               │ - Docker Container        │
│   (assignment8-server1)   │               │   (assignment8-server2)   │
│ - Ubuntu 24.04 Base       │               │ - Ubuntu 24.04 Base       │
│ - OpenSSH Server          │               │ - OpenSSH Server          │
│ - NGINX & curl Installed  │               │ - NGINX & curl Installed  │
│ - Custom index.html       │               │ - Custom index.html       │
└───────────────────────────┘               └───────────────────────────┘
```

---

## Project Structure

```text
Assignment-8/
├── .gitignore                                   # Ignore rules for Ansible & Kubernetes artifacts
├── README.md                                    # Main Assignment 8 documentation (this file)
├── Report/                                      # Academic laboratory submission
│   └── 123B1B184_Assignment_8_DevOps.pdf
├── Screenshots/                                 # 21 practical verification screenshots
│   ├── 1-kubernetes-cluster-verification.png
│   ├── 2-namespace-created.png
│   ├── 3-pod-created.png
│   ├── 4-deployment-created.png
│   ├── 5-nodeport-service.png
│   ├── 6-nginx-service-verification.png
│   ├── 7-configmap-created.png
│   ├── 8-secret-created.png
│   ├── 9-persistent-volume-and-claim.png
│   ├── 10-kubernetes-service-types.png
│   ├── 11-ansible-control-node.png
│   ├── 12-ansible-version.png
│   ├── 13-ansible-managed-servers.png
│   ├── 14-ansible-inventory.png
│   ├── 15-ansible-ping-success.png
│   ├── 16-ansible-playbook-syntax-check.png
│   ├── 17-ansible-playbook-success.png
│   ├── 18-nginx-ansible-verification.png
│   ├── 19-nginx-process-verification.png
│   ├── 20-ansible-idempotency.png
│   └── 21-combined-devops-workflow.png
├── ansible/                                     # Ansible Configuration Management Case Study
│   ├── .gitignore                               # Ansible ignore rules (logs, retries, keys)
│   ├── Dockerfile                               # Ubuntu managed-node image definition
│   ├── README.md                                # Concise Ansible case study documentation
│   ├── install-nginx.yml                        # Automated NGINX deployment playbook
│   └── inventory.ini                            # Managed node connection inventory
└── kubernetes/                                  # Kubernetes Manifest Definitions
    ├── configmap.yaml                           # Non-sensitive configuration data
    ├── deployment.yaml                          # NGINX Deployment (3 replicas)
    ├── namespace.yaml                           # Custom namespace definition (assignment8)
    ├── nodeport-service.yaml                    # NodePort service definition
    ├── pod.yaml                                 # Standalone NGINX Pod manifest
    ├── pv-pvc.yaml                              # PersistentVolume and PersistentVolumeClaim
    ├── secret.yaml                              # Sensitive credential data (Opaque)
    └── service-types.yaml                       # ClusterIP, LoadBalancer, and ExternalName services
```

---

## Part A: Kubernetes Implementation & Resource Management

### 1. Namespace Creation (`namespace.yaml`)
Provides logical boundary isolation to separate Assignment 8 workloads from other cluster resources:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: assignment8
```
- **Execution**: `kubectl apply -f namespace.yaml`
- **Verification**: `kubectl get namespaces` confirms `assignment8` active.

### 2. Standalone Pod (`pod.yaml`)
Deploys a basic atomic compute unit running an NGINX container:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: assignment8
  labels:
    app: nginx-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```
- **Execution**: `kubectl apply -f pod.yaml`
- **Verification**: `kubectl get pods -n assignment8 -o wide` confirms status `Running`, `1/1 Ready` on `desktop-control-plane`.

### 3. Declarative Deployment (`deployment.yaml`)
Manages a scalable ReplicaSet of 3 NGINX pods ensuring desired state and self-healing:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: assignment8
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```
- **Execution**: `kubectl apply -f deployment.yaml`
- **Verification**: `kubectl get deployments -n assignment8` displays `3/3 Ready`, `3 Up-to-date`, `3 Available`.

### 4. NodePort Service (`nodeport-service.yaml`)
Exposes the NGINX deployment externally on each node’s IP at a static port:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
  namespace: assignment8
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```
- **Execution**: `kubectl apply -f nodeport-service.yaml`
- **Verification**: `kubectl get service -n assignment8` displays port mapping `80:31678/TCP`.

### 5. ConfigMap & Secret Management
Decouples configuration parameters and credentials from container images:
- **`configmap.yaml`**: Injects environment variables (`APP_ENV=production`, `APP_NAME=Assignment8-Nginx`).
- **`secret.yaml`**: Injects sensitive database credentials (`username=admin`, `password=admin123`) using an `Opaque` secret type.
- **Verification**:
  ```powershell
  kubectl describe configmap app-config -n assignment8
  kubectl get secrets -n assignment8
  ```

### 6. Persistent Storage (`pv-pvc.yaml`)
Implements persistent cluster storage that survives pod recreation:
- **PersistentVolume (`assignment8-pv`)**: 1Gi capacity, `ReadWriteOnce` access mode, `Retain` reclaim policy, backed by host path `/tmp/assignment8-data`.
- **PersistentVolumeClaim (`assignment8-pvc`)**: Requests 1Gi storage in `assignment8` namespace.
- **Verification**: `kubectl get pv` and `kubectl get pvc -n assignment8` confirm status `Bound`.

### 7. Kubernetes Service Types Comparison (`service-types.yaml`)
Demonstrates and deploys all four primary Kubernetes service types in the same namespace:
1. **ClusterIP (`nginx-clusterip`)**: Default internal IP accessible only from within the cluster.
2. **NodePort (`nginx-nodeport`)**: Exposes service on a static high port (`30000-32767`) across all cluster nodes.
3. **LoadBalancer (`nginx-loadbalancer`)**: Exposes the service externally using cloud/local load balancing.
4. **ExternalName (`external-service`)**: Maps the internal service name to an external DNS CNAME (`example.com`).
- **Verification**: `kubectl get services -n assignment8` lists all service types concurrently.

---

## Part B: Ansible Automated Configuration Management

### 1. Control Node & Managed Node Infrastructure
- **Ansible Control Node**: Configured inside **WSL2 Ubuntu 24.04 LTS** with `ansible-core 2.20.1` and `python3.12`.
- **Docker-based Managed Nodes**: Custom image built using [`ansible/Dockerfile`](./ansible/Dockerfile):
  ```powershell
  # Build managed node image
  docker build -t assignment8-ansible-node .

  # Launch Server-1 (SSH port 2221)
  docker run -d --name assignment8-server1 -p 127.0.0.1:2221:22 assignment8-ansible-node

  # Launch Server-2 (SSH port 2222)
  docker run -d --name assignment8-server2 -p 127.0.0.1:2222:22 assignment8-ansible-node
  ```

### 2. Inventory Configuration (`inventory.ini`)
Defines managed nodes and connection parameters without hardcoding credentials:
```ini
[webservers]
server-1 ansible_host=127.0.0.1 ansible_port=2221 ansible_user=ansible
server-2 ansible_host=127.0.0.1 ansible_port=2222 ansible_user=ansible
```
- **Graph Verification**: `ansible-inventory -i inventory.ini --graph`
- **Connectivity Check**: `ansible all -i inventory.ini -m ping -k` (Confirmed `ping => pong` for both nodes).

### 3. Automated NGINX Playbook (`install-nginx.yml`)
Declarative configuration management playbook executing the following tasks with privilege escalation (`become: yes`):
```yaml
---
- name: Configure Web Servers
  hosts: webservers
  become: yes

  tasks:
    - name: Install Nginx and curl
      ansible.builtin.apt:
        name:
          - nginx
          - curl
        state: present
        update_cache: yes

    - name: Start and enable Nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: yes

    - name: Deploy custom web page
      ansible.builtin.copy:
        content: |
          <html>
          <head>
            <title>Ansible Assignment 8</title>
          </head>
          <body>
            <h1>Web Server Configured Using Ansible</h1>
            <p>Server configured automatically using Ansible.</p>
          </body>
          </html>
        dest: /var/www/html/index.html
        mode: '0644'
```

### 4. Playbook Execution, Verification & Idempotency
1. **Pre-flight Syntax Check**:
   ```bash
   ansible-playbook -i inventory.ini install-nginx.yml --syntax-check
   ```
2. **Initial Playbook Run**:
   ```bash
   ansible-playbook -i inventory.ini install-nginx.yml -k
   ```
   *Execution Result*: `server-1: ok=4 changed=2`, `server-2: ok=4 changed=2` (NGINX started, custom webpage deployed).
3. **HTTP Content Verification**:
   ```bash
   ansible server-1 -i inventory.ini -m shell -a "curl -s http://localhost" -k
   ansible server-2 -i inventory.ini -m shell -a "curl -s http://localhost" -k
   ```
   *Result*: Both servers successfully returned the custom HTML content.
4. **Process State Verification**:
   ```bash
   ansible webservers -i inventory.ini -m shell -a "pgrep -a nginx" -k
   ```
   *Result*: Active NGINX master and worker processes confirmed on both servers.
5. **Idempotency Demonstration**:
   ```bash
   ansible-playbook -i inventory.ini install-nginx.yml -k
   ```
   *Idempotency Result*: `server-1: ok=4 changed=0`, `server-2: ok=4 changed=0`. No state changes occurred because the system was already in the desired configuration.

---

## Screenshot Evidence

| Figure | Screenshot | Technical Verification Description |
|:---:|---|---|
| **Figure 1** | [`1-kubernetes-cluster-verification.png`](Screenshots/1-kubernetes-cluster-verification.png) | Verification of `docker-desktop` context, cluster control-plane status, and system pods |
| **Figure 2** | [`2-namespace-created.png`](Screenshots/2-namespace-created.png) | Namespace `assignment8` creation and verification via `kubectl get namespaces` |
| **Figure 3** | [`3-pod-created.png`](Screenshots/3-pod-created.png) | Standalone NGINX Pod creation and status inspection in `assignment8` namespace |
| **Figure 4** | [`4-deployment-created.png`](Screenshots/4-deployment-created.png) | NGINX Deployment provisioning with 3 active replicas (`3/3 AVAILABLE`) |
| **Figure 5** | [`5-nodeport-service.png`](Screenshots/5-nodeport-service.png) | NodePort service creation with port mapping `80:31678/TCP` |
| **Figure 6** | [`6-nginx-service-verification.png`](Screenshots/6-nginx-service-verification.png) | Web browser verification of live NGINX server output on `http://localhost:8082` |
| **Figure 7** | [`7-configmap-created.png`](Screenshots/7-configmap-created.png) | ConfigMap `app-config` creation and data inspection (`APP_ENV`, `APP_NAME`) |
| **Figure 8** | [`8-secret-created.png`](Screenshots/8-secret-created.png) | Sensitive `Opaque` Secret `db-secret` creation and listing |
| **Figure 9** | [`9-persistent-volume-and-claim.png`](Screenshots/9-persistent-volume-and-claim.png) | PersistentVolume and PersistentVolumeClaim creation and `Bound` status check |
| **Figure 10** | [`10-kubernetes-service-types.png`](Screenshots/10-kubernetes-service-types.png) | Concurrent verification of ClusterIP, NodePort, LoadBalancer, and ExternalName services |
| **Figure 11** | [`11-ansible-control-node.png`](Screenshots/11-ansible-control-node.png) | WSL2 Ubuntu control node verification, Linux kernel release, and package update |
| **Figure 12** | [`12-ansible-version.png`](Screenshots/12-ansible-version.png) | Ansible Core version verification (`v2.20.1`) and CLI inventory utilities |
| **Figure 13** | [`13-ansible-managed-servers.png`](Screenshots/13-ansible-managed-servers.png) | Docker container execution of Server-1 and Server-2 with forwarded SSH ports |
| **Figure 14** | [`14-ansible-inventory.png`](Screenshots/14-ansible-inventory.png) | Inventory configuration (`inventory.ini`) and hierarchical graph inspection |
| **Figure 15** | [`15-ansible-ping-success.png`](Screenshots/15-ansible-ping-success.png) | Successful SSH connectivity ping (`ping => pong`) to both managed nodes |
| **Figure 16** | [`16-ansible-playbook-syntax-check.png`](Screenshots/16-ansible-playbook-syntax-check.png) | Pre-flight YAML and module syntax validation of `install-nginx.yml` |
| **Figure 17** | [`17-ansible-playbook-success.png`](Screenshots/17-ansible-playbook-success.png) | Initial playbook run completing all 4 tasks across both managed nodes |
| **Figure 18** | [`18-nginx-ansible-verification.png`](Screenshots/18-nginx-ansible-verification.png) | Content verification via ad-hoc curl returning deployed custom HTML page |
| **Figure 19** | [`19-nginx-process-verification.png`](Screenshots/19-nginx-process-verification.png) | Process verification via `pgrep -a nginx` confirming active master/worker processes |
| **Figure 20** | [`20-ansible-idempotency.png`](Screenshots/20-ansible-idempotency.png) | Second playbook execution demonstrating idempotency (`changed=0` on both hosts) |
| **Figure 21** | [`21-combined-devops-workflow.png`](Screenshots/21-combined-devops-workflow.png) | Complete end-to-end DevOps workflow architecture from Code to K8s and Ansible |

---

## Requirement Coverage Summary

| Curriculum Requirement | Demonstrated In | Technical Evidence |
|---|---|---|
| **Kubernetes Namespace Isolation** | Part A | `namespace.yaml`, Figure 2 |
| **Kubernetes Pod Workload** | Part A | `pod.yaml`, Figure 3 |
| **Kubernetes Deployment & Scaling** | Part A | `deployment.yaml` (3 replicas), Figure 4 |
| **Kubernetes Service Types (All 4)** | Part A | `nodeport-service.yaml`, `service-types.yaml`, Figures 5 & 10 |
| **External Service Access** | Part A | NodePort `31678`, Figure 6 |
| **Decoupled Application Config** | Part A | `configmap.yaml`, Figure 7 |
| **Sensitive Data Management** | Part A | `secret.yaml`, Figure 8 |
| **Stateful Persistent Storage** | Part A | `pv-pvc.yaml` (PV & PVC Bound), Figure 9 |
| **Ansible Control Node Setup** | Part B | WSL2 Ubuntu 24.04, Figures 11 & 12 |
| **Managed Node Provisioning** | Part B | Dockerfile, `assignment8-server1/2`, Figure 13 |
| **Host Inventory Management** | Part B | `inventory.ini`, Figure 14 |
| **Agentless SSH Connectivity** | Part B | `ansible -m ping`, Figure 15 |
| **Automated Playbook Configuration** | Part B | `install-nginx.yml`, Figures 16 & 17 |
| **Service & Process Verification** | Part B | Ad-hoc `curl` & `pgrep`, Figures 18 & 19 |
| **Playbook Idempotency** | Part B | Repeated execution (`changed=0`), Figure 20 |
| **End-to-End DevOps Architecture** | Architecture | Complete Pipeline Workflow, Figure 21 |

---

## Resource Decommissioning & Cleanup Steps

To maintain clean system hygiene, all practical resources can be torn down using the following commands:

### 1. Kubernetes Workload Teardown
```powershell
cd "d:\Projects\DevOps Github\Assignment-8\kubernetes"

# Delete all resources by deleting the isolated namespace
kubectl delete namespace assignment8

# Delete cluster-level PersistentVolume
kubectl delete pv assignment8-pv

# Verify teardown
kubectl get namespaces
kubectl get pv
```

### 2. Ansible Container & Image Teardown
```powershell
# Stop and remove managed node containers
docker stop assignment8-server1 assignment8-server2
docker rm assignment8-server1 assignment8-server2

# Remove custom node Docker image
docker rmi assignment8-ansible-node

# Verify Docker container cleanup
docker ps -a
```

---

## Learning Outcomes
1. **Kubernetes Workload & Cluster Management**: Mastered declarative resource management across namespaces, scalable deployments, and standalone pods.
2. **Service Discovery & Exposure Strategies**: Gained clear architectural understanding of ClusterIP (internal), NodePort (static port), LoadBalancer (external gateway), and ExternalName (DNS aliasing).
3. **Config & Secret Decoupling**: Implemented twelve-factor app principles by decoupling configurations and secrets from container image builds.
4. **Kubernetes Storage Lifecycle**: Learned the relationship between storage volumes, PersistentVolumes, and claims, ensuring state persistence across pod lifecycles.
5. **Ansible Architecture & Automation**: Understood agentless architecture over SSH, inventory categorization, and ad-hoc module execution.
6. **Infrastructure as Code & Idempotency**: Mastered writing Ansible playbooks that produce identical, predictable system states regardless of how many times they are executed.
7. **Cross-Platform DevOps Integration**: Integrated Windows, WSL2 Ubuntu, Docker containers, and Kubernetes into a cohesive local engineering pipeline.

---

## Submission Details
- **GitHub Repository:** [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-8](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-8)
- **Academic Report:** [`Report/123B1B184_Assignment_8_DevOps.pdf`](Report/123B1B184_Assignment_8_DevOps.pdf)
- **Hosted / Output:** N/A — Local Kubernetes cluster and containerized Ansible environment.
