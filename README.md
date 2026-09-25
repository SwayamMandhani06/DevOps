# DevOps Practical Assignments

This repository contains the DevOps practical assignments completed as part of the B.Tech Computer Engineering curriculum at Pimpri Chinchwad College of Engineering (PCCOE). Each assignment focuses on hands-on implementation of core DevOps methodologies and cloud engineering domains, including cloud compute lifecycle management, object storage, serverless computing, managed relational databases, traffic distribution via load balancers, container orchestration, and telemetry monitoring.

---

# Student Details

| Field | Details |
|---|---|
| **Name** | Swayam Mandhani |
| **PRN / Roll No** | 123B1B184 |
| **Class** | B.Tech, Computer Engineering |
| **Division** | C |
| **Batch** | C2 |
| **Academic Year** | 2026‑27 |
| **Semester** | VII |
| **Subject** | DevOps |
| **Course Code** | BCE27PE01 |
| **Institution** | Pimpri Chinchwad College of Engineering (PCCOE), Pune |

---

# Repository Overview

This repository serves as a centralized portfolio for all DevOps practical coursework and lab submissions. The repository is modularly organized: each practical assignment resides in its dedicated directory containing:
- **`README.md`j*: In-depth technical documentation, step-by-step procedure, configuration commands, architecture workflows, and evaluation notes.
- **`Report/`**: Complete academic lab report in PDF format prepared according to the autonomous college submission template.
- **`Screenshots/`**: High-resolution, numbered image evidence documenting every milestone of the implementation, configuration parameters, verified web outputs, and resource teardown.

---

# Assignments

| Assignment | Title | Main Technologies / Services | Status | Documentation |
|---|---|---|---|---|
| **Assignment 2** | AWS Cloud Computing Services & EC2 Practical Lifecycle | AWS C2, S3, Lambda, RDS, ELB, ECS, CloudWatch, NGINX, Linux | **Completed** | [View Assignment 2](./Assignment-2/) |
| **Assignment 3** | Infrastructure as Code (IaC) with Terraform | Terraform, Cloud Infrastructure Provisioning | *Not yet completed* | *Scheduled* |
| **Assignment 4** | Containerization with Docker | Docker, Dockerfile, Container Management | *Not yet completed* | *Scheduled* |
| **Assignment 5** | Multi-Container Orchestration with Docker Compose | Docker Compose, Service Networking, Volumes | *Not yet completed* | *Scheduled* |

>{ ! NOTE]
> Detailed implementations and artifacts are actively documented upon practical completion. Assignment 2 is fully implemented, verified, and documented with complete screenshot evidence and academic reports. Subsequent curriculum assignments will be added as they are performed in the laboratory sessions.

---

# Assignment Details

## Assignment 2 — AWS Cloud Computing Services

### Objective
To study major Amazon Web Services (AWS) cloud computing solutions—including compute, storage, serverless functions, managed databases, load balancing, and container orchestration—for practically implementing, configuring, connecting to, monitoring, and decommissioning a cloud virtual machine instance using Amazon EC2.

### Key Concepts / Technologies
- **Amazon EC2 (Elastic Compute Cloud)**: Virtual machine provisioning, Amazon Linux 2023 AMI, `t3.micro` instance type, SSH key pairs, Security Groups (ports 22 & 80), browser-based EC2 Instance Connect, and VM administrative verification.
- **NGINX Web Server**: Package installation via `dnf`, service enablement with `systemctl`, HTTP traffic handling, and web page serving.
- **Amazon CloudWatch**: Telemetry monitoring, status checks (2/2 passing), and per-instance CPUPutilization metrics graphing.
- **Amazon S3 (Simple Storage Service)**: Object storage, bucket creation with Block Public Access enforcement, object upload (`s3-test.txt`), and object lifecycle management.
- **AWS Lambda**: Serverless computing, Python 3.12 runtime, handler execution, test event simulation (`devops-test-event`), and HTTP 200 response generation.
- **Amazon RDS (Relational Database Service)**: Managed relational database provisioning using MySQL Community engine (`db.t4g.micro`) in the `ap-south-1b` availability zone.
- **Elastic Load Balancing (ELB)**: Layer-7 Application Load Balancer (`devops-assignment-2-alb`), Target Group (`devops-assignment-2-tg`), HTTP listener on port 80, health checks, and DNS-based request routing.
- **Amazon ECS (Elastic Container Service)**: Container cluster management study and cluster creation (`devops-assignment-2-ecs`).
- **Resource Decommissioning & FinOps**: Planned teardown of instances, databases, load balancers, buckets, and functions to prevent billing leakage.

