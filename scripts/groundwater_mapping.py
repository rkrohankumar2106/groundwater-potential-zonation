import ee

# ==========================================
# INITIALIZE EARTH ENGINE
# ==========================================
ee.Initialize(project="spatial-iris-496915-b4")

# ==========================================
# AREA OF INTEREST (AOI)
# ==========================================
aoi = ee.FeatureCollection(
    "projects/spatial-iris-496915-b4/assets/sivaganga"
)

# ==========================================
# SENTINEL-2 DATA
# ==========================================
image = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(aoi)
    .filterDate("2023-01-01", "2023-12-31")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))
    .median()
    .clip(aoi)
)

# NDVI
ndvi = image.normalizedDifference(["B8", "B4"]).rename("NDVI")

# ==========================================
# DEM + SLOPE
# ==========================================
dem = ee.Image("USGS/SRTMGL1_003").clip(aoi)
slope = ee.Terrain.slope(dem)

# ==========================================
# LULC DATA
# ==========================================
lulc = ee.Image("ESA/WorldCover/v200/2021").select("Map").clip(aoi)

# ==========================================
# RECLASSIFICATION
# ==========================================

ndvi_class = ndvi.expression(
    "(b('NDVI') < 0.2) ? 1"
    ": (b('NDVI') < 0.4) ? 2"
    ": (b('NDVI') < 0.6) ? 3"
    ": (b('NDVI') < 0.8) ? 4"
    ": 5"
).rename("NDVI_Class")

slope_class = slope.expression(
    "(b('slope') < 2) ? 5"
    ": (b('slope') < 5) ? 4"
    ": (b('slope') < 10) ? 3"
    ": (b('slope') < 20) ? 2"
    ": 1"
).rename("Slope_Class")

lulc_class = lulc.expression(
    "(b('Map') == 80) ? 5"
    ": (b('Map') == 90) ? 4"
    ": (b('Map') == 10) ? 4"
    ": (b('Map') == 40) ? 3"
    ": (b('Map') == 30) ? 2"
    ": 1"
).rename("LULC_Class")

# ==========================================
# WEIGHTED OVERLAY ANALYSIS
# ==========================================
groundwater_index = (
    ndvi_class.multiply(0.4)
    .add(slope_class.multiply(0.3))
    .add(lulc_class.multiply(0.3))
).rename("GW_Index")

# ==========================================
# FINAL CLASSIFICATION
# ==========================================
gw_class = groundwater_index.expression(
    "(b('GW_Index') <= 1) ? 1"
    ": (b('GW_Index') <= 2) ? 2"
    ": (b('GW_Index') <= 3) ? 3"
    ": (b('GW_Index') <= 4) ? 4"
    ": 5"
).rename("GW_Class")

# ==========================================
# VISUALIZATION
# ==========================================
gw_vis = {
    "min": 1,
    "max": 5,
    "palette": [
        "#d73027",   # Very Low
        "#fc8d59",   # Low
        "#fee08b",   # Moderate
        "#91cf60",   # High
        "#1a9850"    # Very High
    ]
}

gw_map = gw_class.visualize(**gw_vis)

# ==========================================
# AREA STATISTICS
# ==========================================
pixel_area = ee.Image.pixelArea().divide(1e6)

stats = pixel_area.addBands(gw_class).reduceRegion(
    reducer=ee.Reducer.sum().group(
        groupField=1,
        groupName="Class"
    ),
    geometry=aoi.geometry(),
    scale=30,
    maxPixels=1e13
)

print("Area Statistics (km²):")
print(stats.getInfo())

# EXPORT FINAL MAP TO GOOGLE DRIVE

task = ee.batch.Export.image.toDrive(
    image=gw_map,
    description="Groundwater_Final_Map",
    folder="Groundwater_Report",
    fileNamePrefix="groundwater_final_map",
    region=aoi.geometry(),
    scale=30,
    maxPixels=1e13
)

task.start()

print("Export Task Started Successfully!")
print("Check Google Drive → Groundwater_Report folder")