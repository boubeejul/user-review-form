resource "aws_dynamodb_table" "dynamodb_table" {
  name           = "UsersReviews"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "ID"

  attribute {
    name = "ID"
    type = "S"
  }
}