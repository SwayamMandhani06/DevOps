# Security Group
resource "aws_security_group" "devops_sg" {
  name        = "devops-terraform-sg"
  description = "Security group for DevOps Terraform EC2 instance"

  # SSH access
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTP access
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
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


# EC2 Instance
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