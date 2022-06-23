from PIL import Image
import numpy as np
import math
import os

reference_link_basename = 'pg.jpg'
reference_link = os.path.join(os.getcwd(), reference_link_basename)


def create_submatrix(path, upper_row, lower_row, left_col, right_col, rotate):
    im = Image.open(path).convert('L')
    pix_matrix = np.array(im)

    if rotate == None:
        return np.ndarray.tolist(pix_matrix[upper_row:lower_row, left_col:right_col])
    else:
        return np.ndarray.tolist(np.rot90(pix_matrix[upper_row:lower_row, left_col:right_col], 2))


def create_cuts_new(path,
                    channel):  # РЎРѕР·РґР°РЅРёРµ РјР°С‚СЂРёС†С‹ РёРЅС‚РµРЅСЃРёРІРЅРѕСЃС‚Рё РґР»СЏ РёР·РѕР±СЂР°Р¶РµРЅРёСЏ РЅР° СѓРєР°Р·Р°РЅРЅРѕР№ Р»РёРЅРёРё
    # path - РџРѕР»РЅС‹Р№ РїСѓС‚СЊ Рє РёСЃС…РѕРґРЅРѕРјСѓ РёР·РѕР±СЂР°Р¶РµРЅРёСЋ СЃ РєР°РјРµСЂС‹
    # channel - РґР»РёРЅР° РІРѕР»РЅС‹ РёР·Р»СѓС‡РµРЅРёСЏ РёСЃСЃР»РµРґСѓРµРјРѕРіРѕ РєР°РЅР°Р»Р°
    im = Image.open(path)
    pix_matrix = im.load()

    # Р”Р»СЏ РєР°Р¶РґРѕРіРѕ РєР°РЅР°Р»Р° Р·Р°РґР°СЋС‚СЃСЏ СЂР°Р·РјРµСЂС‹ РІС‹СЂРµР·Р°РµРјРѕРіРѕ РёР·РѕР±СЂР°Р¶РµРЅРёСЏ, РѕРїСЂРµРґРµР»СЏРµРјС‹Рµ РїРѕ СЃРЅРёРјРєСѓ СЃ С‡РµС‚РєРѕ РІРёРґРёРјС‹РјРё РіСЂР°РЅРёС†Р°РјРё
    if str(channel) == '728':
        left = 219
        right = 533
        top = 17
        bot = 331
        key = 0
    if str(channel) == '706':
        left = 673
        right = 946
        top = 54
        bot = 339
        key = 1
    if str(channel) == '667':
        left = 673
        right = 958
        top = 471
        bot = 764
        key = 0
    if str(channel) == '720':
        left = 237
        right = 516
        top = 486
        bot = 760
        key = 1

    # Р’С‹СЂРµР·Р°РЅРЅРѕРµ РёР·РѕР±СЂР°Р¶РµРЅРёРµ Р·Р°РїРёСЃС‹РІР°РµС‚СЃСЏ РІ РјР°С‚СЂРёС†Сѓ СЃРѕРѕС‚РІРµС‚СЃС‚РІСѓСЋС‰РµРіРѕ СЂР°Р·РјРµСЂР° Рё РїСЂРё РЅРµРѕР±С…РѕРґРёРјРѕСЃС‚Рё (key == 1) РїРµСЂРµРІРѕСЂР°С‡РёРІР°РµС‚СЃСЏ РЅР° 180 РіСЂР°РґСѓСЃРѕРІ
    if key == 0:
        return create_submatrix(path, top, bot, left, right, None)
    else:
        return create_submatrix(path, top, bot, left, right, 'rotate')


def create_sub_cuts_VS(path, channel):
    delta_rows = 140
    delta_cols = 140
    drows = 200
    dcols = 200
    if str(channel) == '728':
        left = 230 + drows
        right = left + delta_cols
        top = 10 + drows
        bot = top + delta_rows
    if str(channel) == '706':
        left = 640
        right = left + delta_cols
        top = 0
        bot = top + delta_rows
    if str(channel) == '667':
        left = 650 + drows
        right = left + delta_cols
        top = 450 + drows
        bot = top + delta_rows

    return [create_submatrix(path, top, bot, left, right, None), top, left]


