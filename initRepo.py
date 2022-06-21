#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv

load_dotenv()

GH_TOKEN = os.getenv('GH_TOKEN')

# get the current directory name to use it as repo name
folderName = os.path.basename(os.getcwd())

print("creating repository...")

API_URL = "https://api.github.com"
payload = '{"name": "' + folderName + '"}'
headers = {
    "Authorization": "token " + GH_TOKEN,
    "Accept": "application/vnd.github.v3+json",
}

try:
    res = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
    res.raise_for_status()

except requests.exceptions.RequestException as err:
    raise SystemExit(err)

print("Successfully created repository: " + folderName)

print("initializing repository...")

url = res.json()["clone_url"]

os.system("git init")
os.system("git remote add origin " + url)

try:
    md = open("README.md", "x")
    # md.write("# " + folderName)
    md.close()
except:
    print("README.md already exists")

os.system("git add .")
os.system('git commit -m "Initial commit"')
os.system("git branch -M main")
os.system("git push -u origin main")