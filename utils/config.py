import os
import yaml

from utils.path import ROOT_PATH

config_file = os.path.join(ROOT_PATH, "config.yaml")
with open(config_file, "r") as file:
    configs = yaml.load(file, Loader=yaml.FullLoader)
    system_configs = configs['system']
    database_configs = configs['database']

if __name__ == "__main__":
    print("system_configs: ", system_configs)
