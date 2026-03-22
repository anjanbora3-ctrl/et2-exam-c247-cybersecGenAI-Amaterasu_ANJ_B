resource "aws_rds" "example_140" {
  name = "infrastructure_140.tf"
  port = 3306
  public_access = false
}
