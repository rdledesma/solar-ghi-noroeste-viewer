import xarray as xr

ds = xr.open_dataset("tmy_NOA_ghi.nc")
ds = ds.chunk({"time": 200, "lat": 10, "lon": 10})
ds.to_zarr("ghi_NOA.zarr", mode="w")
