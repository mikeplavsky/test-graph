import requests as r
import os

tenant = os.environ["AAD_TENANT"]
client_id = os.environ["CLIENT_ID"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

msft = "https://login.microsoftonline.com"
url = f"{msft}/{tenant}/oauth2/v2.0/"
token = f"{url}/token"

res = r.post(token, 
        data=dict(
            grant_type="password",
            client_id=f"{client_id}",
            username=f"{username}",
            password=f"{password}",
            scope="https://graph.microsoft.com/.default"
            ))

access_token = res.json()["access_token"];

users = f"https://graph.microsoft.com/v1.0/users/delta"

res = r.get(users, headers={
            "Content-Type" : "application/json",
            "Authorization" : f"Bearer {access_token}"})

print(res)
print(res.json())



