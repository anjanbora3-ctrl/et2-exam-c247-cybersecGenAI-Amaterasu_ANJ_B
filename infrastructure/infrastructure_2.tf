resource "aws_vm" "example_2" {
  name = "infrastructure_2.tf"
  port = 8080
  public_access = true
}
