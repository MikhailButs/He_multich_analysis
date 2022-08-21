import numpy as np


class dataCore():
    def __init__(self):
        super().__init__()

        # images
        self.images_dir = ''
        self.got_images_dir = ''
        self.images_list = []
        self.exposure = 0
        self.interval = 0
        self.trigger = 0
        self.ChType = 'three'  # 'one' or 'three'
        self.ShowFrames = False  # True or False
        self.intensity_list = []
        self.init_pic_list = []
        self.init_flt_pic_list = []
        self.diff_pic_list = []
        self.final_pic_list = []
        self.time_list = []
        self.frames_list = []
        self.int1 = np.array([])
        self.int1_scaled = np.array([])
        self.int2 = np.array([])
        self.int2_scaled = np.array([])
        self.int3 = np.array([])
        self.int3_scaled = np.array([])

        # sht
        self.sht_dir = ''
        self.sht_num = ''
        self.sht_file = ''
        self.sht_data = {}
        self.got_sht_file = ''
        self.Dalpha_x = np.array([])
        self.Dalpha_x_frames = []
        self.Dalpha_y = np.array([])
        self.Dalpha_y_scaled = np.array([])
        self.NII_x = np.array([])
        self.NII_x_frames = []
        self.NII_y = np.array([])
        self.NII_y_scaled = np.array([])
        self.He_x = np.array([])
        self.He_x_frames = []
        self.He_y = np.array([])
        self.He_y_scaled = np.array([])
