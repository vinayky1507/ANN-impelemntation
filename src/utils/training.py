from src.utils.common import read_config
import argparse

def training (config_path):
    config=read_config(config_path)


if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args