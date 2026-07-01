# Groundwater Potential Zonation using GIS-Based Multi-Criteria Analysis

## Project Overview

This project identifies groundwater potential zones in Sivaganga District, Tamil Nadu, using Remote Sensing and GIS techniques. A weighted overlay analysis was performed by integrating vegetation, topography, and land use information derived from satellite imagery and digital elevation data.

The project was developed using Google Earth Engine (GEE) and the Earth Engine Python API.

---

## Objectives

- Delineate groundwater potential zones in Sivaganga District.
- Generate thematic layers including NDVI, DEM, Slope, and Land Use/Land Cover (LULC).
- Apply weighted overlay analysis to estimate groundwater potential.
- Produce groundwater potential maps and calculate class-wise area statistics.

---

## Study Area

- Location: Sivaganga District, Tamil Nadu, India
- Area of Interest: Administrative boundary of Sivaganga District
- Coordinate System: WGS 84

---

## Datasets Used

| Dataset | Source | Purpose |
|----------|--------|---------|
| Sentinel-2 Level-2A | Copernicus | NDVI Generation |
| SRTM DEM | USGS | Elevation and Slope |
| ESA WorldCover 2021 | European Space Agency | Land Use/Land Cover |
| Sivaganga Boundary | Google Earth Engine Asset | Area of Interest |

---

## Software and Tools

- Python 3.x
- Google Earth Engine Python API
- Google Earth Engine
- Visual Studio Code

---

## Project Workflow

1. Initialize Google Earth Engine
2. Load Sivaganga District boundary
3. Acquire Sentinel-2 imagery
4. Generate NDVI
5. Generate DEM and Slope
6. Load LULC dataset
7. Reclassify thematic layers
8. Perform weighted overlay analysis
9. Classify groundwater potential zones
10. Calculate area statistics
11. Generate the final groundwater potential map

---

## Groundwater Potential Classes

| Class | Description |
|-------|-------------|
| 1 | Very Low |
| 2 | Low |
| 3 | Moderate |
| 4 | High |
| 5 | Very High |

---

## Results

The project generated the following outputs:

- NDVI Map
- DEM Map
- Slope Map
- LULC Map
- Groundwater Potential Zone Map
- Area Statistics

### Area Statistics

| Groundwater Class | Area (km²) |
|-------------------|-----------:|
| Very Low | 0.17 |
| Low | 97.15 |
| Moderate | 2076.51 |
| High | 1652.96 |
| Very High | 239.53 |

---

## Project Structure

```
Groundwater-Mapping/
│
├── scripts/
│   └── groundwater_mapping.py
│
├── outputs/
│   ├── groundwater_map.png
│   ├── ndvi_map.png
│   ├── dem_map.png
│   ├── slope_map.png
│   └── lulc_map.png
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/groundwater-mapping.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Authenticate Google Earth Engine (first-time setup):

```bash
earthengine authenticate
```

Run the project:

```bash
python scripts/groundwater_mapping.py
```

---

## Sample Outputs

Include the following maps in the `outputs` folder:

- Study Area (AOI)
- Digital Elevation Model (DEM)
- Slope Map
- NDVI Map
- Land Use/Land Cover (LULC) Map
- Groundwater Potential Zone Map

To display an image in GitHub:

```markdown
![Groundwater Potential Map](outputs/groundwater_map.png)
```

---

## References

1. Google Earth Engine Documentation
2. Copernicus Sentinel-2 Mission
3. USGS Shuttle Radar Topography Mission (SRTM)
4. ESA WorldCover 2021

---

## Author

Rohan Kumar

B.E. Computer Science and Engineering  
R.M.D. Engineering College

---

## License

This project is intended for educational and research purposes.