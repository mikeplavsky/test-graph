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

access_token = res.json()["access_token"];

users = f"https://graph.microsoft.com/v1.0/users/delta"
next_link = users 

while next_link:

    res = r.get(next_link, headers={
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {access_token}"})

    objects = res.json()
    next_link = objects.get("@odata.nextLink", "")

    print(objects)
    print(len(objects["value"]))

    if next_link:

        print("Press some key.")
        input()



