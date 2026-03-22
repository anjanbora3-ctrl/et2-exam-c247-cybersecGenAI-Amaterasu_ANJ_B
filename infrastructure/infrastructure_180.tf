resource "aws_rds" "example_180" {
  name = "infrastructure_180.tf"
  port = 3306
  public_access = true
}
