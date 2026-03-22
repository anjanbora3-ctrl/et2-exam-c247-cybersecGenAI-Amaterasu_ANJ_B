resource "aws_vm" "example_42" {
  name = "infrastructure_42.tf"
  port = 21
  public_access = true
}
