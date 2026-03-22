resource "aws_vm" "example_104" {
  name = "infrastructure_104.tf"
  port = 3306
  public_access = false
}
