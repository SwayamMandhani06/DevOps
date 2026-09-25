# DevOps Practical Assignments

This repository contains the DevOps practical assignments completed as part of the B.Tech Computer Engineering curriculum at Pimpri Chinchwad College of Engineering (PCCOE). Each assignment focuses on hands-on implementation of core DevOps methodologies and cloud engineering domains, including cloud compute lifecycle management, object storage, serverless computing, managed relational databases, traffic distribution via load balancers, container orchestration, Infrastructure as Code (IaC) with Terraform, application containerization with Docker, and telemetry monitoring.

---

# Student Details

| Field | Details |
|---|---|
| **Name** | Swayam Mandhani |
| **PRN / Roll No** | 123B1B184 |
| **Class** | B.Tech, Computer Engineering |
| **Division** | C |
| **Batch** | C2 |
| **Academic Year** | 2026–27 |
| **Semester** | VII |
| **Subject** | DevOps |
| **Course Code** | BCE27PE01 |
| **Institution** | Pimpri Chinchwad College of Engineering (PCCOE), Pune |

---

# Repository Overview

This repository serves as a centralized portfolio for all DevOps practical coursework and lab submissions. The repository is modularly organized: each practical assignment resides in its dedicated directory containing:
- **`README.md`**: In-depth technical documentation, step-by-step procedure, configuration commands, architecture workflows, and evaluation notes.
- **`Report/`**: Complete academic lab report in PDF format prepared according to the autonomous college submission template (where applicable).
- **`Screenshots/`**: High-resolution, numbered image evidence documenting every milestone of the implementation, configuration parameters, verified web outputs, and resource teardown.
- **Source / Configuration Files**: Infrastructure as Code (IaC) templates, Docker container recipes, application source code, and deployment descriptors where applicable.

---

# Assignments

| Assignment | Title | Main Technologies / Services | Status | Documentation |
|---|---|---|---|---|
| **Assignment 2** | AWS Cloud Computing Services & EC2 Practical Lifecycle | AWS EC2, S3, Lambda, RDS, ELB, ECS, CloudWatch, NGINX, Linux | **Completed** | [View Assignment 2](./Assignment-2/) |
| **Assignment 3** | Infrastructure as Code (IaC) using Terraform for AWS EC2 Provisioning | Terraform, AWS EC2, Security Groups, NGINX, Ubuntu 24.04, AWS CLI | **Completed** | [View Assignment 3](./Assignment-3/) |
| **Assignment 4** | Containerization with Docker — Create or Migrate an Application | Docker, Dockerfile, Container Lifecycle, Python 3.12, Flask | **Completed** | [View Assignment 4](./Assignment-4/) |
| **Assignment 5** | Multi-Container Orchestration with Docker Compose | Docker Compose, Service Networking, Volumes | *Not yet completed* | *Scheduled* |

> [!NOTE]
> Detailed implementations and artifacts are actively documented upon practical completion. Assignments 2, 3, and 4 are fully implemented, verified, and documented with complete configuration code, screenshots, and technical guides. Subsequent curriculum assignments will be added as they are performed in the laboratory sessions.

---

# Assignment Details

## Assignment 2 — AWS Cloud Computing Services

### Objective
To study major Amazon Web Services (AWS) cloud computing solutions—including compute, storage, serverless functions, managed databases, load balancing, and container orchestration—and to practically implement, configure, connect to, monitor, and decommission a cloud virtual machine instance using Amazon EC2.

