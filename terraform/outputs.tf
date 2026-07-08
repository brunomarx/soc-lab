output "trail_arn" {
  value = aws_cloudtrail.main.arn
}

output "log_bucket" {
  value = aws_s3_bucket.logs.id
}

output "guardduty_detector" {
  value = aws_guardduty_detector.main.id
}
