import requests as r
import os
import json
import random

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
users = f"https://graph.microsoft.com/v1.0/users/"

def patch_user(id,attr,val):

    user = f"{users}/{id}"

    res = r.patch(user, 
            headers={
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {access_token}"},
            data = json.dumps({attr: val}))

    print(res)
    print(res.text)


def patch_all():

    res = r.get(f"{users}", headers={
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {access_token}"})

    objs = res.json()["value"]

    for u in objs:

        id = u["id"]
        job = u["jobTitle"]

        print(f"{id}: {job}")

        patch_user(id, 
                "jobTitle", 
                str(random.randint(0,1000)))


def init_read():

    next_link = f"{users}/delta" 
    while next_link:

        res = r.get(next_link, headers={
                    "Content-Type" : "application/json",
                    "Authorization" : f"Bearer {access_token}"})

        objects = res.json()
        next_link = objects.get("@odata.nextLink", "")

        print(objects)
        print(len(objects["value"]))

        if next_link:

            print("Press Enter.")
            input()



