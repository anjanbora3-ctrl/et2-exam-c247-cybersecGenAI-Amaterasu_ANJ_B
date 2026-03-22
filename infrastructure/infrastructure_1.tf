resource "aws_ec2" "example_1" {
  name = "infrastructure_1.tf"
  port = 25
  public_access = true
}
