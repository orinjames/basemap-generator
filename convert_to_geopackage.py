''' 
_______ Convert to Geopackage _______

This script converts the original geospatial data files to geopackages to improve performance.

Input file data into conversions list as follows:

(
    input_path,
    output_path,
    None OR Geodatabase layer name
)

Note that Geodatabase files require an additional layer specification.

1) Set your SOURCE_DATA_ROOT with the location of the downloaded data files (e.g. Downloads folder)
2) Set your TARGET_DATA_ROOT with the location where you want the converted geopackages to be saved (e.g. a data folder in your project)
3) Run this script in your command line

'''
import geopandas as gpd
from pathlib import Path

# UPDATE THESE PATHS
SOURCE_DATA_ROOT = Path(r"C:\Users\username\Downloads")
TARGET_DATA_ROOT = Path(r"C:\Users\username\Documents\Basemap Generator\data")

# List of files to convert: (input_path, output_path, optional layer name)
conversions = [
    # Borough boundaries
    (
        SOURCE_DATA_ROOT / "Borough Boundaries" / "geo_export_a539c2a7-d30a-4c26-9540-a9fb57bc35cf.shp",
        TARGET_DATA_ROOT / "borough_boundaries.gpkg",
        None
    ),

    # Building footprints
    (
        SOURCE_DATA_ROOT / "Building Footprints" / "geo_export_01e1024e-4f37-43f4-8d35-0c701e7c8a20.shp",
        TARGET_DATA_ROOT / "building_footprints.gpkg",
        None
    ),
    # Subway lines
    (
        SOURCE_DATA_ROOT / "Subway Lines" / "geo_export_9137b667-8e18-40c5-9687-65c426cb6fcb.shp",
        TARGET_DATA_ROOT / "subway_lines.gpkg",
        None
    ),
    # Pavement edge
    (
        SOURCE_DATA_ROOT / "NYC Planimetric Database_ Pavement Edge_20251031" / "geo_export_636f5a0b-00ce-4659-a89e-be479aa02b6b.shp",
        TARGET_DATA_ROOT / "pavement_edge.gpkg",
        None
    ),
    # Sidewalks
    (
        SOURCE_DATA_ROOT / "NYC Planimetric Database_ Sidewalk_20251031" / "geo_export_d77bc740-0279-450a-a0b4-c73f8ece7a4a.shp",
        TARGET_DATA_ROOT / "sidewalks.gpkg",
        None
    ),
    # Parks
    (
        SOURCE_DATA_ROOT / "Parks Properties_20251104" / "geo_export_03be6ed9-5d8d-403e-b157-70947265fbde.shp",
        TARGET_DATA_ROOT / "parks.gpkg",
        None
    ),
    # Pluto (Geodatabase)
    (
        SOURCE_DATA_ROOT / "Pluto" / "MapPLUTO25v3.gdb",
        TARGET_DATA_ROOT / "pluto.gpkg",
        "MapPLUTO_25v3_clipped"
    ),
    # Streets (Geodatabase)
    (
        SOURCE_DATA_ROOT / "DCM.gdb",
        TARGET_DATA_ROOT / "streets.gpkg",
        "DCM_StreetCenterLine"
    ),
    # Zoning districts (Geodatabase)
    (
        SOURCE_DATA_ROOT / "zoning.gdb",
        TARGET_DATA_ROOT / "zoning_districts.gpkg",
        "nyzd"
    ),
    # Commercial overlays (Geodatabase)
    (
        SOURCE_DATA_ROOT / "zoning.gdb",
        TARGET_DATA_ROOT / "commercial_overlays.gpkg",
        "nyco"
    ),
]

# Convert each file input
for input_path, output_path, layer in conversions:
    print(f"Converting {input_path.name}...")

    # Load data to geodataframe and any specific layer as needed
    if layer is None:
        gdf = gpd.read_file(input_path)
    else:
        gdf = gpd.read_file(input_path, layer=layer)
    
    # Save as geopackage file
    gdf.to_file(output_path, driver="GPKG")
    print(f"  Saved to {output_path.name}")
print("Done.")