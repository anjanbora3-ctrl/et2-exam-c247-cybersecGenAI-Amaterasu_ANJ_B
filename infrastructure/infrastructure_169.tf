resource "aws_vm" "example_169" {
  name = "infrastructure_169.tf"
  port = 25
  public_access = false
}