def K(t):
    coef = 0.3708159  # Р’ РѕРїРёСЃР°РЅРёРё С„СѓРЅРєС†РёРё ksmooth РІ Mathcad РїСЂРёРІРµРґРµРЅ РЅРµРїРѕР»РЅС‹Р№ РєРѕСЌС„С„РёС†РёРµРЅС‚: 0.37 -> coeff
    return (math.exp(-(t ** 2) / (2 * coef ** 2)) / (math.sqrt(2 * math.pi) * coef))


def ksmooth(vx, vy, b):
    # vx is a vector of real numbers with elements in ascending order
    # vy is a vector of real numbers the same length as vx
    # b is the bandwidth of the smoothing window
    vec = [0 for i in range(len(vx))]
    for i in range(len(vx)):
        sum1 = 0
        sum2 = 0
        for j in range(len(vx)):
            sum1 += K((vx[i] - vx[j]) / b) * vy[j]
            sum2 += K((vx[i] - vx[j]) / b)
        vec[i] = sum1 / sum2
    return vec


def find_channel_edge_points(I1, I2, I3, visualize):
    delta_rows = 140
    delta_cols = 140
    drows = 200
    dcols = 200

    S1r = [0 for i in range(delta_rows)]
    S2r = [0 for i in range(delta_rows)]
    S3r = [0 for i in range(delta_rows)]
    S1c = [0 for i in range(delta_cols)]
    S2c = [0 for i in range(delta_cols)]
    S3c = [0 for i in range(delta_cols)]
    i_ = [i for i in range(delta_rows)]
    j_ = [i for i in range(delta_cols)]

    for i in range(delta_rows):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for j in range(delta_cols):
            sum1 += I1[i][j]
            sum2 += I2[i][j]
            sum3 += I3[i][j]
        S1c[i] = sum1
        S2c[i] = sum2
        S3c[i] = sum3

    for j in range(delta_cols):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(delta_rows):
            sum1 += I1[i][j]
            sum2 += I2[i][j]
            sum3 += I3[i][j]
        S1r[j] = sum1
        S2r[j] = sum2
        S3r[j] = sum3

    # win_size = 41
    # pol_order = 4
    # S1rm = signal.savgol_filter(S1r, win_size, pol_order)
    # S2rm = signal.savgol_filter(S2r, win_size, pol_order)
    # S3rm = signal.savgol_filter(S3r, win_size, pol_order)
    # S1cm = signal.savgol_filter(S1c, win_size, pol_order)
    # S2cm = signal.savgol_filter(S2c, win_size, pol_order)
    # S3cm = signal.savgol_filter(S3c, win_size, pol_order)
    win_size = 5  # Filter size
    S1rm = ksmooth(j_, S1r, win_size)
    S2rm = ksmooth(j_, S2r, win_size)
    S3rm = ksmooth(j_, S3r, win_size)
    S1cm = ksmooth(i_, S1c, win_size)
    S2cm = ksmooth(i_, S2c, win_size)
    S3cm = ksmooth(i_, S3c, win_size)

    dS1r = [0 for i in range(len(S1r) - 1)]
    dS2r = [0 for i in range(len(S2r) - 1)]
    dS3r = [0 for i in range(len(S3r) - 1)]
    dS1c = [0 for i in range(len(S1c) - 1)]
    dS2c = [0 for i in range(len(S2c) - 1)]
    dS3c = [0 for i in range(len(S3c) - 1)]

    for i in range(len(dS1r)):
        dS1r[i] = S1rm[i] - S1rm[i + 1]
        dS2r[i] = S2rm[i + 1] - S2rm[i]
        dS3r[i] = S3rm[i] - S3rm[i + 1]
    for i in range(len(dS1c)):
        dS1c[i] = S1cm[i] - S1cm[i + 1]
        dS2c[i] = S2cm[i + 1] - S2cm[i]
        dS3c[i] = S3cm[i] - S3cm[i + 1]

    peak_displacement1 = [max(dS1r), max(dS1c)]
    peak_displacement2 = [max(dS2r), max(dS2c)]
    peak_displacement3 = [max(dS3r), max(dS3c)]
    peak_coord1 = [0, 0]
    peak_coord2 = [0, 0]
    peak_coord3 = [0, 0]

    for i in range(len(dS1r)):
        if dS1r[i] == peak_displacement1[0]:
            peak_coord1[1] = i
        if dS2r[i] == peak_displacement2[0]:
            peak_coord2[1] = i
        if dS3r[i] == peak_displacement3[0]:
            peak_coord3[1] = i

    for i in range(len(dS1c)):
        if dS1c[i] == peak_displacement1[1]:
            peak_coord1[0] = i
        if dS2c[i] == peak_displacement2[1]:
            peak_coord2[0] = i
        if dS3c[i] == peak_displacement3[1]:
            peak_coord3[0] = i

    return [peak_coord1, peak_coord2, peak_coord3]


