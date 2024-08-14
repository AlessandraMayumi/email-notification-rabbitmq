#!/usr/bin/env python
import requests
import json
from config import Config

class EmailClient:
    def __init__(self):
        self.api_url = Config.MAIL_API_URL
        self.api_key = Config.MAIL_API_KEY
    
    def _generate_headers(self):
        """Generate headers for the POST request."""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        return headers

    def send_email(self):
        """Send an email using the Mailtrap API."""

        data = {
            'from': {
                'email': Config.MAIL_FROM,
                'name': 'Mailtrap Test'
            },
            'to': [
                {'email': Config.MAIL_TO}
            ],
            'subject': 'You are awesome!',
            'text': 'Congrats for sending test email with Mailtrap!',
            'category': 'Integration Test'
        }
        
        headers = self._generate_headers()
        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
            print("Response:", response.text)
