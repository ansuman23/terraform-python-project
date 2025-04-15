# terraform-python-project

🛠️ Terraform Deployment (for Web Scraper)
This project uses Terraform to automate the deployment of the Python web scraper to an AWS EC2 instance.

✅ Purpose
Instead of running the scraper locally, Terraform provisions a virtual machine in the cloud, installs Python and dependencies, and runs the script automatically.


🚀 How to Deploy Using Terraform
1. Prerequisites
  - An AWS account
  - Install Terraform
  - Install AWS CLI

  Configure AWS credentials:
  
  ``bash
  aws configure
  ```
2. Create Terraform Config (terraform/main.tf)
```
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "scraper" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2
  instance_type = "t2.micro"
  key_name      = "your-keypair-name"

  user_data = <<-EOF
    #!/bin/bash
    sudo yum update -y
    sudo yum install python3 -y
    pip3 install beautifulsoup4 requests
    echo '${file("scraper.py")}' > scraper.py
    python3 scraper.py
  EOF

  tags = {
    Name = "web-scraper"
  }
}
```

3. Deploy with Terraform
In your terminal:
```bash

cd terraform/
terraform init
terraform apply
```

4. Destroy the Instance
```bash
terraform destroy
```
This will delete all resources created by Terraform to avoid charges.
