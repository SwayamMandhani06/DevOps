# DevOps Assignment 3 — Infrastructure as Code using Terraform

## Student Details
| Field | Details |
|---|---|
| Name | Swayam Laxminarayan Mandhani |
| PRN / Roll No | 123B1B184 |
| Class | B.Tech Computer Engineering |
| Division | C |
| Batch | C2 |
| Subject | DevOps |
| Assignment No. | 3 |
| Academic Year | 2026–27 |
| Report Document | [123B1B184_Assignment_3_DevOps.pdf](Report/123B1B184_Assignment_3_DevOps.pdf) |

## 1. Title
**Infrastructure as Code using Terraform for AWS EC2 Provisioning**

## 2. Aim
To study and implement Infrastructure as Code (IaC) using Terraform by defining and provisioning an AWS EC2 instance and its associated security group through Terraform configuration files.

## 3. Objectives
- Understand Infrastructure as Code.
- Configure the AWS provider in Terraform.
- Use Terraform variables and outputs.
- Provision an AWS EC2 instance using Terraform.
- Create and configure an AWS security group.
- Allow SSH on port 22 and HTTP on port 80.
- Verify the provisioned infrastructure.
- Inspect Terraform outputs and state.
- Perform infrastructure cleanup using `terraform destroy`.

## 4. Overview
Infrastructure as Code (IaC) manages infrastructure through machine-readable configuration rather than manual configuration. Terraform is a declarative IaC tool that can provision and manage cloud resources.

In this assignment, Terraform was used to provision an Ubuntu 24.04 LTS EC2 instance in AWS Mumbai (`ap-south-1`) and a Terraform-managed security group. The EC2 instance was verified, NGINX was installed and accessed through HTTP, Terraform outputs/state were checked, and the infrastructure was finally destroyed using Terraform.

## 5. Technologies Used
- Terraform
- Amazon EC2
- AWS Security Groups
- AWS CLI
- AWS IAM
- Ubuntu 24.04 LTS
- NGINX
- PowerShell
- Git / GitHub

## 6. Workflow
```text
Terraform Configuration
        ↓
terraform init
        ↓
terraform validate
        ↓
terraform plan
        ↓
terraform apply
        ↓
AWS EC2 + Security Group
        ↓
EC2 / NGINX Verification
        ↓
terraform output
        ↓
terraform state list
        ↓
terraform destroy
```

## 7. Project Structure
```text
Assignment-3/
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── main.tf
│   ├── outputs.tf
│   ├── .gitignore
│   └── terraform.tfvars
├── Report/
│   └── 123B1B184_Assignment_3_DevOps.pdf
├── Screenshots/
│   ├── 1-terraform-version.png
│   ├── 2-terraform-files.png
│   ├── 3-terraform-plan.png
│   ├── 4-terraform-apply-success.png
│   ├── 5-aws-ec2-running.png
│   ├── 6-terraform-state-output.png
│   ├── 7-nginx-web-verification.png
│   └── 8-terraform-destroy.png
└── README.md
```

> `terraform.tfvars`, Terraform state files, `.pem` private keys, and other sensitive files must not be committed to GitHub.

## 8. Terraform Configuration

### provider.tf
```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

### variables.tf
```hcl
variable "aws_region" {
  description = "AWS region where the EC2 instance will be created"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "Ubuntu AMI ID for the EC2 instance"
  type        = string
}

variable "key_name" {
  description = "Name of the AWS EC2 key pair"
  type        = string
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "DevOps-Terraform-EC2"
}
```

> During actual execution, `t3.micro` was supplied through `terraform.tfvars` because AWS rejected `t2.micro` as not eligible for the account's current Free Tier configuration.

### main.tf
```hcl
resource "aws_security_group" "devops_sg" {
  name        = "devops-terraform-sg"
  description = "Security group for DevOps Terraform EC2 instance"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name       = "DevOps-Terraform-SG"
    Assignment = "DevOps-Assignment-03"
    ManagedBy  = "Terraform"
  }
}

resource "aws_instance" "devops_ec2" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.devops_sg.id]

  tags = {
    Name       = var.instance_name
    Assignment = "DevOps-Assignment-03"
    ManagedBy  = "Terraform"
  }
}
```

### outputs.tf
```hcl
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.devops_ec2.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.devops_ec2.public_ip
}

output "instance_public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.devops_ec2.public_dns
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.devops_sg.id
}
```

## 9. Final AWS Configuration Used
| Parameter | Actual Value |
|---|---|
| AWS Region | `ap-south-1` |
| AMI | Ubuntu 24.04 LTS |
| AMI ID | `ami-007b1f3fdea0383d9` |
| Instance Type | `t3.micro` |
| Key Pair | `devops-assignment-2-key` |
| Security Group | `devops-terraform-sg` |
| SSH Port | 22 |
| HTTP Port | 80 |

## 10. Implementation Commands
```powershell
aws configure
aws sts get-caller-identity

terraform init
terraform fmt
terraform validate
terraform plan
terraform apply

terraform output
terraform state list

terraform destroy
```

NGINX verification on the EC2 instance:
```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable --now nginx
```

## 11. Actual Provisioning Result
```text
EC2 Instance ID: i-0213e369ad43d98d3
Security Group ID: sg-04ae315878da8108b
```

The EC2 public IP during verification was `65.0.73.47`. The infrastructure was subsequently destroyed using Terraform.

## 12. Screenshots
| Figure | Screenshot | Purpose |
|---|---|---|
| 1 | [`1-terraform-version.png`](Screenshots/1-terraform-version.png) | Terraform installation/version |
| 2 | [`2-terraform-files.png`](Screenshots/2-terraform-files.png) | Terraform project files |
| 3 | [`3-terraform-plan.png`](Screenshots/3-terraform-plan.png) | Terraform execution plan |
| 4 | [`4-terraform-apply-success.png`](Screenshots/4-terraform-apply-success.png) | Successful provisioning |
| 5 | [`5-aws-ec2-running.png`](Screenshots/5-aws-ec2-running.png) | EC2 running in AWS |
| 6 | [`6-terraform-state-output.png`](Screenshots/6-terraform-state-output.png) | Terraform outputs and state |
| 7 | [`7-nginx-web-verification.png`](Screenshots/7-nginx-web-verification.png) | NGINX web verification |
| 8 | [`8-terraform-destroy.png`](Screenshots/8-terraform-destroy.png) | Final infrastructure cleanup |

## 13. Result
The AWS infrastructure was successfully provisioned using Terraform. The EC2 instance and security group were defined as code, the EC2 instance was verified, NGINX was accessed through HTTP, Terraform outputs/state were inspected, and all Terraform-managed resources were removed after completion.

## 14. Conclusion
This assignment provided practical experience with Infrastructure as Code using Terraform. The implementation covered AWS provider configuration, variables, resources, outputs, EC2 provisioning, security group configuration, Terraform state, infrastructure verification, and resource cleanup.

## 15. References
1. Terraform Documentation — https://developer.hashicorp.com/terraform/docs
2. AWS EC2 Documentation — https://docs.aws.amazon.com/ec2/
3. AWS CLI Documentation — https://docs.aws.amazon.com/cli/
4. AWS IAM Documentation — https://docs.aws.amazon.com/iam/
5. AWS Security Groups Documentation — https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html

## 16. Submission Links
**GitHub Repository Link:** `https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-3`

**Hosted / Output Link:** `N/A — AWS Console based practical`
