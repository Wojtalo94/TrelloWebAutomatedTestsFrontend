import yaml

with open("tools/config.yml", "r") as file:
    config = yaml.safe_load(file)
    BASE_URL = config['base_url']
    BROWSER = config['browser']
    FULLSCREEN = config["fullscreen"]
    INCOGNITO = config["incognito"]
    APP_LOGS = config["app_logs"]
    MAX_WAIT = config["max_wait"]
