import ee

# Initialize Earth Engine
ee.Initialize(project='spatial-iris-496915-b4')

# Load Sivaganga AOI
aoi = ee.FeatureCollection(
    "projects/spatial-iris-496915-b4/assets/sivaganga"
)

# Display AOI information
print("Google Earth Engine Connected Successfully!")
print("AOI Loaded Successfully!")

# Calculate AOI area (sq.km)
area = aoi.geometry().area().divide(1e6)

print("Area (sq.km):")
print(area.getInfo())

# Get AOI bounding coordinates
bounds = aoi.geometry().bounds()

print("Bounding Box:")
print(bounds.getInfo())