### Key Concepts / Technologies
- **Amazon EC2 (Elastic Compute Cloud)**: Virtual machine provisioning, Amazon Linux 2023 AMI, `t3.micro` instance type, SSH key pairs, Security Groups (ports 22 & 80), browser-based EC2 Instance Connect, and VM validation.
- **NGINX Web Server**: Package installation via `dnf`, service enablement with `systemctl`, HTTP traffic handling, and web page serving.
- **Amazon CloudWatch**: Telemetry monitoring, status checks (2/2 passing), and per-instance CPU utilization metrics graphing.
- **Amazon S3 (Simple Storage Service)**: Object storage, bucket creation with Block Public Access enforcement, object upload (`s3-test.txt`), and object lifecycle management.
- **AWS Lambda**: Serverless computing, Python 3.12 runtime, handler execution, test event simulation (`devops-test-event`), and HTTP 200 response generation.
- **Amazon RDS (Relational Database Service)**: Managed relational database provisioning using MySQL Community engine (`db.t4g.micro`) in the `ap-south-1b` availability zone.
- **Elastic Load Balancing (ELB)**: Layer-7 Application Load Balancer (`devops-assignment-2-alb`), Target Group (`devops-assignment-2-tg`), HTTP listener on port 80, health checks, and DNS-based request routing.
- **Amazon ECS (Elastic Container Service)**: Container cluster management study and cluster creation (`devops-assignment-2-ecs`).
- **Resource Decommissioning & FinOps**: Planned teardown of instances, databases, load balancers, buckets, and functions to prevent billing leakage.

### Implementation
1. **EC2 Instance Lifecycle**: Launched `DevOps-Assignment-2-EC2` (`i-0c130501b321efcef`) in `ap-south-1` using Amazon Linux 2023 AMI and `t3.micro`. Configured firewall rules allowing SSH (port 22) and HTTP (port 80). Connected through EC2 Instance Connect, validated shell environment (`whoami`, `hostname`, `pwd`, `uname -a`), installed and enabled NGINX, and verified web output locally and over public IPv4 (`13.232.27.135`). Monitored compute utilization via CloudWatch before final instance termination.
2. **S3 Object Storage**: Created general-purpose bucket `s3://devops-assignment-2-swayam-2026` with all public access blocked. Uploaded `s3-test.txt` (96 B), verified storage integrity, and deleted the object and bucket during cleanup.
3. **AWS Lambda Execution**: Authored and deployed a Python 3.12 serverless function `devops-assignment-2-lambda`. Invoked via test event `devops-test-event`, validating response `{"statusCode": 200, "body": "Hello from AWS Lambda!"}` with 80 ms execution duration.
4. **Amazon RDS Deployment**: Configured and provisioned a MySQL RDS instance `devops-assignment-2-rds` (`db.t4g.micro`). Monitored status until reaching the `Available` state, followed by immediate deletion without final snapshots.
5. **Load Balancing via ALB**: Created target group `devops-assignment-2-tg` (HTTP:80) and registered the running EC2 target. Configured internet-facing ALB `devops-assignment-2-alb` and verified web traffic over the ALB DNS endpoint (`http://devops-assignment-2-alb-1312030093.ap-south-1.elb.amazonaws.com`).
6. **Amazon ECS Demonstration**: Successfully created cluster `devops-assignment-2-ecs` in the AWS console. In alignment with academic guidelines and AWS service-linked role observations, compute container tasks were not persisted to avoid unmonitored charges.

### Output / Evidence
- **Screenshots**: 21 high-resolution captured figures located in [`Assignment-2/Screenshots/`](./Assignment-2/Screenshots/)
- **Academic Report**: Comprehensive PDF report available at [`Assignment-2/Report/123B1B184_Assignment_2_DevOps.pdf`](./Assignment-2/Report/123B1B184_Assignment_2_DevOps.pdf)

### Status
**Completed**

### Documentation
- Folder: [Assignment-2/](./Assignment-2/)
- GitHub Direct Link: [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-2](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-2)

---

## Assignment 3 — Infrastructure as Code using Terraform

### Objective
To study and implement Infrastructure as Code (IaC) principles using HashiCorp Terraform by declaratively defining, planning, provisioning, verifying, and destroying an Amazon EC2 virtual machine and its accompanying security group on AWS.

