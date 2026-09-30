# DevOps Assignment 7 — Kubernetes Application Deployment using Helm

## Student Details
- **Name:** Swayam Mandhani
- **PRN / Roll No.:** 123B1B184
- **Class:** B.Tech Computer Engineering
- **Division / Batch:** C / C2
- **Subject:** DevOps (BCE27PE01)
- **Assignment:** 7
- **Report Document:** [123B1B184_Assignment_7_DevOps.pdf](Report/123B1B184_Assignment_7_DevOps.pdf)

---

## Title
**Package and Deploy an Application on a Kubernetes Cluster using Helm Package Manager**

## Aim
To configure a local Kubernetes cluster using Docker Desktop, install and verify the Helm package manager, create and structure a custom Helm chart (`myapp`), package, lint, template, and deploy an NGINX web application to Kubernetes, verify deployed pods, services, and deployments, test application connectivity through port-forwarding, perform a rolling release upgrade (scaling replicas from 2 to 3), and execute clean resource decommissioning.

---

## Technologies & Tools Used
- **Kubernetes (K8s):** v1.30+ (Single-node local cluster orchestrated via Docker Desktop)
- **Helm:** v3.15+ (The Kubernetes Package Manager)
- **Docker Engine & Desktop:** v29.x (Container runtime and local Kubernetes host)
- **kubectl:** Kubernetes Command-Line Interface (`docker-desktop` context)
- **NGINX:** Official containerized web server (`nginx:latest`)
- **Shell / OS:** PowerShell 7 / Windows 11

---

## Kubernetes Cluster Architecture

The following diagram illustrates the single-node local Kubernetes cluster architecture managed by Docker Desktop and orchestrated via Helm:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Kubernetes Control Plane & Node                      │
│                    (Context: docker-desktop)                           │
│                                                                        │
│  ┌───────────────────────┐             ┌────────────────────────────┐  │
│  │   kube-apiserver      │◄────────────┤  Helm CLI & kubectl CLI    │  │
│  │  (Port :52653 / HTTPS)│             │ (PowerShell Admin Console) │  │
│  └──────────┬────────────┘             └────────────────────────────┘  │
│             │                                                          │
│      ┌──────┴──────┬──────────────┬──────────────┐                     │
│      ▼             ▼              ▼              ▼                     │
│  ┌───────┐   ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │ etcd  │   │ scheduler │  │controller-│  │  CoreDNS  │               │
│  │       │   │           │  │  manager  │  │           │               │
│  └───────┘   └───────────┘  └───────────┘  └───────────┘               │
│                                                                        │
│ ────────────────────────────────────────────────────────────────────── │
│                         Workload Namespace: default                    │
│                                                                        │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │               Service: myrelease-myapp                       │     │
│   │      Type: NodePort | ClusterIP: 10.96.74.255:80             │     │
│   │                 NodePort: 32353/TCP                          │     │
│   └──────────────────────────────┬───────────────────────────────┘     │
│                                  │                                     │
│             ┌────────────────────┼────────────────────┐                │
│             ▼                    ▼                    ▼                │
│      ┌─────────────┐      ┌─────────────┐      ┌─────────────┐         │
│      │ Pod 1       │      │ Pod 2       │      │ Pod 3       │         │
│      │ NGINX       │      │ NGINX       │      │ NGINX       │         │
│      │ (Port 80)   │      │ (Port 80)   │      │ (Port 80)   │         │
│      └─────────────┘      └─────────────┘      └─────────────┘         │
│       (Initial: 2)         (Initial: 2)         (Upgrade: 3)           │
│                                                                        │
│ ────────────────────────────────────────────────────────────────────── │
│   Port Forwarding: 127.0.0.1:8081  ──►  service/myrelease-myapp:80     │
│                    Browser Access: http://localhost:8081               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Project Structure

