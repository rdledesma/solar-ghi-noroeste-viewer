// Necesario si querés mantener el alias:
const z = zarr;

// URL del store Zarr (local)
const store = new zarr.FetchStore("http://127.0.0.1:8000/ghi_NOA.zarr/");
const root = await zarr.openGroup(store);


// Abrir grupo raíz


// Cargar variables
const ghi = await root.getItem("GHI");
const lats = await root.getItem("lat");
const lons = await root.getItem("lon");
const time = await root.getItem("time");

// Obtener coordenadas completas
const latVals = await lats.get();
const lonVals = await lons.get();
const timeVals = await time.get();

// Inicializar mapa
const map = new maplibregl.Map({
    container: 'map',
    style: 'https://demotiles.maplibre.org/style.json',
    center: [-65, -26],
    zoom: 5
});

// Click en el mapa
map.on('click', async (e) => {
    const lat = e.lngLat.lat;
    const lon = e.lngLat.lng;

    // Índice lat/lon más cercano
    const ilat = indexNearest(latVals, lat);
    const ilon = indexNearest(lonVals, lon);

    console.log("Lat:", lat, "ILAT:", ilat);
    console.log("Lon:", lon, "ILON:", ilon);

    // Extraer serie temporal completa para ese punto
    const serie = await ghi.get([null, ilat, ilon]);

    // Graficar
    Plotly.newPlot('chart', [{
        x: timeVals,
        y: serie,
        mode: 'lines',
        type: 'scatter'
    }]);
});

// Función auxiliar
function indexNearest(arr, value){
    let idx = 0;
    let min = Infinity;
    for (let i = 0; i < arr.length; i++) {
        const d = Math.abs(arr[i] - value);
        if (d < min) { idx = i; min = d; }
    }
    return idx;
}
