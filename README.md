# WebAutomatedTestsBackend

# Automated Tests - WebAutomatedTestsBackend

## Table of Contents

1. [Cloning an automated test repository](#cloning-an-automated-test-repository)
2. [Preparation of the web application environment](#preparation-of-the-web-application-environment)
3. [Browser configuration](#browser-configuration)

## Cloning an automated test repository

Clone the **WebAutomatedTestsBackend** repository:

```bash
git clone https://github.com/Wojtalo94/WebAutomatedTestsBackend.git
```

## Preparation of the web application environment

Create a virtual environment (**venv**) along with the installation of additional libraries from the file **requirements.txt**:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Browser configuration

In the `config.yml` file we have:

- configured basic address of the app under test
- the type of browser we want to use for testing
- the configuration in which we want to run the browser

```python
# YAML
base_url: 'https://trello.com/'
browser: 'chrome' # choose 'chrome' or 'firefox' or 'edge'

# test settings
fullscreen: true
incognito: true
```
