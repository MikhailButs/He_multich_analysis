import numpy as np


class dataCore():
    def __init__(self):
        super().__init__()

        # images
        self.images_dir = ''
        self.got_images_dir = ''
        self.images_data = {}
        self.intensity_data = {}
        self.images_list = []
        self.exposure = 0
        self.interval = 0
        self.trigger = 0
        self.ChType = 'three'  # 'one' or 'three'
        self.reference_picture = None
        self.depth = 8

        # sht
        self.sht_dir = ''
        self.sht_num = ''
        self.sht_file = ''
        self.sht_data = {}
        self.got_sht_file = ''
