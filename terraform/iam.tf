data "aws_iam_policy_document" "lambda_assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "lambda_role" {
  name               = "lambda_execution_role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json
}

data "aws_iam_policy_document" "lambda_dynamo_permissions" {
  statement {
    effect = "Allow"
    actions = [
      "dynamodb:PutItem",
      "dynamodb:Query"
    ]
    resources = [aws_dynamodb_table.dynamodb_table.arn]
  }
}

resource "aws_iam_role_policy" "lambda_dynamodb_policy" {
  name   = "lambda-dynamodb-policy"
  role   = aws_iam_role.lambda_role.id
  policy = data.aws_iam_policy_document.lambda_dynamo_permissions.json
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_permission" "apigw_invoke_1" {
  statement_id  = "AllowAPIGatewayInvoke_SaveReview"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.save_review_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api_gateway.execution_arn}/*"
}

resource "aws_lambda_permission" "apigw_invoke_2" {
  statement_id  = "AllowAPIGatewayInvoke_GetReviews"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.get_reviews_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api_gateway.execution_arn}/*"
}
