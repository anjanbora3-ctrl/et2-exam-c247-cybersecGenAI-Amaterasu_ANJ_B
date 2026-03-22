resource "aws_ec2" "example_172" {
  name = "infrastructure_172.tf"
  port = 3306
  public_access = true
}
