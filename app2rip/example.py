import ripper

data, link = ripper.extract('', 38516, ['^i', 'SXR'])

print(list(data.keys()), link)

data_all = ripper.extract('in', 38516)  # extract all charts of 38516 discharge in relative path 'in'

for diag_list in data_all:
    for diag in diag_list:
        print(diag_list[diag]['name'])

x, y = ripper.x_y(data_all[0][17])  # convert data to (x, y) format

print('success')
