import pathlib
import os
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent

config_filename = os.getenv('CONFIG_FILENAME', 'polls') + '.yaml'
config_path = BASE_DIR / 'config' / config_filename


def get_config():
    with open(config_path) as f:
        _config = yaml.load(f)

    return _config
