import geopandas as gpd
from pathlib import Path

DATA_ROOT = Path(r"C:\Users\orinj\Documents")

# List of files to convert: (input_path, output_path, optional layer name)
conversions = [
    # Borough boundaries
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "Borough Boundaries" / "geo_export_a539c2a7-d30a-4c26-9540-a9fb57bc35cf.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "borough_boundaries.gpkg",
        None
    ),

    # Building footprints
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "Building Footprints (BK & QN)" / "geo_export_01e1024e-4f37-43f4-8d35-0c701e7c8a20.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "bk_qn_building_footprints.gpkg",
        None
    ),
    # Subway lines
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "IBX" / "Subway Lines" / "geo_export_9137b667-8e18-40c5-9687-65c426cb6fcb.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "subway_lines.gpkg",
        None
    ),
    # Pavement edge
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "NYC Planimetric Database_ Pavement Edge_20251031" / "geo_export_636f5a0b-00ce-4659-a89e-be479aa02b6b.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "pavement_edge.gpkg",
        None
    ),
    # Sidewalks
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "NYC Planimetric Database_ Sidewalk_20251031" / "geo_export_d77bc740-0279-450a-a0b4-c73f8ece7a4a.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "sidewalks.gpkg",
        None
    ),
    # Parks
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "Parks Properties_20251104" / "geo_export_03be6ed9-5d8d-403e-b157-70947265fbde.shp",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "parks.gpkg",
        None
    ),

    # Pluto
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "Pluto" / "MapPLUTO25v3.gdb",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "pluto.gpkg",
        "MapPLUTO_25v3_clipped"
    ),

    # Streets
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "DCM.gdb",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "streets.gpkg",
        "DCM_StreetCenterLine"
    ),

    # Zoning districts
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "zoning.gdb",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "zoning_districts.gpkg",
        "nyzd"
    ),
    # Commercial overlays
    (
        DATA_ROOT / "Urban Planning" / "GIS Data" / "zoning.gdb",
        DATA_ROOT / "Python" / "Basemap Generator" / "data" / "commercial_overlays.gpkg",
        "nyco"
    ),
]

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