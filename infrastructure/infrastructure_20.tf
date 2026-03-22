resource "aws_rds" "example_20" {
  name = "infrastructure_20.tf"
  port = 6379
  public_access = true
}
