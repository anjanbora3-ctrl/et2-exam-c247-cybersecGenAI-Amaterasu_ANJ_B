resource "aws_blobstorage" "example_80" {
  name = "infrastructure_80.tf"
  port = 22
  public_access = false
}