### Key Concepts / Technologies
- **Infrastructure as Code (IaC)**: Declarative cloud resource management, eliminating manual console drift and standardizing infrastructure deployment.
- **HashiCorp Terraform**: Open-source IaC engine using HashiCorp Configuration Language (HCL), managing state transitions, dependency graphs, and resource lifecycles.
- **Terraform Workflow**: Systematic progression through `init` → `fmt` / `validate` → `plan` → `apply` → `output` / `state` → `destroy`.
- **AWS Provider**: Official plugin (`hashicorp/aws ~> 6.0`) interfacing with AWS APIs in region `ap-south-1` (Mumbai).
- **Modular Terraform Structure**: Clean separation of concerns across `provider.tf`, `variables.tf`, `main.tf`, `outputs.tf`, and `terraform.tfvars`.
- **Security Group Management**: Automated ingress rules for SSH (port 22) and HTTP (port 80), plus unrestricted outbound traffic (`0.0.0.0/0`).
- **Ubuntu 24.04 LTS Compute Instance**: Automated provisioning of an AWS EC2 instance (`t3.micro`, AMI `ami-007b1f3fdea0383d9`).
- **NGINX Web Server Verification**: Remote connection and automated web server installation via `apt`, validating live HTTP web traffic.
- **Resource Decommissioning**: Full infrastructure destruction using `terraform destroy` for clean cloud cost governance.

### Core Terraform Files
The infrastructure is organized modularly under [`Assignment-3/terraform/`](./Assignment-3/terraform/):
- **[`provider.tf`](./Assignment-3/terraform/provider.tf)**: Declares required Terraform version (`>= 1.5.0`), required provider (`hashicorp/aws ~> 6.0`), and configures the AWS provider with `region = var.aws_region`.
- **[`variables.tf`](./Assignment-3/terraform/variables.tf)**: Defines configurable parameters with descriptions and defaults: `aws_region`, `instance_type` (`t3.micro`), `ami_id`, `key_name`, and `instance_name` (`DevOps-Terraform-EC2`).
- **[`main.tf`](./Assignment-3/terraform/main.tf)**: Defines infrastructure resources:
  - `aws_security_group.devops_sg`: Creates `devops-terraform-sg` with port 22 (SSH) and port 80 (HTTP) ingress rules and tags.
  - `aws_instance.devops_ec2`: Provisions the EC2 instance with variable references for AMI, instance type, key pair, security group association, and metadata tags.
- **[`outputs.tf`](./Assignment-3/terraform/outputs.tf)**: Exposes essential deployment values: `instance_id`, `instance_public_ip`, `instance_public_dns`, and `security_group_id`.
- **`terraform.tfvars`**: Contains environment-specific values (AMI ID, key pair name; excluded from source control via `.gitignore`).

### Terraform Workflow & Implementation
The complete end-to-end workflow executed during the practical:

```text
┌─────────────────┐       ┌────────────────────┐       ┌──────────────────┐
│ terraform init  │ ───►  │ terraform validate │ ───►  │  terraform plan  │
│ (Download AWS   │       │ (Syntax & config   │       │ (Execution diff: │
│  provider ~6.0) │       │  correctness check)│       │  +2 to add)      │
└─────────────────┘       └────────────────────┘       └────────┬─────────┘
                                                                │
┌─────────────────┐       ┌────────────────────┐                │
│terraform destroy│ ◄───  │ EC2 / NGINX Test   │ ◄──────────────┘
│ (Clean teardown │       │ (curl / browser on │       ┌──────────────────┐
│  of all 2 items)│       │  public IP:80)     │ ◄───  │ terraform apply  │
└─────────────────┘       └────────────────────┘       │ (Provision EC2 + │
                                                       │  Security Group) │
                                                       └──────────────────┘
```

1. **Authentication & Initialization**:
   - Authenticated AWS credentials using `aws configure` and verified identity via `aws sts get-caller-identity`.
   - Executed `terraform init` to download and initialize the AWS provider plugin (`hashicorp/aws v6.16.0`).
2. **Formatting & Validation**:
   - Executed `terraform fmt` to ensure clean, standardized indentation.
   - Ran `terraform validate`, confirming: `Success! The configuration is valid.`
3. **Execution Plan**:
   - Ran `terraform plan`, inspecting the planned actions (+2 to add: `aws_instance.devops_ec2` and `aws_security_group.devops_sg`).
