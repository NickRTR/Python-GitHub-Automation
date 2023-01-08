# Python-GitHub Automation

## Installation:

Python is required to be installed on your machine.

1. clone repo to some location on your machine `git clone https://github.com/NickRTR/GitHub-Automation.git`
2. `cd GitHub-Automation`
3. pip install python-dotenv
3. Create a GitHub access token with repo access
4. Edit the `.env` file and enter your token after `GH_TOKEN=`
5. Make script globally accessible (see further down)

## Globally access script

### Windows

1. Search for environment variables
2. Select edit environment variables
3. In the Tab "Advanced" select "environment variables"
4. Select the variable "PATH" and double click on its value
4. Add the path which leads to the `initRepo.py` script

### Linux

1. Give execution permissions `chmod +x initRepo.py`
2. Add script to environment variables `export PATH="$PATH:<path to initRepo.py>`

### Mac

1. Give execution permissions `chmod 755 initRepo.py`
2. Add script to environment variables `% PATH=<path to initRepo.py> export PATH`

## Usage:

1. Navigate into the folder, you want to create a Repo in
2. `initRepo.py`

If you want to create a private repo, use the `-p` / `--private` flag after `initRepo.py`
If you want to specify a different name than your directory is called, use the `-n` / `--name` flag and your name after `initRepo.py`

## Todos