def create_cuts_moving(path, point, channel):
    im = Image.open(path)
    pix = im.load()

    if str(channel) == '728':
        width = 315
        height = 315
    if str(channel) == '706':
        width = 274
        height = 286
    if str(channel) == '667':
        width = 286
        height = 294

    matr = [[0 for j in range(width)] for i in range(height)]

    if str(channel) == '728' or str(channel) == '667':
        # print('channel =', str(channel), point[1] - width, point[0] - height)
        for i in range(height):
            for j in range(width):
                matr[i][j] = pix[j + point[1] - width, i + point[0] - height]
        return matr
    if str(channel) == '706':
        # print('channel =', str(channel), point[1] + width, point[0] + height)
        for i in range(height):
            for j in range(width):
                matr[i][j] = pix[j + point[1], i + point[0]]
        add1 = tuple(zip(*matr[::-1]))  # РџРѕРІРѕСЂРѕС‚ РЅР° 90 РіСЂР°РґСѓСЃРѕРІ
        return tuple(zip(*add1[::-1]))  # Р•С‰Рµ РѕРґРёРЅ РїРѕРІРѕСЂРѕС‚ РЅР° 90 РіСЂР°РґСѓСЃРѕРІ


def max_el(matr):
    m = -1e18
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] > m:
                m = matr[i][j]
    return m


def capillar_position(I3):
    matr = [[0 for j in range(40)] for i in range(90)]
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            matr[i][j] = I3[i + 20][j]
    dI3 = matr - np.mean(matr)
    a = max_el(dI3)
    i_list = []
    j_list = []
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if dI3[i][j] == a:
                i_list.append(i + 20)
                j_list.append(j)
    if 0:
        fig3 = Image.new('L', [len(matr[0]), len(matr)], color=0)
        fig3_ = ImageDraw.Draw(fig3)
        for i in range(len(matr[0])):
            for j in range(len(matr)):
                fig3_.point([i, j], matr[j][i])
        fig3.show()

    return [i_list, j_list]