4. **Provisioning via Apply**:
   - Executed `terraform apply -auto-approve`.
   - Successfully provisioned:
     - **EC2 Instance ID**: `i-0213e369ad43d98d3`
     - **Security Group ID**: `sg-04ae315878da8108b`
     - **Public IP**: `65.0.73.47`
     - **Public DNS**: `ec2-65-0-73-47.ap-south-1.compute.amazonaws.com`
5. **State & Output Inspection**:
   - Inspected output variables via `terraform output`.
   - Listed tracked resources via `terraform state list`.
6. **NGINX Web Server Verification**:
   - Connected to the instance via SSH and deployed NGINX:
     ```bash
     sudo apt update
     sudo apt install nginx -y
     sudo systemctl enable --now nginx
     ```
   - Verified HTTP traffic through a web browser accessing `http://65.0.73.47`, confirming the default "Welcome to nginx!" page.
7. **Clean Teardown with Terraform Destroy**:
   - Executed `terraform destroy -auto-approve` to terminate the EC2 instance and remove the security group.
   - Verified complete destruction: `Destroy complete! Resources: 2 destroyed.`

### Output / Evidence
- **Screenshots**: 8 comprehensive output verification screenshots located in [`Assignment-3/Screenshots/`](./Assignment-3/Screenshots/):
  - `1-terraform-version.png`: Terraform v1.5+ and AWS provider verification.
  - `2-terraform-files.png`: Directory listing showing modular `.tf` file structure.
  - `3-terraform-plan.png`: Execution plan output showing +2 resources to create.
  - `4-terraform-apply-success.png`: Successful apply completion with output values.
  - `05-aws-ec2-running.png`: AWS Management Console confirming EC2 in `Running` state.
  - `6-terraform-state-output.png`: Verification of `terraform state list` and `terraform output`.
  - `07-nginx-web-verification.png`: Browser HTTP verification of NGINX on `http://65.0.73.47`.
  - `8-terraform-destroy.png`: Clean destruction of all resources via `terraform destroy`.
- **Academic Report**: Comprehensive PDF report available at [`Assignment-3/Report/123B1B184_Assignment_3_DevOps.pdf`](./Assignment-3/Report/123B1B184_Assignment_3_DevOps.pdf).

### Status
**Completed**

### Documentation
- Folder: [Assignment-3/](./Assignment-3/)
- GitHub Direct Link: [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-3](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-3)

---

## Assignment 4 — Create or Migrate an Application to Docker

### Objective
To containerize and package a Python Flask web application and its dependencies into a portable Docker image using a multi-step Dockerfile, execute it in an isolated Docker container with port mapping, verify application and health check endpoints, inspect container execution logs and internal filesystem, demonstrate container lifecycle management, and perform clean resource teardown.

### Key Concepts / Technologies
- **Application Containerization**: Encapsulating application code, runtime dependencies, and environment configuration into an immutable container image to eliminate environment discrepancy.
- **Docker Engine & Docker Desktop**: Container runtime platform providing process isolation, resource abstraction, and CLI tooling for image and container management.
- **Declarative Dockerfile**: Multi-layer build definition based on `python:3.12-slim`, establishing working directory (`/app`), caching dependencies (`pip install --no-cache-dir -r requirements.txt`), copying application files, exposing port `5000`, and defining runtime command `CMD ["python", "app.py"]`.
- **Build Context Filtering (`.dockerignore`)**: Excluding bytecode caches (`__pycache__`, `*.pyc`), git directories (`.git`), virtual environments (`venv`), environment files (`.env`), and markdown documentation from the Docker build context.
- **Python 3.12 & Flask Web Service**: Lightweight REST-compatible Python web application configured to listen on `0.0.0.0:5000` inside the container, implementing root (`/`) and health check (`/health`) routes.
- **Port Mapping & Network Forwarding**: Exposing container port 5000 to host port 5000 (`-p 5000:5000`) for seamless HTTP access from host machine browsers and clients.
- **Container Observability & Telemetry**: Inspecting container stdout/stderr output via `docker logs`, accessing the running container shell interactively via `docker exec -it <container> sh`, and verifying containerized file placement (`pwd`, `ls`).
- **Container Lifecycle Operations**: Managing runtime states including starting, running in detached mode (`-d`), graceful stopping (`docker stop`), status queries (`docker ps`, `docker ps -a`), and restarting (`docker start`).
- **Resource Decommissioning & Cleanup**: Stopping active containers, removing terminated container instances (`docker rm`), and deleting custom container images (`docker rmi`) to maintain clean local storage.

