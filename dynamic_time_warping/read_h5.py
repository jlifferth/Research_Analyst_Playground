import h5py

file_name = '/Users/jonathanlifferth/PycharmProjects/Pairwise-Cell-Track-Matrices/cell_track_data.h5'
f = h5py.File(file_name, 'r')

for key in f.keys():
    print(key)  # Names of the groups in HDF5 file.

# List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])

print(data)
