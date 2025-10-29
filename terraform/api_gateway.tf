resource "aws_apigatewayv2_api" "api_gateway" {
  name                      = "user-review-api"
  protocol_type             = "HTTP"

  cors_configuration {
    allow_origins = ["*"]                   
    allow_methods = ["GET", "POST"]
    allow_headers = ["*"]
    max_age       = 3600
  }
}

resource "aws_apigatewayv2_integration" "save_review_integration" {
  api_id                    = aws_apigatewayv2_api.api_gateway.id
  integration_type          = "AWS_PROXY"

  description               = "Lambda SaveUserReview"
  integration_uri           = aws_lambda_function.save_review_lambda.invoke_arn
}

resource "aws_apigatewayv2_integration" "get_reviews_integration" {
  api_id                    = aws_apigatewayv2_api.api_gateway.id
  integration_type          = "AWS_PROXY"

  description               = "Lambda GetUsersReviews"
  integration_uri           = aws_lambda_function.get_reviews_lambda.invoke_arn
}

resource "aws_apigatewayv2_stage" "default" {
  api_id                    = aws_apigatewayv2_api.api_gateway.id
  name                      = "$default"
  auto_deploy               = true
}

resource "aws_apigatewayv2_route" "save_review_route" {
  api_id                    = aws_apigatewayv2_api.api_gateway.id
  route_key                 = "POST /reviews"
  target                    = "integrations/${aws_apigatewayv2_integration.save_review_integration.id}"
}

resource "aws_apigatewayv2_route" "get_reviews_route" {
  api_id                    = aws_apigatewayv2_api.api_gateway.id
  route_key                 = "GET /reviews"
  target                    = "integrations/${aws_apigatewayv2_integration.get_reviews_integration.id}"
}