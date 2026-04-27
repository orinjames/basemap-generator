import geopandas as gpd
from pathlib import Path

DATA_ROOT = Path(r"C:\Users\orinj\Documents\Urban Planning\GIS Data")

# List of files to convert: (input_path, output_path, optional layer name)
conversions = [
    (
        DATA_ROOT / "IBX" / "bk_qn_building_footprints.geojson",
        DATA_ROOT / "IBX" / "bk_qn_building_footprints.gpkg",
        None
    ),
    (
        DATA_ROOT / "NYC Planimetric Database_ Pavement Edge_20251031" / "geo_export_636f5a0b-00ce-4659-a89e-be479aa02b6b.shp",
        DATA_ROOT / "NYC Planimetric Database_ Pavement Edge_20251031" / "pavement_edge.gpkg",
        None
    ),
    # add others as needed
]

for input_path, output_path, layer in conversions:
    print(f"Converting {input_path.name}...")
    gdf = gpd.read_file(input_path) if layer is None else gpd.read_file(input_path, layer=layer)
    gdf.to_file(output_path, driver="GPKG")
    print(f"  Saved to {output_path.name}")

print("Done.")