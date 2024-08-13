import requests
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

class EmailClient:
    def __init__(self):
        self.api_url = getenv('API_URL')
        self.api_key = getenv('API_KEY')
    
    def _generate_headers(self):
        """Generate headers for the POST request."""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        return headers

    def send_email(self, from_email, from_name, to_email, subject, text, category):
        """Send an email using the Mailtrap API."""
        data = {
            'from': {
                'email': from_email,
                'name': from_name
            },
            'to': [
                {'email': to_email}
            ],
            'subject': subject,
            'text': text,
            'category': category
        }
        
        headers = self._generate_headers()
        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
            print("Response:", response.text)

# Usage example
if __name__ == "__main__":
    email_client = EmailClient()
    email_client.send_email(
        from_email=getenv('FROM_EMAIL'),
        from_name='Mailtrap Test',
        to_email=getenv('TO_EMAIL'),
        subject='You are awesome!',
        text='Congrats for sending test email with Mailtrap!',
        category='Integration Test'
    )
