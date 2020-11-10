import os
import sys

base_path = os.getcwd()
sys.path.append('../')

import yaml


def yaml_load_data():
    with open('../datas/add.yml') as f:
        print(yaml.safe_load(f))
        # return yaml.safe_load(f)


yamld = yaml_load_data()
