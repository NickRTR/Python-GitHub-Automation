# GitHub Automation

## Installation:

Python is required to be installed on your machine.

1. clone repo to some location on your machine `git clone "https://github.com/NickRTR/GitHub-Automation.git"`
2. `cd GitHub-Automation`
3. pip install python-dotenv
3. Create a GitHub access token with repo access
4. Create and open `.env` and enter your token as following `GH_TOKEN=YOURTOKEN`
5. Add `initRepo.py` to your environment variables (see further down)

## Add script to env variables

### Windows
1. Search for environment variables
2. Select edit environment variables
3. In the Tab "Advanced" select "environment variables"
4. Select the variable "PATH" and double click on its value
4. Add the path which leads to the `initRepo.py` script

## Usage:

1. `py initRepo`

## Links

https://docs.github.com/en/rest/repos/repos


## Todos

TODO: Add arguments for private/public
TODO: Add argument for other repo name than directory name