```text
Assignment-7/
├── .gitignore                                   # Helm package & Kubernetes ignore patterns
├── README.md                                    # Comprehensive assignment documentation
├── Report/                                      # Academic laboratory submission
│   └── 123B1B184_Assignment_7_DevOps.pdf
├── Screenshots/                                 # Verification screenshot evidence (16 figures)
│   ├── 1-kubernetes-tools-verification.png
│   ├── 2-kubernetes-cluster-info.png
│   ├── 3-kubernetes-nodes.png
│   ├── 4-kubernetes-architecture.png
│   ├── 5-helm-version.png
│   ├── 6-helm-chart-created.png
│   ├── 7-helm-chart-structure.png
│   ├── 8-helm-template-output.png
│   ├── 9-helm-install-success.png
│   ├── 10-kubernetes-pods-deployments-services.png
│   ├── 11-helm-list-and-status.png
│   ├── 12-kubernetes-port-forward-configuration.png
│   ├── 13-kubernetes-application-running.png
│   ├── 14-helm-upgrade.png
│   ├── 15-kubernetes-upgrade-verification.png
│   └── 16-helm-uninstall.png
└── myapp/                                       # Helm Chart Directory
    ├── .helmignore                              # Patterns to ignore when packaging chart
    ├── Chart.yaml                               # Chart metadata, API version, and release info
    ├── values.yaml                              # Default template values (replicas, image, service)
    ├── charts/                                  # Sub-charts and chart dependencies
    └── templates/                               # Kubernetes manifest templates
        ├── NOTES.txt                            # Post-installation notes and instructions
        ├── _helpers.tpl                         # Reusable Go template helper functions
        ├── deployment.yaml                      # Kubernetes Deployment specification
        ├── hpa.yaml                             # Horizontal Pod Autoscaler manifest
        ├── httproute.yaml                       # Gateway API HTTPRoute manifest
        ├── ingress.yaml                         # Ingress resource manifest
        ├── service.yaml                         # Kubernetes Service (NodePort) specification
        ├── serviceaccount.yaml                  # Kubernetes ServiceAccount manifest
        └── tests/                               # Integration test manifests
            └── test-connection.yaml
```

---

## Helm Chart Configuration

### 1. `Chart.yaml`
The chart metadata file defines the API version, chart name, type, and semantic versioning:

```yaml
apiVersion: v2
name: myapp
description: A Helm chart for Kubernetes
type: application
version: 0.1.0
appVersion: "1.16.0"
```

### 2. `values.yaml` (Key Configuration Sections)
The `values.yaml` file decouples environment-specific configuration parameters from the underlying Kubernetes manifest templates:

```yaml
# ReplicaSet scale count (initially 2, upgraded to 3)
replicaCount: 3

# Container image settings
image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "latest"

imagePullSecrets: []
nameOverride: ""
fullnameOverride: ""

# ServiceAccount configuration
serviceAccount:
  create: true
  automount: true
  annotations: {}
  name: ""

# Service definition for exposing NGINX
service:
  type: NodePort
  port: 80

# Ingress & Resource constraints
ingress:
  enabled: false

resources: {}
```

---

## Step-by-Step Implementation Procedure

### Step 1: Environment Setup & Prerequisites Verification
1. Enable the built-in Kubernetes cluster in Docker Desktop via **Settings → Kubernetes → Enable Kubernetes → Apply & restart**.
2. Open PowerShell as Administrator and verify installed tool versions and cluster control plane status:
   ```powershell
   # Verify Docker engine version
   docker --version

   # Verify kubectl CLI client version
   kubectl version --client

   # Verify current Kubernetes context
   kubectl config current-context

   # Verify cluster control plane endpoints
   kubectl cluster-info
   ```
3. Inspect active namespaces and verify single-node cluster readiness:
   ```powershell
   # List active cluster namespaces
   kubectl get namespaces

   # Verify control-plane node status
   kubectl get nodes
   ```
   *Verification Output:* The node `desktop-control-plane` is in the `Ready` state.

---

### Step 2: Helm Package Manager Installation & Verification
1. Verify the Helm CLI installation and client build version:
   ```powershell
   helm version
   ```
   *Verification Output:* Build info confirms Helm client `v3.15.0` with Go `1.22.x` and clean Git tree state.
2. Explore available Helm commands and operational environment variables:
   ```powershell
   helm help
   ```

---

### Step 3: Creating and Inspecting the `myapp` Helm Chart
1. Generate the standard chart skeleton structure using `helm create`:
   ```powershell
   cd "D:\Projects\DevOps Github\Assignment-7"
   helm create myapp
   ```
