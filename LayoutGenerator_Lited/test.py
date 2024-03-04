from __future__ import print_function
import os
import sys
import pprint
import random
import time
import datetime
import argparse
import dateutil.tz
import torch
import torchvision.transforms as transforms
# from miscc.config import cfg, cfg_from_file
# config environment
from easydict import EasyDict as edict

import yaml

with open('cfg/layout.yml', 'r') as f:
    cfg = edict(yaml.load(f, Loader=yaml.FullLoader))

dir_path = (os.path.abspath(os.path.join(os.path.realpath(__file__), './.')))
sys.path.append(dir_path)

now = datetime.datetime.now(dateutil.tz.tzlocal())
timestamp = now.strftime('%Y_%m_%d_%H_%M_%S')
output_dir = '../output_bbox_gcn/%s_%s_%s' % \
             (cfg.DATASET_NAME, cfg.CONFIG_NAME, timestamp)

print(output_dir)