### Core Project Files
The containerized application is structured under [`Assignment-4/`](./Assignment-4/):
- **[`app.py`](./Assignment-4/app.py)**: Python Flask application serving the home route (`/`) and health check route (`/health`), binding to `0.0.0.0:5000`.
- **[`Dockerfile`](./Assignment-4/Dockerfile)**: Docker build recipe specifying the `python:3.12-slim` base image, working directory, package installation, port exposure, and execution entrypoint.
- **[`requirements.txt`](./Assignment-4/requirements.txt)**: Python package dependency file pinning `Flask`.
- **[`.dockerignore`](./Assignment-4/.dockerignore)**: Build context exclusion filter preventing unnecessary files and caches from entering the Docker image.
- **[`README.md`](./Assignment-4/README.md)**: Detailed assignment guide with comprehensive build, execution, lifecycle, and verification commands.

### Docker Workflow & Implementation
The complete end-to-end containerization workflow executed during the practical:

```text
┌────────────────────┐       ┌────────────────────┐       ┌────────────────────┐
│ Write Application  │ ───►  │   docker build     │ ───►  │    docker run      │
│ (app.py, reqs,     │       │ (Build image:      │       │ (Run in background:│
│  Dockerfile,       │       │  flask-docker-     │       │  -p 5000:5000      │
│  .dockerignore)    │       │  app:v1)           │       │  flask-container)  │
└────────────────────┘       └────────────────────┘       └─────────┬──────────┘
                                                                    │
┌────────────────────┐       ┌────────────────────┐                 │
│   docker cleanup   │ ◄───  │Lifecycle Management│ ◄───────────────┤
│(docker stop, rm,   │       │(docker stop, start,│                 ▼
│ docker rmi image)  │       │ ps, ps -a checks)  │       ┌────────────────────┐
└────────────────────┘       └────────────────────┘       │ Verify & Inspect   │
                                                          │ - http://...:5000  │
                                                          │ - /health endpoint │
                                                          │ - docker logs      │
                                                          │ - docker exec (sh) │
                                                          └────────────────────┘
```

1. **Pre-requisite & Local Testing**:
   - Verified Docker Engine installation and operational status using `docker --version`, `docker info`, and `docker run hello-world`.
   - Tested the Flask application locally via `pip install -r requirements.txt` and `python app.py`.
2. **Docker Image Build**:
   - Built the Docker container image from the Dockerfile:
     ```powershell
     docker build -t flask-docker-app:v1 .
     ```
   - Verified image generation and metadata in local storage:
     ```powershell
     docker images
     ```
3. **Container Execution & Port Mapping**:
   - Ran the containerized application in detached mode with host-to-container port mapping:
     ```powershell
     docker run -d -p 5000:5000 --name flask-container flask-docker-app:v1
     ```
   - Verified container running status and mapped ports using `docker ps`.
4. **Application & Health Endpoint Verification**:
   - Tested the primary application endpoint:
     - URL: `http://localhost:5000`
     - Response: `"Hello! My application is running inside Docker."`
   - Tested the health check endpoint:
     - URL: `http://localhost:5000/health`
     - Response: `{"status": "healthy"}`
5. **Logs & Container Shell Inspection**:
   - Inspected application request logs streamed from the container:
     ```powershell
     docker logs flask-container
     ```
   - Opened an interactive shell inside the running container to inspect the working directory and files:
     ```powershell
     docker exec -it flask-container sh
     pwd   # Output: /app
     ls    # Output: Dockerfile app.py requirements.txt
     exit
     ```
