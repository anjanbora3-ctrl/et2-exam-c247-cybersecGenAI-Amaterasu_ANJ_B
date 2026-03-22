resource "aws_rds" "example_5" {
  name = "infrastructure_5.tf"
  port = 25
  public_access = false
}
