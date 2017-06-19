import numpy as np

# replace `~` with user directory i.e. `/Users/my_username`
npz_location = '~/.keras/datasets/imdb.npz'
csv_location = '~/code/aind-projects/aind2-dl/temp/'
data = np.load(npz_location)
print(data.keys())
print(data.f.x_train)
print(data.f.x_test)
print(data.f.y_train)
print(data.f.y_test)
for key, value in data.items():
    np.savetxt(csv_location + key + ".csv", value)