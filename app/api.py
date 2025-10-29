import requests
import os

def get_reviews():
    api_url = os.getenv("AWS_API_URL")
    response = requests.get(url=f"{api_url}/reviews")

    response.raise_for_status()
    reviews = response.json()

    return reviews.get("reviews")

def save_review(review: dict):
    api_url = os.getenv("AWS_API_URL")
    response = requests.post(url=f"{api_url}/reviews",
                             json=review)

    response.raise_for_status()

    return response.json().get("message")