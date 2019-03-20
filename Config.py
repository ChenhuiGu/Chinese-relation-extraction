import os

base_dir = os.path.split(os.path.realpath(__file__))[0]

CN_DATA = base_dir + '/data/cndata/'
ORIGIN_DATA = base_dir + '/origindata/'
TRAIN_DATA = ORIGIN_DATA + '/train_data/'