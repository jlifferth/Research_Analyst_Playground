import tifffile
import napari

path = '/Users/jonathanlifferth/data/imaging-hackathon/exemplar-001/exemplar-001.ome.tif'
img = tifffile.imread(path)
napari.view_image(img, channel_axis=0)
