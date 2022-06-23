import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = ROOT_PATH.replace("/utils", "")

ai_path = os.path.join(ROOT_PATH, "ai")
api_path = os.path.join(ROOT_PATH, "api")
utils_path = os.path.join(ROOT_PATH, "utils")
dataset_path = os.path.join(ROOT_PATH, "dataset")
