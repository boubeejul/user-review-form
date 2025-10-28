data "archive_file" "zip_save_review" {
  type        = "zip"
  source_file = "../api/save_review.py"
  output_path = "../api/save_review.zip"
}

resource "aws_lambda_function" "save_review_lambda" {
  filename         = data.archive_file.zip_save_review.output_path
  function_name    = "SaveUserReview"
  role             = aws_iam_role.lambda_role.arn
  handler          = "save_review.handler"
  source_code_hash = data.archive_file.zip_save_review.output_base64sha256

  runtime = "python3.9"

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.dynamodb_table.name
    }
  }
}