import json
from dataclasses import dataclass
from pathlib import Path
from typing import List
@dataclass
class AppConfig:
    tmp_dir: List[str]
    """Temp direct such as ["tmp"]"""
    inc_dir: List[str]
    """inlude dir such as ["resources", "include"]"""
    stickytape: List[str]
    """stickytape path such as ["env", "bin", "stickytape"]"""

def read_config(config_file: str) -> AppConfig:
    """
    Gets config for given config file

    Args:
        config_file (str): Config file to load

    Returns:
        AppConfig: Configuration object
    """
    with open(config_file, 'r') as file:
        data = json.load(file)
        return AppConfig(**data)

def read_config_default() -> AppConfig:
    """
    Loads default configuration ``config.json``

    Returns:
        AppConfig: Configuration Object
    """
    root = Path(__file__).parent
    config_file = Path(root, 'config.json')
    return read_config(str(config_file))