6. **Container Lifecycle Management**:
   - Tested graceful container stopping:
     ```powershell
     docker stop flask-container
     docker ps        # Confirmed container is no longer running
     docker ps -a     # Confirmed container status is Exited (0)
     ```
   - Tested restarting the container:
     ```powershell
     docker start flask-container
     docker ps        # Confirmed container resumed active running state
     ```
7. **Resource Teardown & Cleanup**:
   - Stopped and removed the container and deleted the custom Docker image to maintain clean disk hygiene:
     ```powershell
     docker stop flask-container
     docker rm flask-container
     docker rmi flask-docker-app:v1
     docker images    # Confirmed removal of custom image
     ```

### Output / Evidence
- **Screenshots**: 15 comprehensive output verification screenshots located in [Assignment-4/Screenshots/](./Assignment-4/Screenshots/)
- **Academic Report**: Comprehensive PDF report available at [Assignment-4/Report/123B1B184_Assignment_4_DevOps.pdf](./Assignment-4/Report/123B1B184_Assignment_4_DevOps.pdf)
- **Practical Verification Milestones**: Verified through 13 practical execution milestones:
  1. Local Flask application execution and verification
  2. Local `/health` endpoint response
  3. Successful Docker image build (`flask-docker-app:v1`)
  4. Local `docker images` inventory listing
  5. Container execution and port mapping verification (`5000:5000`)
  6. Dockerized application response on `http://localhost:5000`
  7. Dockerized `/health` response on `http://localhost:5000/health`
  8. Container runtime stdout logs via `docker logs`
  9. Interactive shell inspection (`pwd`, `ls`) inside container filesystem
  10. Container stop operation and `docker ps -a` status check
  11. Container restart operation via `docker start`
  12. Container removal via `docker rm`
  13. Docker image cleanup via `docker rmi`

### Status
**Completed**

### Documentation
- Folder: [Assignment-4/](./Assignment-4/)
- GitHub Direct Link: [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-4](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-4)

---

# Technologies Used

### Cloud Computing Platform
- **Amazon Web Services (AWS)**
  - Amazon EC2 (Elastic Compute Cloud — Amazon Linux 2023 & Ubuntu 24.04 LTS)
  - Amazon S3 (Simple Storage Service — Buckets & Objects)
  - AWS Lambda (Serverless Compute — Python runtime)
  - Amazon RDS (Relational Database Service — Managed MySQL)
  - Elastic Load Balancing (Application Load Balancer — ALB & Target Groups)
  - Amazon ECS (Elastic Container Service — Cluster orchestration)
  - Amazon CloudWatch (Metrics, Observability & Alarms)
  - AWS VPC & Security Groups (Network Access Control & Firewall Rules)
  - AWS CLI (`aws configure`, `aws sts get-caller-identity`)

### Infrastructure as Code (IaC)
- **HashiCorp Terraform** (Core CLI v1.5+, AWS Provider `~> 6.0`, State Management, Lifecycle Automation)

### Containers & Virtualization
- **Docker Engine & Docker Desktop** (Container runtime, daemon, and image management)
- **Dockerfile** (Declarative container build specifications)
- **Docker CLI** (Image building, container execution, inspection, lifecycle, and teardown)

### Web & Application Servers / Frameworks
- **Flask** (Python lightweight web framework and REST service)
- **NGINX** (HTTP Web Server & Reverse Proxy)

### Operating Systems, Tools & Shell
- **Amazon Linux 2023** (Kernel 6.18, x86_64)
- **Ubuntu 24.04 LTS** (Noble Numbat, x86_64)
- **Debian / Python Slim** (`python:3.12-slim` container base image)
- **Bash / Linux CLI** (systemd, dnf, apt, curl, core utilities)
- **PowerShell** (Windows CLI execution for Terraform and Docker automation)
- **EC2 Instance Connect & SSH** (Secure remote shell access)

### Languages & Configuration Formats
- **Python 3.12** (Flask web service, AWS Lambda handler)
- **HashiCorp Configuration Language (HCL)** (Terraform configuration)
- **Dockerfile Syntax** (Container image build instructions)

---

# Repository Structure