2. Verify the generated chart contents and directory tree:
   ```powershell
   Get-ChildItem .\myapp
   tree .\myapp /F
   ```
   The chart contains `Chart.yaml`, `values.yaml`, `.helmignore`, `charts/`, and `templates/` with `deployment.yaml`, `service.yaml`, `serviceaccount.yaml`, and helper templates.

---

### Step 4: Chart Linting & Manifest Templating
1. Validate the chart syntax and structure against Helm best practices:
   ```powershell
   helm lint .\myapp
   ```
   *Verification Output:* `1 chart(s) linted, 0 chart(s) failed`.
2. Render and inspect the generated Kubernetes YAML manifests without deploying them to the cluster:
   ```powershell
   helm template myapp .\myapp
   ```
   *Verification Output:* Outputs rendered YAML manifests for `ServiceAccount`, `Service` (`NodePort`, port 80), and `Deployment` (2 initial replicas of `nginx:latest`).

---

### Step 5: Application Deployment via Helm (`helm install`)
1. Deploy the release named `myrelease` into the `default` namespace:
   ```powershell
   helm install myrelease .\myapp
   ```
   *Verification Output:*
   ```text
   NAME: myrelease
   LAST DEPLOYED: Wed Sep 30 2026
   NAMESPACE: default
   STATUS: deployed
   REVISION: 1
   DESCRIPTION: Install complete
   ```
2. Verify deployed Kubernetes workloads:
   ```powershell
   # Verify running Pods
   kubectl get pods

   # Verify Deployment status
   kubectl get deployments

   # Verify NodePort Service configuration
   kubectl get services
   ```
   *Verification Output:*
   - Pods: 2 pods running with `1/1 Ready` status.
   - Deployment `myrelease-myapp`: `2/2 Ready`, `2 Up-to-date`, `2 Available`.
   - Service `myrelease-myapp`: `NodePort`, Cluster-IP `10.96.74.255`, Port mapping `80:32353/TCP`.
3. Inspect Helm release tracking and status:
   ```powershell
   helm list
   helm status myrelease
   ```

---

### Step 6: Application Access Verification (Port Forwarding)
1. Establish a local port-forwarding bridge from host port `8081` to the Kubernetes service port `80`:
   ```powershell
   kubectl port-forward service/myrelease-myapp 8081:80
   ```
   *Output:* `Forwarding from 127.0.0.1:8081 -> 80`.
2. Open a web browser and navigate to:
   ```text
   http://localhost:8081
   ```
3. *Verification Result:* The **"Welcome to nginx!"** landing page renders successfully, confirming operational connectivity through the Kubernetes Service to the backing NGINX container pods.

---

### Step 7: Rolling Release Upgrade (Scaling Replicas from 2 to 3)
1. Update `replicaCount: 3` in `myapp/values.yaml` (or pass dynamically via `--set replicaCount=3`).
2. Execute the release upgrade command:
   ```powershell
   helm upgrade myrelease .\myapp
   ```
   *Verification Output:* `Release "myrelease" has been upgraded. Happy Helming!`.
3. Verify the rolling deployment and updated replica scale:
   ```powershell
   kubectl get pods
   helm status myrelease
   ```
   *Verification Output:* 3 Pods are actively running in `1/1 Ready` state, and deployment reflects `3/3 AVAILABLE`.

---

### Step 8: Decommissioning & Cleanup Verification
1. Uninstall and remove the Helm release from the cluster:
   ```powershell
   helm uninstall myrelease
   ```
   *Verification Output:* `release "myrelease" uninstalled`.
2. Verify complete teardown of Kubernetes resources:
   ```powershell
   # Verify release removal
   helm list

   # Verify all application pods terminated
   kubectl get pods

   # Verify deployment deletion
   kubectl get deployments

   # Verify service deletion
   kubectl get services
   ```
   *Verification Output:* `No resources found in default namespace.` Only the internal `kubernetes` cluster service remains.

---

## Screenshot Evidence

