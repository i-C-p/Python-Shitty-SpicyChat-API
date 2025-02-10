import requests
import os

from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from dotenv import load_dotenv

load_dotenv()
disable_warnings(InsecureRequestWarning)

auth = os.getenv("AUTH")
char_id = os.getenv("CHAR_ID")
conv_id = os.getenv("CONV_ID")

class spicy:
    def __init__(self,url="https://spicychat.ai/"):
        self.url = url
    def fetch_page(self):
        response = requests.get(self.url, verify=False)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
            
  
    def username(self, username:str):
    soup = self.fetch_page()
    if soup:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth}"
        }
        payload = {
            "username": username
        }
        api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/users"
        response = requests.patch(api_url, headers=headers, json=payload, verify=False)
        
        # Debugging the response
        print(f"API Response Status: {response.status_code}")
        print(f"API Response JSON: {response.json()}")  # Add this to see what the API returns
        
        data = response.json()
        return data.get("username", "Username key not found in response")  # Use .get() to prevent KeyError
    else:
        print("URL not found")


    def name(self, name:str):
        soup = self.fetch_page()
        if soup:
            headers ={
                ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth}"
            }
            payload = {
                "name": name
            }
            api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/users"
            response = requests.patch(api_url, headers=headers, json=payload, verify = False)
            data = response.json()
            return data["name"]
        else:
            print("url not found") 

    def highlights(self, highlights:str):
        soup = self.fetch_page()
        if soup:
            headers ={
                ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth}"
            }
            payload = {
                "highlights": highlights
            }
            api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/users"
            response = requests.patch(api_url, headers=headers, json=payload, verify = False)
            data = response.json()
            return data["highlights"]
        else:
            print("url not found")

    #BOT
    def bot_name(self,name:str):
        soup = self.fetch_page()
        if soup:
            headers ={
                ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth}"
            }
            payload = {
                "name": name
            }
            api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
            response = requests.patch(api_url, headers=headers, json=payload, verify = False)
            data = response.json()
            return data["name"]
        else:
            print("url not found")
    def greeting(self, greeting:str):
        soup = self.fetch_page()
        if soup:
            headers ={
                ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth}"
            }
            payload = {
                "greeting": greeting
            }
            api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
            response = requests.patch(api_url, headers=headers, json=payload, verify = False)
            data = response.json()
            return data["greeting"]
        else:
            print("url not found")
    def title(self, title:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "title": title
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                return data["title"]
            else:
                print("url not found")

    def visibility(self, visibility:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "visibility": visibility
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                print(data)
            else:
                print("url not found")

    def persona(self, persona:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "persona": persona
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                return data["persona"]
            else:
                print("url not found")
    def avatar_url(self, avatar_url:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "avatar_url": avatar_url
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                return data["avatar_url"]
            else:
                print("url not found")
    def openai_api_key_url(self, openai_api_key:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "openai_api_key": openai_api_key
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                return data["openai_api_key"]
            else:
                print("url not found")
    def openai_mode(self, openai_mode:str):
            soup = self.fetch_page()
            if soup:
                headers ={
                    ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth}"
                }
                payload = {
                    "openai_mode": openai_mode
                }
                api_url = "https://4mpanjbsf6.execute-api.us-east-1.amazonaws.com/v2/characters/e6bbfac2-13ee-434b-8912-a77bedc911b3?switch=T1"
                response = requests.patch(api_url, headers=headers, json=payload, verify = False)
                data = response.json()
                return data["openai_mode"]
            else:
                print("url not found")
    #MESSAGE
    def send_message(self, message:str):
        soup = self.fetch_page()
        if soup:
            headers ={
                ""User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.160 Safari/537.36",
                "Accept": "*/*",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth}"
            }
            payload = {
                "message": message,
                "character_id": char_id,
                "conversation_id": conv_id,


            }
            api_url = "https://chat.nd-api.com/chat"
            response = requests.post(api_url, headers=headers, json=payload, verify = False)
            data = response.json()
            bot_msg = data["message"]["content"]
            return bot_msg
        else:
            print("url not found")