```text
DevOps/
├── README.md                                    # Master repository documentation (this file)
├── Assignment-2/                                # Assignment 02: AWS Cloud Computing Services
│   ├── README.md                                # Detailed Assignment 2 technical guide
│   ├── Report/                                  # Complete academic submission report
│   │   └── 123B1B184_Assignment_2_DevOps.pdf
│   └── Screenshots/                             # High-resolution output verification (21 figures)
│       ├── 01-aws-console-region.png
│       ├── 02-ec2-dashboard.png
│       ├── 03-ami-instance-type.png
│       ├── 04-key-pair.png
│       ├── 05-security-group.png
│       ├── 07-ec2-running.png
│       ├── 09-vm-verification.png
│       ├── 10-nginx-running.png
│       ├── 12-ec2-web-output.png
│       ├── 13-ec2-monitoring.png
│       ├── 14-cloudwatch-cpu.png
│       ├── 15-s3-dashboard.png
│       ├── 16-s3-bucket-created.png
│       ├── 17-s3-object-uploaded.png
│       ├── 18-aws-lambda-code.png
│       ├── 19-lambda-test.png
│       ├── 20-rds-available.png
│       ├── 21-target-group.png
│       ├── 22-alb-creation.png
│       ├── 23-alb-working.png
│       └── 24-ecs-cluster.png
├── Assignment-3/                                # Assignment 03: Infrastructure as Code using Terraform
│   ├── README.md                                # Detailed Assignment 3 technical guide
│   ├── Report/                                  # Academic submission report
│   │   └── 123B1B184_Assignment_3_DevOps.pdf
│   ├── Screenshots/                             # Terraform provisioning verification screenshots (8 figures)
│   │   ├── 1-terraform-version.png
│   │   ├── 2-terraform-files.png
│   │   ├── 3-terraform-plan.png
│   │   ├── 4-terraform-apply-success.png
│   │   ├── 05-aws-ec2-running.png
│   │   ├── 6-terraform-state-output.png
│   │   ├── 07-nginx-web-verification.png
│   │   └── 8-terraform-destroy.png
│   └── terraform/                               # Terraform HCL configuration files
│       ├── provider.tf
│       ├── variables.tf
│       ├── main.tf
│       ├── outputs.tf
│       └── .gitignore
└── Assignment-4/                                # Assignment 04: Create or Migrate an Application to Docker
    ├── README.md                                # Detailed Assignment 4 containerization guide
    ├── app.py                                   # Python Flask web application (ports & health routes)
    ├── requirements.txt                         # Application runtime dependencies (Flask)
    ├── Dockerfile                               # Container build instructions (python:3.12-slim)
    ├── .dockerignore                            # Build context ignore rules
    ├── Report/                                  # Academic submission report
    │   └── 123B1B184_Assignment_4_DevOps.pdf
    └── Screenshots/                             # Practical output verification screenshots (15 figures)
        ├── 0-docker-verification (1).png
        ├── 0-docker-verification.png
        ├── 1-local-flask.png
        ├── 2-flask-healthy.png
        ├── 3-docker-build.png
        ├── 4-docker-images.png
        ├── 5-docker-run.png
        ├── 6-dockerized-running.png
        ├── 7-dockerized-health-check.png
        ├── 8-docker-container-logs.png
        ├── 9-applications-inside-docker.png
        ├── 10-stopping-and-checking-status-of-container.png
        ├── 11-restart-docker-container.png
        ├── 12-container-removed.png
        └── 13-docker-image-cleanup.png
```

---

# Academic Compliance & Integrity

- **Original Implementation**: All practical tasks were configured and executed individually across AWS cloud environments and local Docker container runtimes.
- **Security & Privacy**: No confidential credentials, IAM secret access keys, database passwords, `.tfvars` variable files, or private key pairs (`.pem`) are stored in this repository.
- **Resource Governance & Teardown**: All temporary cloud resources (EC2 instances, ALBs, Target Groups, RDS databases, S3 objects/buckets, Lambda functions, Terraform-managed infrastructure) and local Docker containers/images were decommissioned immediately following practical verification.