| Figure | Screenshot | Technical Verification Description |
|:---:|---|---|
| **Figure 1** | [`1-kubernetes-tools-verification.png`](Screenshots/1-kubernetes-tools-verification.png) | Docker engine version (`v29.x`), `kubectl` client version, `docker-desktop` context, and cluster control-plane endpoints |
| **Figure 2** | [`2-kubernetes-cluster-info.png`](Screenshots/2-kubernetes-cluster-info.png) | `kubectl cluster-info` output and listing of active namespaces (`default`, `kube-system`, etc.) |
| **Figure 3** | [`3-kubernetes-nodes.png`](Screenshots/3-kubernetes-nodes.png) | Single-node cluster status verification (`desktop-control-plane` in `Ready` state) |
| **Figure 4** | [`4-kubernetes-architecture.png`](Screenshots/4-kubernetes-architecture.png) | Kubernetes control-plane components (API server, etcd, scheduler) and worker architecture diagram |
| **Figure 5** | [`5-helm-version.png`](Screenshots/5-helm-version.png) | Helm CLI version verification (`v3.15.0`) and overview of Helm operational commands |
| **Figure 6** | [`6-helm-chart-created.png`](Screenshots/6-helm-chart-created.png) | Creation of custom Helm chart `myapp` using `helm create` and directory verification |
| **Figure 7** | [`7-helm-chart-structure.png`](Screenshots/7-helm-chart-structure.png) | Full recursive directory tree inspection of `myapp` chart using `tree /F` |
| **Figure 8** | [`8-helm-template-output.png`](Screenshots/8-helm-template-output.png) | Chart lint validation (`helm lint`) and dry-run manifest rendering (`helm template`) |
| **Figure 9** | [`9-helm-install-success.png`](Screenshots/9-helm-install-success.png) | Successful Helm release installation (`myrelease`) with revision 1 in `default` namespace |
| **Figure 10** | [`10-kubernetes-pods-deployments-services.png`](Screenshots/10-kubernetes-pods-deployments-services.png) | Active Kubernetes resource verification (`kubectl get pods`, `deployments`, and `NodePort` service) |
| **Figure 11** | [`11-helm-list-and-status.png`](Screenshots/11-helm-list-and-status.png) | Helm release tracking verification via `helm list` and detailed status inspect via `helm status` |
| **Figure 12** | [`12-kubernetes-port-forward-configuration.png`](Screenshots/12-kubernetes-port-forward-configuration.png) | Port-forwarding configuration bridging localhost port `8081` to service port `80` |
| **Figure 13** | [`13-kubernetes-application-running.png`](Screenshots/13-kubernetes-application-running.png) | Live browser verification of the deployed NGINX web application on `http://localhost:8081` |
| **Figure 14** | [`14-helm-upgrade.png`](Screenshots/14-helm-upgrade.png) | Execution of release upgrade command (`helm upgrade myrelease`) scaling workload |
| **Figure 15** | [`15-kubernetes-upgrade-verification.png`](Screenshots/15-kubernetes-upgrade-verification.png) | Post-upgrade verification confirming 3 running Pod replicas (`3/3 AVAILABLE`) |
| **Figure 16** | [`16-helm-uninstall.png`](Screenshots/16-helm-uninstall.png) | Clean release uninstallation (`helm uninstall`) and verification of zero remaining resources |

---

## Learning Outcomes
1. **Container Orchestration with Kubernetes**: Gained practical competence with core Kubernetes API objects including Pods, ReplicaSets, Deployments, Services (NodePort/ClusterIP), and ServiceAccounts.
2. **Package Management via Helm**: Understood the architecture and utility of Helm as the de facto Kubernetes package manager, eliminating boilerplate YAML and managing application releases declaratively.
3. **Template Parameterization**: Learned to structure Helm charts using `Chart.yaml`, decouple environment variables into `values.yaml`, and leverage the Go templating syntax for dynamic resource generation.
4. **Validation and Pre-deployment Testing**: Mastered pre-flight chart validation techniques using `helm lint` and dry-run rendering via `helm template`.
5. **Release Lifecycle & Rolling Upgrades**: Experienced atomic release deployment, declarative scaling via `helm upgrade` without application downtime, and clean teardown via `helm uninstall`.
6. **Local Service Debugging**: Utilized `kubectl port-forward` to establish secure tunnels from local workstations to cluster-internal services.

---

## Submission Details
- **GitHub Repository:** [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-7](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-7)
- **Academic Report:** [`Report/123B1B184_Assignment_7_DevOps.pdf`](Report/123B1B184_Assignment_7_DevOps.pdf)
- **Hosted / Output:** N/A — Local Kubernetes cluster orchestrated via Docker Desktop.
