# DevOps Assignment 2 — AWS Cloud Computing Services

## Study of AWS Cloud Computing Services and Practical Implementation of Amazon EC2

This repository contains the implementation, architecture, screenshots, and complete documentation for **DevOps Assignment 2**. The assignment demonstrates major AWS cloud computing services and covers the complete practical lifecycle of an Amazon EC2 virtual machine along with storage, serverless compute, database, load balancing, and container orchestration services.

---

## 📋 Academic & Student Details

| Field | Details |
|---|---|
| **Institute** | Pimpri Chinchwad College of Engineering (PCCOE), Pune |
| **Department** | Computer Engineering |
| **Course** | DevOps |
| **Course Code** | BCE27PE01 |
| **Academic Year** | 2026 – 2027 |
| **Semester** | VII |
| **Student Name** | Swayam Mandhani |
| **PRN / Roll No** | 123B1B184 |
| **Class & Division** | B.Tech, Computer Engineering — Division C |
| **Batch** | C2 |
| **Assignment No.** | 02 |
| **Report Document** | [DevOps_Assignment_2_AWS_Report.pdf](Report/DevOps_Assignment_2_AWS_Report.pdf) |
| **Repository Link** | [https://github.com/SwayamMandhani06/DevOps/Assignment-2](https://github.com/SwayamMandhani06/DevOps/Assignment-2) |

---

## 🎯 Aim

To study major AWS cloud computing services including **Amazon EC2, Amazon S3, AWS Lambda, Amazon RDS, Elastic Load Balancing (ELB), and Amazon ECS**, and to practically create, configure, connect to, monitor, and terminate a virtual machine instance using Amazon EC2.

---

## ☁️ AWS Services Covered

| Service | Category | Role in Demonstration |
|---|---|---|
| **Amazon EC2** | Compute (Virtual Machine) | Provisioned Linux VM, configured security groups, connected via EC2 Instance Connect, deployed NGINX web server, monitored, and terminated. |
| **Amazon S3** | Object Storage | Created general-purpose S3 bucket with Block Public Access enabled, uploaded test text object, verified storage, and cleaned up. |
| **AWS Lambda** | Serverless Compute | Created and deployed Python serverless function, configured test event, and verified execution response. |
| **Amazon RDS** | Relational Database | Created managed MySQL database instance (`db.t4g.micro`), verified `Available` state, and performed cleanup. |
| **Elastic Load Balancing (ELB)** | Traffic Distribution | Created Target Group, registered EC2 instance target, configured Application Load Balancer (ALB), and accessed web app through ALB DNS. |
| **Amazon ECS** | Container Orchestration | Explored container orchestration principles and created an ECS Cluster (`devops-assignment-2-ecs`). |
| **Amazon CloudWatch** | Monitoring & Observability | Monitored EC2 CPU utilization, network traffic, and instance status checks. |

---

## 🏛️ System Architecture

```text
                                 [ Internet / User Browser ]
                                              │
                                              ▼
                             ┌─────────────────────────────────┐
                             │    Application Load Balancer    │
                             │ (devops-assignment-2-alb)       │
                             └────────────────┬────────────────┘
                                              │ HTTP : Port 80
                                              ▼
                             ┌─────────────────────────────────┐
                             │       ELB Target Group          │
                             │ (devops-assignment-2-tg)        │
                             └────────────────┬────────────────┘
                                              │
                                              ▼
                             ┌─────────────────────────────────┐
                             │       Amazon EC2 Instance       │
                             │ (DevOps-Assignment-2-EC2)       │
                             │   - Amazon Linux 2023           │
                             │   - NGINX Web Server (Port 80)  │
                             │   - Security Group (SSH/HTTP)   │
                             └────────┬───────────────┬────────┘
                                      │               │
                  Metrics & Alarms    │               │  Object Storage
                                      ▼               ▼
                        ┌──────────────────┐    ┌───────────────────────────┐
                        │ Amazon CloudWatch│    │ Amazon S3                 │
                        │ (CPUUtilization) │    │ (devops-assignment-2-...) │
                        └──────────────────┘    └───────────────────────────┘

           ┌────────────────────────────┐       ┌───────────────────────────┐
           │ AWS Lambda (Serverless)    │       │ Amazon RDS (MySQL)        │
           │ (devops-assignment-2-...)  │       │ (devops-assignment-2-rds) │
           └────────────────────────────┘       └───────────────────────────┘
```

---

## 🛠️ Step-by-Step Implementation

### 1. Amazon EC2 — Virtual Machine Lifecycle

Amazon EC2 was used for the complete hands-on virtual machine lifecycle:

```text
Select AMI & Type ──► Key Pair & Security Group ──► Launch Instance ──► EC2 Instance Connect ──► Install NGINX ──► Verify Web Output ──► CloudWatch Monitoring ──► Clean Termination
```

1. **Region Selection**: Selected `ap-south-1` (Asia Pacific - Mumbai) for low latency.
2. **AMI & Instance Type Selection**:
   - **AMI**: Amazon Linux 2023 AMI (`ami-066c4849e6b3a1e3d`, x86_64, Kernel 6.18)
   - **Instance Type**: `t3.micro` (Free tier eligible, 2 vCPUs, 1 GiB Memory)
   - **Instance Name**: `DevOps-Assignment-2-EC2`
3. **Key Pair & Security Group**:
   - Configured key pair `devops-assignment-2-key`
   - Created security group `DevOps-Assignment-2-SG` (`sg-00db7f73cc904b19d`) with inbound rules:
     - **SSH**: Port `22`, TCP, from authorized source
     - **HTTP**: Port `80`, TCP, from `0.0.0.0/0`
4. **Launch & Verification**:
   - Instance ID: `i-0c130501b321efcef`
   - Public IPv4: `13.232.27.135`
   - Private IPv4: `172.31.0.78`
5. **Connection via EC2 Instance Connect**:
   - Verified Linux shell environment with:
     ```bash
     whoami      # Output: ec2-user
     hostname    # Output: ip-172-31-0-78.ap-south-1.compute.internal
     pwd         # Output: /home/ec2-user
     uname -a    # Linux kernel verification
     ```
6. **Deploying & Configuring NGINX Web Server**:
   ```bash
   sudo dnf install -y nginx
   sudo systemctl start nginx
   sudo systemctl enable nginx
   sudo systemctl status nginx
   ```
7. **Verifying Web Output**:
   - Verified locally via terminal:
     ```bash
     curl http://localhost
     ```
   - Verified via browser using Public IPv4: `http://13.232.27.135`
8. **Monitoring & Observability**:
   - Inspected EC2 Management Console monitoring dashboard for CPU utilization, disk metrics, and 2/2 status checks.
   - CloudWatch per-instance metrics CPU utilization graphed.
9. **Instance Termination**:
   - Terminated the EC2 instance upon practical completion as part of resource cleanup.

---

### 2. Amazon S3 — Object Storage Demonstration

```text
Create Bucket ──► Configure Block Public Access ──► Upload Object ──► Verify Storage ──► Cleanup
```

1. Opened the Amazon S3 Console in `ap-south-1`.
2. Created a general-purpose bucket: `s3://devops-assignment-2-swayam-2026`.
3. Kept **Block all public access** enabled to follow cloud security best practices.
4. Uploaded a test file: `s3-test.txt` (size: 96.0 Bytes, MIME: `text/plain`).
5. Verified the upload status (`1 file, 96.0 B, 100.00% Succeeded`).
6. Cleaned up by deleting `s3-test.txt` and removing the bucket.

---

### 3. AWS Lambda — Serverless Function

```text
Create Function ──► Author Python Handler ──► Deploy ──► Test Event ──► Verify Execution ──► Cleanup
```

1. Created an AWS Lambda function named `devops-assignment-2-lambda`.
2. Runtime selected: **Python 3.12**.
3. Function Handler code (`lambda_function.py`):
   ```python
   def lambda_handler(event, context):
       return {
           "statusCode": 200,
           "body": "Hello from AWS Lambda!"
       }
   ```
4. Deployed the function and configured a test event: `devops-test-event`.
5. Invoked the function and verified execution:
   - **Status**: `Succeeded`
   - **Status Code**: `200`
   - **Body**: `"Hello from AWS Lambda!"`
   - **Billed Duration**: `80 ms`, Memory Used: `37 MB / 128 MB`
6. Cleaned up the function after capturing test evidence.

---

### 4. Amazon RDS — Managed Relational Database

```text
Select Engine ──► Configure DB Instance ──► Deploy RDS ──► Verify 'Available' State ──► Cleanup
```

1. Opened the Amazon RDS Console.
2. Selected **MySQL Community** as the database engine.
3. Created a test database instance: `devops-assignment-2-rds`.
4. Instance specifications:
   - **DB Instance Class**: `db.t4g.micro`
   - **Region / AZ**: `ap-south-1b`
5. Monitored creation until the database state reached **Available**.
6. Cleaned up by deleting the test database instance without retaining final snapshots to avoid recurring charges.

---

### 5. Elastic Load Balancing (ELB) — Application Load Balancer

```text
Create Target Group ──► Register EC2 Target ──► Configure ALB & Listener ──► Access ALB DNS ──► Cleanup
```

1. **Target Group Creation**:
   - Target group name: `devops-assignment-2-tg`
   - Target type: `Instances`
   - Protocol & Port: `HTTP: 80`
   - VPC: Default VPC (`vpc-03395c567b4b0d103`)
2. **Target Registration**:
   - Registered EC2 instance `DevOps-Assignment-2-EC2` (`i-0c130501b321efcef`) on port 80.
3. **Application Load Balancer Creation**:
   - Name: `devops-assignment-2-alb`
   - Scheme: Internet-facing, IPv4
   - Listener: HTTP on port 80 forwarding to `devops-assignment-2-tg`.
4. **Verification**:
   - Verified that the target reached the **Healthy** state.
   - Accessed the ALB DNS endpoint in the browser:
     ```text
     http://devops-assignment-2-alb-1312030093.ap-south-1.elb.amazonaws.com
     ```
   - Confirmed the "Welcome to nginx!" response served via the load balancer.
5. Cleaned up by deleting the ALB and Target Group.

---

### 6. Amazon ECS — Container Orchestration

1. Studied container management concepts under AWS Elastic Container Service (ECS).
2. Opened the ECS Console in `ap-south-1` and created a cluster named `devops-assignment-2-ecs`.
3. Verified the successful creation of the cluster in the ECS console (`devops-assignment-2-ecs has been created successfully`).
4. **Academic Observation**: During task definition and container task execution, AWS service-linked role permissions were evaluated (`Unable to assume the service linked role`). To adhere to cloud cost-governance and avoid launching unmonitored container tasks, no persistent container workloads were kept running.

---

## 📁 Repository Structure

```text
DevOps-Assignment-02/
│
├── .gitignore                                   # Git ignore rules (build artifacts, temp files)
├── README.md                                    # Comprehensive assignment documentation
│
├── Report/
│   └── DevOps_Assignment_2_AWS_Report.pdf       # Complete academic submission report
│
└── Screenshots/                                 # Practical output screenshots
    ├── 01-aws-console-region.png                # Figure 1: AWS Console region selection
    ├── 02-ec2-dashboard.png                     # Figure 2: Amazon EC2 dashboard
    ├── 03-ami-instance-type.png                 # Figure 3: EC2 AMI and instance-type configuration
    ├── 04-key-pair.png                          # Figure 4: EC2 key-pair configuration
    ├── 05-security-group.png                    # Figure 5: EC2 security-group configuration
    ├── 07-ec2-running.png                       # Figure 6: EC2 instance in Running state
    ├── 09-vm-verification.png                   # Figure 7: EC2 VM connection and verification
    ├── 10-nginx-running.png                     # Figure 8: NGINX service running on EC2
    ├── 12-ec2-web-output.png                    # Figure 9: EC2 web output verification
    ├── 13-ec2-monitoring.png                    # Figure 10: EC2 monitoring
    ├── 14-cloudwatch-cpu.png                    # Figure 11: CloudWatch CPU monitoring
    ├── 15-s3-dashboard.png                      # Figure 12: Amazon S3 dashboard
    ├── 16-s3-bucket-created.png                 # Figure 13: S3 bucket created
    ├── 17-s3-object-uploaded.png                # Figure 14: S3 object uploaded
    ├── 18-aws-lambda-code.png                   # Figure 15: AWS Lambda code configuration
    ├── 19-lambda-test.png                       # Figure 16: AWS Lambda successful test
    ├── 20-rds-available.png                     # Figure 17: Amazon RDS database in Available state
    ├── 21-target-group.png                      # Figure 18: ELB target group
    ├── 22-alb-creation.png                      # Figure 19: Application Load Balancer configuration
    ├── 23-alb-working.png                       # Figure 20: Working Application Load Balancer endpoint
    └── 24-ecs-cluster.png                       # Figure 21: Elastic Container Service (ECS) Cluster
```

---

## 🖼️ Output Evidence & Screenshot Gallery

### Figure 1: AWS Management Console — Region Selection
![Figure 1: AWS Management Console](Screenshots/01-aws-console-region.png)
*Region set to Asia Pacific (Mumbai) `ap-south-1` for practical implementation.*

---

### Figure 2: Amazon EC2 Dashboard
![Figure 2: Amazon EC2 Dashboard](Screenshots/02-ec2-dashboard.png)
*Amazon EC2 management dashboard showing compute resources overview.*

---

### Figure 3: EC2 AMI & Instance Type Configuration
![Figure 3: EC2 AMI & Instance Type](Screenshots/03-ami-instance-type.png)
*Selection of Amazon Linux 2023 AMI (x86_64) and `t3.micro` free tier eligible instance.*

---

### Figure 4: EC2 Key Pair Configuration
![Figure 4: EC2 Key Pair](Screenshots/04-key-pair.png)
*Configuring SSH key pair `devops-assignment-2-key` for authentication.*

---

### Figure 5: EC2 Security Group Configuration
![Figure 5: EC2 Security Group](Screenshots/05-security-group.png)
*Security Group `DevOps-Assignment-2-SG` with SSH (Port 22) and HTTP (Port 80) inbound rules.*

---

### Figure 6: EC2 Instance in Running State
![Figure 6: EC2 Instance Running](Screenshots/07-ec2-running.png)
*Instance `DevOps-Assignment-2-EC2` (`i-0c130501b321efcef`) active with Public IPv4 `13.232.27.135`.*

---

### Figure 7: EC2 VM Connection & System Verification
![Figure 7: EC2 VM Verification](Screenshots/09-vm-verification.png)
*Connected via EC2 Instance Connect executing `whoami`, `hostname`, and `pwd`.*

---

### Figure 8: NGINX Service Running on EC2
![Figure 8: NGINX Running](Screenshots/10-nginx-running.png)
*NGINX installed via `dnf`, started, enabled, and showing `active (running)`.*

---

### Figure 9: EC2 Web Output Verification
![Figure 9: EC2 Web Output](Screenshots/12-ec2-web-output.png)
*Terminal `curl http://localhost` returning the default NGINX welcome page.*

---

### Figure 10: EC2 Instance Monitoring Dashboard
![Figure 10: EC2 Monitoring](Screenshots/13-ec2-monitoring.png)
*EC2 console monitoring showing system status checks, CPU, and network utilization.*

---

### Figure 11: Amazon CloudWatch CPU Utilization Graph
![Figure 11: CloudWatch CPU Monitoring](Screenshots/14-cloudwatch-cpu.png)
*Per-instance CloudWatch metric graph plotting CPUUtilization over time.*

---

### Figure 12: Amazon S3 Dashboard
![Figure 12: Amazon S3 Dashboard](Screenshots/15-s3-dashboard.png)
*Amazon Simple Storage Service (S3) dashboard.*

---

### Figure 13: Amazon S3 Bucket Created
![Figure 13: S3 Bucket Created](Screenshots/16-s3-bucket-created.png)
*General-purpose S3 bucket `devops-assignment-2-swayam-2026` created with Block Public Access enabled.*

---

### Figure 14: Amazon S3 Object Upload Verification
![Figure 14: S3 Object Uploaded](Screenshots/17-s3-object-uploaded.png)
*Successful upload verification of test text file `s3-test.txt` (96.0 B).*

---

### Figure 15: AWS Lambda Function Code Configuration
![Figure 15: AWS Lambda Code](Screenshots/18-aws-lambda-code.png)
*Serverless Python function `devops-assignment-2-lambda` configured in the AWS Lambda console.*

---

### Figure 16: AWS Lambda Successful Test Invocation
![Figure 16: AWS Lambda Test Execution](Screenshots/19-lambda-test.png)
*Execution result `Succeeded` returning HTTP status code `200` and response body `"Hello from AWS Lambda!"`.*

---

### Figure 17: Amazon RDS Database in Available State
![Figure 17: Amazon RDS Available](Screenshots/20-rds-available.png)
*Managed MySQL database `devops-assignment-2-rds` (`db.t4g.micro`) active in the `Available` state.*

---

### Figure 18: Elastic Load Balancing Target Group
![Figure 18: ELB Target Group](Screenshots/21-target-group.png)
*Target Group `devops-assignment-2-tg` configured on HTTP port 80 with the EC2 target registered.*

---

### Figure 19: Application Load Balancer Creation & Configuration
![Figure 19: ALB Creation](Screenshots/22-alb-creation.png)
*Internet-facing Application Load Balancer `devops-assignment-2-alb` configured with HTTP listener.*

---

### Figure 20: Working Application Load Balancer Endpoint in Browser
![Figure 20: Working ALB Endpoint](Screenshots/23-alb-working.png)
*Accessing `http://devops-assignment-2-alb-1312030093.ap-south-1.elb.amazonaws.com` displaying the NGINX response.*

---

### Figure 21: Elastic Container Service (ECS) Cluster Created
![Figure 21: ECS Cluster](Screenshots/24-ecs-cluster.png)
*Amazon ECS cluster `devops-assignment-2-ecs` created successfully.*

---

## 🧹 Resource Cleanup & Cost Governance

In cloud environments and DevOps practices, automated or deliberate decommissioning of temporary resources is critical to prevent unexpected charges:

| Resource | Action Taken | Status |
|---|---|---|
| **Amazon EC2 Instance** (`i-0c130501b321efcef`) | Terminated via EC2 Console | Terminated |
| **Application Load Balancer** (`devops-assignment-2-alb`) | Deleted | Removed |
| **Target Group** (`devops-assignment-2-tg`) | Deleted | Removed |
| **Amazon RDS Database** (`devops-assignment-2-rds`) | Deleted without final snapshot | Removed |
| **AWS Lambda Function** (`devops-assignment-2-lambda`) | Deleted | Removed |
| **Amazon S3 Object & Bucket** (`s3://devops-assignment-2-swayam-2026`) | Deleted object and emptied/deleted bucket | Removed |
| **Amazon ECS Cluster** (`devops-assignment-2-ecs`) | Deleted / cleaned up | Removed |

> [!NOTE]
> All credentials, keys, private IP ranges, and temporary cloud resources were sanitized before publishing to GitHub to ensure security best practices.

---

## 💡 Key Learning Outcomes

Through this practical assignment, the following DevOps and Cloud Computing concepts were explored:
1. **Infrastructure Provisioning**: Understood virtual machine creation, virtualization types, AMIs, and compute sizing.
2. **Cloud Network & Security**: Configured Virtual Private Clouds (VPC), Subnets, Security Groups, and Inbound/Outbound firewall rules.
3. **Remote Administration**: Practiced secure instance connection using browser-based EC2 Instance Connect.
4. **Web Server Deployment**: Automated and verified installation of NGINX on Amazon Linux.
5. **Observability & Telemetry**: Evaluated metrics in Amazon CloudWatch including CPU utilization and status checks.
6. **Object Storage Management**: Managed scalable object storage with S3 and enforced public access block policies.
7. **Serverless Architectures**: Deployed lightweight event-driven functions using AWS Lambda.
8. **Managed Database Services**: Explored relational database provisioning with Amazon RDS and evaluated database engine parameters.
9. **Traffic Distribution & High Availability**: Configured Target Groups, health checks, and Application Load Balancers for routing traffic.
10. **Container Orchestration**: Understood AWS ECS cluster architecture and container management principles.
11. **FinOps & Resource Lifecycle**: Implemented responsible resource decommissioning to avoid cloud billing waste.

---

## 📝 Conclusion

This assignment provided comprehensive practical exposure to core AWS cloud computing services. Amazon EC2 was utilized to complete the full lifecycle of a cloud virtual machine — from instance provisioning, security group configuration, and EC2 Instance Connect access, to NGINX web server deployment, CloudWatch telemetry monitoring, and instance termination. Additionally, Amazon S3 demonstrated secure object storage, AWS Lambda illustrated serverless event execution, Amazon RDS showcased automated relational database management, Elastic Load Balancing demonstrated layer-7 traffic distribution to compute targets, and Amazon ECS highlighted container cluster orchestration. 

The practical reinforced foundational DevOps and cloud engineering skills, particularly in Infrastructure as a Service (IaaS), Platform as a Service (PaaS), serverless architectures, and cost-effective cloud resource governance.

---

## 📚 References

- [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/)
- [Elastic Load Balancing Documentation](https://docs.aws.amazon.com/elasticloadbalancing/)
- [Amazon ECS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)
- [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)

---

## 📌 Submission Information

- **Student Name**: Swayam Mandhani
- **PRN / Roll No**: 123B1B184
- **Class / Division**: B.Tech Computer Engineering, Division C, Batch C2
- **Course**: DevOps (BCE27PE01)
- **Institution**: Pimpri Chinchwad College of Engineering (PCCOE)
- **Assignment**: DevOps Assignment 02 — AWS Cloud Computing Services
- **GitHub Repository**: [https://github.com/SwayamMandhani06/DevOps/Assignment-2](https://github.com/SwayamMandhani06/DevOps/Assignment-2)
