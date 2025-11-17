import xarray as xr

ds = xr.open_dataset("TMY_2009_2024_fast.nc")

GHI_prom = ds["GHI_corr"].where(ds["GHI_corr"] > 0).mean(dim="time")


ds_out = xr.Dataset(
    {
        "GHI_promedio_pos": GHI_prom
    },
    coords={
        "lat": ds.lat,
        "lon": ds.lon
    }
)

ds_out.to_netcdf("GHI_promedio.nc")




import xarray as xr
import json

# Abrir NetCDF
ds = xr.open_dataset("GHI_promedio.nc")

# Extraer coordenadas y datos
lats = ds["lat"].values.tolist()
lons = ds["lon"].values.tolist()
data = ds["GHI_promedio_pos"].values.tolist()   # matriz 2D

geo = {
    "lat": lats,
    "lon": lons,
    "GHI_promedio": data
}

# Guardar JSON
with open("GHI_promedio.json", "w") as f:
    json.dump(geo, f)