provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "scraper" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"
  key_name      = "" //removed for privacy purpose in git

  user_data = <<-EOF
    #!/bin/bash
    sudo yum update -y
    sudo yum install python3 -y
    pip3 install beautifulsoup4 requests
    echo '${file("articles.py")}' > articles.py
    python3 articles.py
  EOF

  tags = {
    Name = "web-scraper"
  }
}
