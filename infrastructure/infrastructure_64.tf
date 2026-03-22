resource "aws_rds" "example_64" {
  name = "infrastructure_64.tf"
  port = 8080
  public_access = true
}
