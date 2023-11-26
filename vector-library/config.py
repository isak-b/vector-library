import os
import yaml

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
default_cfg_path = f"{root_path}/config.yaml"


def load_cfg(path: str = default_cfg_path) -> dict:
    """Load a YAML config file and return a dict"""
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg
