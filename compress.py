import xarray as xr

ds = xr.open_dataset("TMY_2009_2024_fast.nc")
ds = ds.chunk({"time": 200, "lat": 10, "lon": 10})
ds.to_zarr("ghi_NOA.zarr", mode="w")



ds['GHI_corr'].mean('time').rio.to_raster('ghi_mean.tif', driver='COG')




import zarr
import numpy as np

# Create a sample Zarr array
z = zarr.create_array(
    store="my_zarr_data.zarr",
    shape=(10, 10),
    chunks=(5, 5),
    dtype="f4"
)
z[:, :] = np.random.rand(10, 10) * 100



# Get array info
array_info = z.info

# Get a small subset of the data
subset_data = z[:2, :2].tolist() # Convert to a list for easy HTML display



html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Zarr Array Example</title>
</head>
<body>
    <h1>Zarr Array Information</h1>
    <p><strong>Shape:</strong> {array_info.shape}</p>
    <p><strong>Data Type:</strong> {array_info.dtype}</p>
    <p><strong>Chunk Shape:</strong> {array_info.chunk_shape}</p>

    <h2>Subset of Data (Top-Left 2x2)</h2>
    <table border="1">
        {"".join([f"<tr>{''.join([f'<td>{val:.2f}</td>' for val in row])}</tr>" for row in subset_data])}
    </table>
</body>
</html>
"""

# Save the HTML to a file
with open("zarr_example.html", "w") as f:
    f.write(html_content)