resource "aws_vm" "example_101" {
  name = "infrastructure_101.tf"
  port = 6379
  public_access = false
}
