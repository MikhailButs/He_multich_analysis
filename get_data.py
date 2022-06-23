from functions_evg import *


def get_data(link):
    path_discharge_image = link

    [I1, top1, left1] = create_sub_cuts_VS(path_discharge_image, 728)  # грубая обрезка
    [I2, top2, left2] = create_sub_cuts_VS(path_discharge_image, 706)
    [I3, top3, left3] = create_sub_cuts_VS(path_discharge_image, 667)

    [a, b, c] = find_channel_edge_points(I1, I2, I3, False) # поиск края канала
    im1_728 = create_cuts_moving(path_discharge_image, [top1 + a[0], left1 + a[1]], 728) # точная образка
    im1_706 = create_cuts_moving(path_discharge_image, [top2 + b[0], left2 + b[1]], 706)
    im1_667 = create_cuts_moving(path_discharge_image, [top3 + c[0], left3 + c[1]], 667)
    im1_720 = create_cuts_new(path_discharge_image, 720)

    # [a, b, c] = capillar_shifts(im1_728, im1_706, im1_667)
    [a, b, c] = capillar_shifts1() # поиск капилляра
    [im_728, im_706, im_667, im_720, R, Z, cap_pos] = im_shift(a, b, c, im1_728, im1_706, im1_667, im1_720) # сдвиг картинки

    im_728 = np.array(im_728)  # convert to np.array
    im_706 = np.array(im_706)
    im_667 = np.array(im_667)

    im_728L = np.zeros((len(im_728), len(im_728[0])))  # initial arrays for L-type pictures
    im_706L = np.zeros((len(im_706), len(im_706[0])))
    im_667L = np.zeros((len(im_667), len(im_667[0])))

    for i in range(len(im_728)):  # manually making L picture from RGB picture (grayscale = 0.299*R + 0.587*G + 0.114*B)
        for j in range(len(im_728[0])):
            im_728L[i][j] = int(round(0.299 * im_728[i][j][0] + 0.587 * im_728[i][j][1] + 0.114 * im_728[i][j][2], 0))
    for i in range(len(im_706)):
        for j in range(len(im_706[0])):
            im_706L[i][j] = int(round(0.299 * im_706[i][j][0] + 0.587 * im_706[i][j][1] + 0.114 * im_706[i][j][2], 0))
    for i in range(len(im_667)):
        for j in range(len(im_667[0])):
            im_667L[i][j] = int(round(0.299 * im_667[i][j][0] + 0.587 * im_667[i][j][1] + 0.114 * im_667[i][j][2], 0))

    intensity_728 = np.sum(im_728L) / np.size(im_728L)
    intensity_706 = np.sum(im_706L) / np.size(im_706L)
    intensity_667 = np.sum(im_667L) / np.size(im_667L)

    # print(f'{intensity_728}, {intensity_706}, {intensity_667}')

    # Image.fromarray(im_728L).show()
    # Image.fromarray(im_706L).show()
    # Image.fromarray(im_667L).show()

    return (im_728L, intensity_728), (im_706L, intensity_706), (im_667L, intensity_667)