def capillar_shifts(matr_728, matr_706, matr_667):
    reference_image = reference_link
    [I1, top1, left1] = create_sub_cuts_VS(reference_image, 728)
    [I2, top2, left2] = create_sub_cuts_VS(reference_image, 706)
    [I3, top3, left3] = create_sub_cuts_VS(reference_image, 667)

    [a, b, c] = find_channel_edge_points(I1, I2, I3, visualize=False)
    ref_728 = create_cuts_moving(reference_image, [top1 + a[0], left1 + a[1]], 728)
    ref_706 = create_cuts_moving(reference_image, [top2 + b[0], left2 + b[1]], 706)
    ref_667 = create_cuts_moving(reference_image, [top3 + c[0], left3 + c[1]], 667)
    # print(top1 + discharge_coord1[0] - dwin, top1 + discharge_coord1[0], left1 + discharge_coord1[1] - dwin - 15, left1 + discharge_coord1[1])
    # print(top1 + discharge_coord1[0] - dwin + 20, top1 + discharge_coord1[0] - dwin + 110, left1 + discharge_coord1[1] - dwin - 15, left1 + discharge_coord1[1] - dwin + 45)
    # print(top2 + discharge_coord2[0] + dwin, top2 + discharge_coord2[0], left2 + discharge_coord2[1] + dwin, left2 + discharge_coord2[1])
    # print(top2 + discharge_coord2[0] + dwin - 20, top2 + discharge_coord2[0] + dwin - 110, left2 + discharge_coord2[1] + dwin, left2 + discharge_coord2[1] + dwin - 60)
    # print(top3 + discharge_coord3[0] - dwin, top3 + discharge_coord3[0], left3 + discharge_coord3[1] - dwin, left3 + discharge_coord3[1])
    # print(top3 + discharge_coord3[0] - dwin + 20, top3 + discharge_coord3[0] - dwin + 110, left3 + discharge_coord3[1] - dwin, left3 + discharge_coord3[1] - dwin + 60)

    [list1i, list1j] = capillar_position(ref_728)
    # print(list1i[0], list1j[0]) #capillar position within ref_728 image from top left corner
    # print(list1i[0] + top1 + a[0] - 315, list1j[0] + left1 + a[1] - 315) #capillar position within whole image from top left corner
    # print('**')

    [list2i, list2j] = capillar_position(ref_706)
    # print(list2i[0], list2j[0]) #capillar position within ref_706 image from top left corner
    # print(-list2i[0] + top2 + b[0] + 286, -list2j[0] + left2 + b[1] + 274) #capillar position within whole image from top left corner
    # print('**')

    [list3i, list3j] = capillar_position(ref_667)
    # print(list3i[0], list3j[0]) #capillar position within ref_667 image from top left corner
    # print(list3i[0] + top3 + c[0] - 294, list3j[0] + left3 + c[1] - 286) #capillar position within whole image from top left corner
    # print('**')

    [list4i, list4j] = capillar_position(matr_667)
    # print(list4i[0], list4j[0]) #capillar position within ref_667 image from top left corner
    # print(list4i[0] + top4 + c[0] - 294, list3j[0] + left3 + c[1] - 286) #capillar position within whole image from top left corner
    # print('**')

    ref_shift = [list4i[0] - list3i[0], list4j[0] - list3j[0]]

    return [[list1i[0] + ref_shift[0], list1j[0] + ref_shift[1]], [list2i[0] + ref_shift[0] + ref_shift[1], list2j[0]],
            [list4i[0], list4j[0]]]


