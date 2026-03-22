resource "aws_vm" "example_7" {
  name = "infrastructure_7.tf"
  port = 6379
  public_access = true
}
