#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
import argparse

load_dotenv()

GH_TOKEN = os.getenv('GH_TOKEN')

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', type=str, dest="name")
parser.add_argument('-org', '--organization', type=str, dest="organization")
parser.add_argument('-p', '--private', dest="isPrivate", action="store_true")
args = parser.parse_args()

if (args.name == None):
    # get the current directory name to use it as repo name
    name = os.path.basename(os.getcwd())
else:
    name = args.name

isPrivate = args.isPrivate    

if isPrivate:
    payload = '{"name": "' + name + '", "private": "true"}'
else:
    payload = '{"name": "' + name + '", "private": "false"}'

print("creating repository...")

API_URL = "https://api.github.com"
headers = {
    "Authorization": "token " + GH_TOKEN,
    "Accept": "application/vnd.github.v3+json",
}

if (args.organization == None):
    try:
        res = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
        res.raise_for_status()
        
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
else:
    try:
        res = requests.post(API_URL + "/orgs/" + args.organization + "/repos", data=payload, headers=headers)
        res.raise_for_status()
        
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

print("Successfully created repository: " + name)

print("initializing repository...")

url = res.json()["clone_url"]

os.system("git init")
os.system("git remote add origin " + url)

try:
    with open("README.md", "x") as md:
        md.write("# " + name)
        md.close()
except:
    print("README.md already exists")

os.system("git add .")
os.system('git commit -m "Initial commit"')
os.system("git branch -M main")
os.system("git push -u origin main")