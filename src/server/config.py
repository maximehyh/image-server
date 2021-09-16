import os


INPUT_FOLDER = os.getenv('INPUT_FOLDER') if os.getenv(
    'INPUT_FOLDER') else "../assets"
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER') if os.getenv(
    'OUTPUT_FOLDER') else "static/images"
SERVER_PORT = os.getenv('SERVER_PORT') if os.getenv('SERVER_PORT') else 5000
DEBUG = os.getenv('DEBUG') if os.getenv('DEBUG') else True
PATH_FROM_PROC_MOD = "server"
