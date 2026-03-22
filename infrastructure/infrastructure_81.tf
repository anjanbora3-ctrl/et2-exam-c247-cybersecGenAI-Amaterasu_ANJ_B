resource "aws_rds" "example_81" {
  name = "infrastructure_81.tf"
  port = 6379
  public_access = true
}