### Implementation
1. **EC2 Instance Lifecycle**: Launched `DevOps-Assignment-2-EC2` (`i-0c130501b321efcef`) in `ap-south-1` using Amazon Linux 2023 AMI and `t3.micro`. Configured firewall rules allowing SSH (port 22) and HTTP (port 80). Connected through EC2 Instance Connect, validated shell environment (`whoami`, `hostname`, `pwd`, `uname -a`), installed and enabled NGINX, web output verified locally and over public IPv4 (`13.232.27.135`). Monitored compute utilization via CloudWatch before final instance termination.
2. **S3 Object Storage**: Created general-purpose bucket `s3://devops-assignment-2-swayam-2026` with all public access blocked. Uploaded `s3-test.txt` (96 B), verified storage integrity, and deleted the object and bucket during cleanup.
3. **AWS Lambda Execution**: Authored and deployed a Python 3.12 serverless function `devops-assignment-2-lambda`. Invoked via test event `devops-test-event`, validating response `{"isSuccessful": true, "statusCode": 200, "body": "Hello from AWS Lambda!"}` with 80 ms execution duration.
4. **Amazon RDS Deployment**: Configured and provisioned a MySQL RDS instance `devops-test-rds` (`db.t4g.micro`). Monitored status until reaching the `Available` state, followed by immediate deletion without final snapshots.
5. **Load Balancing via ALB**: Created target group `devops-assignment-2-tg` (HTTP:80) and registered the running EC2 target. Configured internet-facing ALB `devops-assignment-2-alb@ and verified web traffic over the ALB DNS endpoint (`http://devops-assignment-2-alb-1312030093.ap-south-1.elb.amazonaws.com`).
6. **Amazon ECS Demonstration**: Successfully created cluster `devops-assignment-2-ecs` in the AWS console. In alignment with academic guidelines and AWS service-linked role observations, compute container tasks were not persisted to avoid unmonitored charges.

### Output / Evidence
- **Screenshots**: 21 high-resolution captured figures located in [`Assignment-2/Screenshots/`](./Assignment-2/Screenshots/)
- **Academic Report**: Comprehensive PDF report available at [`Assignment-2/Report/DevOps_Assignment_2_AWS_Report.pdf`,(./Assignment-2/Report/DevOps_Assignment_2_AWS_Report.pdf)

### Status
**Completed**

### Documentation
- Folder: [Assignment-2/](./Assignment-2/)
- GitHub Direct Link: [https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-2](https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-2)

---

# Technologies Used

### Cloud Computing Platform
- **Amazon Web Services (AWS)**
  - Amazon EC2 (Elastic Compute Cloud)
  - Amazon S3 (Simple Storage Service)
  - AWS Lambda (Serverless Compute)
  - Amazon RDS (Relational Database Service — MySQL)
  - Elastic Load Balancing (Application Load Balancer — ALB)
  - Amazon ECS (Elastic Container Service)
  - Amazon CloudWatch (Metrics & Observability)

### Web & Application Servers
- **NGINX** (HTTO Web Server & Reverse Proxy)

### Operating Systems & Shell
- **Amazon Linux 2023** (Kernel 6.18, x86_64)
- **Bash / Linux CLI** (systemd, dnf, curl, core utilities)
- **EC2 Instance Connect** (Browser-based SSH terminal)

### Languages & Runtimes
- **Python 3.12** (AWS Lambda runtime)

---

# Repository Structure

```text
DevOps/
├──README.md                                   # Master repository documentation (this file)
└──Assignment-2/                                 # Assignment 02: AWS Cloud Computing Services
    ├──README.md                                # Detailed Assignment 2 technical guide
    ├──Report/                                 # Complete academic submission report
     └──DevOps_Assignment_2_AWS_Report.pdf   #
    └──Screenshots/                              # High-resolution output verification
        “℠ 01-aws-console-region.png            # AWS console region selection (ap-south-1)
        “℠ 02-ec2-dashboard.png                 # EC2 dashboard overview
        ⌜℀ 03-ami-instance-type.png             # Amazon Linux 2023 & t3.micro configuration
        “℠ 04-key-pair.png                      # SSH key pair setup
        “℠ 05-security-group.png                # Security group rules (SSH 22, HTTP 80)
        “℠ 07-ec2-running.png                    # EC2 instance running state
        ⌜℀ 09-vm-verification.png                # Linux VM verification via EC2 Instance Connect
        ⌜℀ 10-nginx-running.png                  # NGIMX service installation and active status
        “℠ 12-ec2-web-output.png                 # Local web response verification via curl
        “℠ 13-ec2-monitoring.png                 # EC2 compute monitoring dashboard
        “℠ 14-cloudwatch-cpu.png                 # CloudWatch CPUUtilization metric graph
        ⌜℀ 15-s3-dashboard.png                    # Amazon S3 console dashboard
        ⌜℀ 16-s3-bucket-created.png            # S3 bucket creation with Block Public Access
        “℠ 17-s3-object-uploaded.png            # Successful text object upload to S3
        “℠ 18-aws-lambda-code.png               # Python Lambda handler code configuration
        ⌜℀ 19-lambda-test.png                  # Successful Lambda invocation & test response
        “℠ 20-rds-available.png                 # Managed MySQL RDS database in Available state
        ⌜℀ 21-target-group.png                  # ELB target group with registered EC2 target
        “℠ 22-alb-creation.png                 # Application Load Balancer configuration
        “℠ 23-alb-working.png                  # Verified ALB DNS endpoint in browser
        └─ 24-ecs-cluster.png                  # Amazon ECS cluster creation confirmation
```

---

# Academic Compliance & Integrity

- **Original Implementation**: All practical tasks were configured and executed individually on an active AWS cloud environment.
- **Security & Privacy**: No confidential credentials, IAM secret access keys, database passwords, or private key pairs (`.pem`) are stored in this repository.
- **Cloud Governance**: All temporary cloud resources (EC2 instances, ALBs, Target Groups, RDS databases, S3 objects/buckets, Lambda functions) were decommissioned immediately following practical verification.