def capillar_shifts1():
    [I1, top1, left1] = create_sub_cuts_VS(reference_link, 728)
    [I2, top2, left2] = create_sub_cuts_VS(reference_link, 706)
    [I3, top3, left3] = create_sub_cuts_VS(reference_link, 667)

    dwin = 280
    [discharge_coord1, discharge_coord2, discharge_coord3] = find_channel_edge_points(I1, I2, I3, visualize=False)
    # print(discharge_coord1, top1 - dwin + discharge_coord1[0], top1 + discharge_coord1[0], left1 - dwin + discharge_coord1[1] - 15, left1 + discharge_coord1[1])
    # print(discharge_coord2, top2 + discharge_coord2[0], top2 + discharge_coord2[0] + dwin, left2 + discharge_coord2[1], left2 + discharge_coord2[1] + dwin)
    # print(discharge_coord3, top3 - dwin + discharge_coord3[0], top3 + discharge_coord3[0], left3 - dwin + discharge_coord3[1], left3 + discharge_coord3[1])

    m1 = create_submatrix(reference_link,
                          top1 - dwin + discharge_coord1[0], top1 + discharge_coord1[0],
                          left1 - dwin + discharge_coord1[1] - 15, left1 + discharge_coord1[1], None)
    # WRITEPRN(m1, r'E:\PhD_study\He_monitor\He_image_processing\a1.txt')
    [list1i, list1j] = capillar_position(m1)
    # print(list1i[0], list1j[0])

    m2 = create_submatrix(reference_link,
                          top2 + discharge_coord2[0], top2 + discharge_coord2[0] + dwin, left2 + discharge_coord2[1],
                          left2 + discharge_coord2[1] + dwin, 'rotate')
    # WRITEPRN(m2, r'E:\PhD_study\He_monitor\He_image_processing\a2.txt')
    [list2i, list2j] = capillar_position(m2)
    # print(list2i[0], list2j[0])

    m3 = create_submatrix(reference_link,
                          top3 - dwin + discharge_coord3[0], top3 + discharge_coord3[0],
                          left3 - dwin + discharge_coord3[1], left3 + discharge_coord3[1], None)
    # WRITEPRN(m3, r'E:\PhD_study\He_monitor\He_image_processing\a3.txt')
    [list3i, list3j] = capillar_position(m3)
    # print(list3i[0], list3j[0])

    return [[list1i[0], list1j[0]], [list2i[0], list2j[0]], [list3i[0], list3j[0]]]


def im_shift(cap1, cap2, cap3, matr1, matr2, matr3, matr4):
    min_x = min(cap1[0], cap2[0], cap3[0])
    min_y = min(cap1[1], cap2[1], cap3[1])

    shift_1x = cap1[0] - min_x
    shift_1y = cap1[1] - min_y

    shift_2x = cap2[0] - min_x
    shift_2y = cap1[1] - min_y

    shift_3x = cap3[0] - min_x
    shift_3y = cap1[1] - min_y

    shift_4x = shift_2x
    shift_4y = shift_2y

    width1 = len(matr1[0]) - shift_1y
    height1 = len(matr1) - shift_1x
    width2 = len(matr2[0]) - shift_2y
    height2 = len(matr2) - shift_2x
    width3 = len(matr3[0]) - shift_3y
    height3 = len(matr3) - shift_3x
    width4 = len(matr4[0]) - shift_4y
    height4 = len(matr4) - shift_4x
    width_ = min(width1, width2, width3, width4)
    height_ = min(height1, height2, height3, height4)
    width = min(width_, height_)
    height = min(width_, height_)

    dpix = 245  # pixels
    lamp_diam = 0.130  # m
    R_cap = 0.240  # m
    Z_cap = -0.510  # m
    R_real_cap = 1.09576
    Z_real_cap = 0.26447
    phi = 47.36 * math.pi / 180
    phi_Z = math.atan(
        (Z_real_cap - Z_cap) / math.sqrt(R_cap ** 2 + R_real_cap ** 2 - 2 * R_cap * R_real_cap * math.cos(phi)))
    phi_R = (math.pi / 2) - phi
    length_per_pixel_R = lamp_diam / dpix / math.cos(phi_R)
    length_per_pixel_Z = lamp_diam / dpix / math.cos(phi_Z)
    R = [[0 for j in range(width)] for i in range(height)]
    Z = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            R[i][j] = R_cap + (i - min_x) * length_per_pixel_R
            Z[i][j] = Z_cap + (j - min_y) * length_per_pixel_Z

    m1 = [[0 for j in range(width)] for i in range(height)]
    m2 = [[0 for j in range(width)] for i in range(height)]
    m3 = [[0 for j in range(width)] for i in range(height)]
    m4 = [[0 for j in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            m1[i][j] = matr1[i + shift_1x][j + shift_1y]
            m2[i][j] = matr2[i + shift_2x][j + shift_2y]
            m3[i][j] = matr3[i + shift_3x][j + shift_3y]
            m4[i][j] = matr4[i + shift_4x][j + shift_4y]
    return [m1, m2, m3, m4, R, Z, [min_x, min_y]]
