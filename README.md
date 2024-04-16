# Shopping List Interpreter

# How to use Python and virtual environments

## Python version management _pyenv_

Install the latest (1.4.2024) Python3 version: `pyenv install 3.12.1`
Take the latest version into use: `pyenv local 3.12.1`. This creates a file `.python-version` to the project root. When someone navigates to the folder which invludes the file and pyenv is installed it should automatically change to the correct Python version.

## Poetry

### Create new poetry project

`poetry new {appname}`. This creates folder structure and needed pyproject.tolm and lock files

### Install packages

`poetry add {packagename}`

### Virtual env (poetry)

Poetry has it's own virtual environment and it's started using command `poetry shell`. `exit` command closes the virtual environment.

## CI

In some cases CI uses pip not poetry and then we need to add packages to requirements.txt as well

- After installation update requirements.txt using command: `pip freeze > requirements.txt`
- Later install packages using command: `pip install -r requirements.txt`

# Testing (using poetry virtaul env)

Start the server inside the `app` folder by command `poetry run python app/server.py` and the server will start at port 3000.

To use the [test_calls.rest](test_calls.rest) the VSCode needs the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension.

# Running locally

1. Create an account to [todoist](https://app.todoist.com/) and go to your profile => settings => integrations => developer -> copy API KEY
2. Create .env file and add `TODOIST_API_KEY=API KEY` from the todoist
3. Create a project with name: `shopping-list`
4.
