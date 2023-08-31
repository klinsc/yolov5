# count total number of instances of each classes in the dataset of YOLOv5 format
# which consists of .txt files with each line containing class number and bounding box coordinates in folder labels
# and the class names are in the file classes.txt in the root folder
# Usage: python count.py --dir <path to data folder>

# yaml format
# path: ./datasets/rpod6  # dataset root dir
# train: images  # train images (relative to 'path') 128 images
# val: images  # val images (relative to 'path') 128 images
# test:  # test images (optional)

# # Classes
# names:
#   0: 11522_tx_dyn1
#   1: 11522_tx_ynyn0d1
#   2: 115_1way_ds_w_motor
#   3: 115_3ways_ds
#   4: 115_3ways_ds_w_motor
#   5: 115_breaker
#   6: 115_buffer
#   7: 115_cvt_1p
#   8: 115_cvt_3p
#   9: 115_ds
#   10: 115_gs
#   11: 115_gs_w_motor
#   12: 115_la
#   13: 115_vt_1p
#   14: 115_vt_3p
#   15: 22_breaker
#   16: 22_cap_bank
#   17: 22_ds
#   18: 22_ds_out
#   19: 22_ds_la_out
#   20: 22_gs
#   21: 22_ll
#   22: 22_vt_1p
#   23: 22_vt_3p
#   24: BCU
#   25: DIM
#   26: DPM
#   27: LL
#   28: MU
#   29: NGR
#   30: NGR_future
#   31: Q
#   32: remote_io_module
#   33: ss_man_mode
#   34: tele_protection
#   35: terminator_double
#   36: terminator_single
#   37: terminator_splicing_kits
#   38: terminator_w_future
#   39: v_m
#   40: v_m_digital

import os
import argparse
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Count total number of instances of each classes in the dataset of YOLOv5 format')
    parser.add_argument('--dir', help='path to data folder', type=str, required=True)
    args = parser.parse_args()
    return args


def save_class_count(class_count, classes, save_path):
    with open(os.path.join(save_path, 'class_count.txt'), 'w') as f:
        for i in range(len(classes)):
            f.write('{}: {}\n'.format(classes[i], class_count[i]))


def save_class_as_yaml(class_count, classes, save_path):
    with open(os.path.join(save_path, 'classes.yaml'), 'w') as f:
        # f.write('path: ./datasets/rpod6  # dataset root dir\n')
        f.write(f'path: {save_path}  # dataset root dir\n')
        f.write('train: images  # train images (relative to \'path\') 128 images\n')
        f.write('val: images  # val images (relative to \'path\') 128 images\n')
        f.write('test:  # test images (optional)\n')
        f.write('\n')
        f.write('# Classes\n')
        f.write('names:\n')
        for i in range(len(classes)):
            f.write('  {}: {}\n'.format(i, classes[i]))


def main():
    args = parse_args()
    data_path = args.dir
    classes = []
    with open(os.path.join(data_path, 'classes.txt'), 'r') as f:
        for line in f:
            classes.append(line.strip())
    print('classes: ', classes)
    class_count = np.zeros(len(classes), dtype=np.int32)
    for file in os.listdir(os.path.join(data_path, 'labels')):
        with open(os.path.join(data_path, 'labels', file), 'r') as f:
            for line in f:
                class_count[int(line.strip().split()[0])] += 1
    print('class_count: ', class_count)

    save_class_count(class_count, classes, data_path)
    save_class_as_yaml(class_count, classes, data_path)

if __name__ == '__main__':
    main()
