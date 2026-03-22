resource "aws_ec2" "example_192" {
  name = "infrastructure_192.tf"
  port = 22
  public_access = false
}
