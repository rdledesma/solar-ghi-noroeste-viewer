async function main() {
    const out = document.getElementById("out");

    try {
        const response = await fetch("miarchivo.nc");

        if (!response.ok) {
            throw new Error("TMY_2009_2024_fast.nc");
        }

        const arrayBuffer = await response.arrayBuffer();

        // En netcdfjs 0.3.0 se usa así:
        const reader = new NetCDFReader(arrayBuffer);

        const dims = reader.dimensions;
        const vars = reader.variables.map(v => v.name);

        out.textContent =
            "Versión NetCDF: " + reader.version + "\n" +
            "Dimensiones:\n" + JSON.stringify(dims, null, 2) + "\n\n" +
            "Variables:\n" + vars.join(", ");

        // Ejemplo: si existe lat
        if (vars.includes("lat")) {
            console.log("lat =", reader.getDataVariable("lat"));
        }

    } catch (err) {
        out.textContent = "ERROR: " + err;
        console.error(err);
    }
}

main();
