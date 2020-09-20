import requests as r
import os

tenant = os.environ["AAD_TENANT"]
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/"
token = f"{url}/token"

res = r.post(token, 
        data=dict(
            grant_type="client_credentials",
            client_id=f"{client_id}",
            client_secret=f"{client_secret}",
            scope="https://graph.microsoft.com/.default"))

print(res) 
print(res.text) 
