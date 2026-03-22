resource "aws_rds" "example_6" {
  name = "infrastructure_6.tf"
  port = 3306
  public_access = true
}
