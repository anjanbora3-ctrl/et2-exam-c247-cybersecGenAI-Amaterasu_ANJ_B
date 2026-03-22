resource "aws_vm" "example_3" {
  name = "infrastructure_3.tf"
  port = 25
  public_access = false
}
