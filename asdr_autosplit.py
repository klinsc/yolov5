# do autosplit of a image dataset
# usage: python asdr_autosplit.py <dataset_dir> <output_dir,optional> <split_ratio,optional>

import os
import sys

from utils.dataloaders import *


def parse_args():
    if len(sys.argv) < 1:
        print(
            "usage: python asdr_autosplit.py <dataset_dir> <(Train, val, test weights),optional>"
        )
        # weights:         Train, val, test weights (list, tuple)
        sys.exit(1)
    dataset_dir = sys.argv[1]
    split_ratio = float(sys.argv[3]) if len(sys.argv) > 3 else 0.2
    return dataset_dir, split_ratio


def main():
    dataset_dir, split_ratio = parse_args()
    autosplit(dataset_dir, split_ratio)
