resource "aws_vm" "example_100" {
  name = "infrastructure_100.tf"
  port = 3306
  public_access = false
}
