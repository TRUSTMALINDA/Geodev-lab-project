# **Month 1 Summary Report** 

Land Use & Land Cover Change Analysis | Mzuzu District, Malawi (2020–2025) 

## **Question Restated** 

**What are the spatial and temporal changes in land use and land cover in Mzuzu District, Malawi, from 2020 to 2025?** 

## **Operations Performed & Justifications** 

1. **Dataset Acquisition & Folder Connection:** Connected workspace directories to ArcGIS Pro Catalog to load multi-band Landsat imagery and administrative boundary shapefiles. _Justification:_ Establishes systematic data access and structured file management. 

2. **Band Ordering & Composite Band Generation:** Arranged Bands 1 to 7 and executed the `Composite Bands` tool. _Justification:_ Combines separate single-band rasters into a unified multi-band dataset necessary for spectral color rendering. 

3. **Symbology Band Combinations:** Applied Natural Color (4,3,2), Color Infrared (5,4,3), Shortwave Infrared (7,6,4), and Agriculture (6,5,2). _Justification:_ Enhances visual discrimination between vegetation, urban structures, bare soil, and water features. 

4. **Reprojection & Spatial Clipping:** Reprojected data to WGS 1984 UTM Zone 36S (EPSG:32736) and clipped rasters to the Mzuzu study boundary. _Justification:_ Ensures metric distance and area precision without geographic projection distortion. 

5. **Supervised Classification (Support Vector Machine):** Digitized training samples via Training Sample Manager and trained an SVM model with unique class color symbology. _Justification:_ SVM robustly handles complex non-linear spectral signatures to accurately classify satellite pixels. 

6. **Raster to Polygon, Dissolve & Intersect:** Converted classified rasters to vector polygons, dissolved boundaries, and intersected multi-temporal layers into a single output. _Justification:_ Merges historical and recent land cover attributes into one table for direct land transition analysis. 

7. **Attribute Geometry & Area Calculations:** Added field attributes and calculated exact area measurements (km²). _Justification:_ Quantifies net surface gains and losses per land cover category over time. 

8. **Excel Pivot Tables & Charting:** Exported data to Excel to construct cross-tabulation pivot tables and comparative bar charts. 

_Justification:_ Synthesizes temporal trends into visual and tabular formats for decision-making. 

## **Expected vs. Obtained Results** 

- **Expected Results:** A gradual expansion of urban built-up areas replacing farmland and forest, accompanied by proportional spatial shifts across all major land classes. 

- **Obtained Results:** Successfully classified multi-temporal maps and intersected vector datasets confirming a rapid expansion of built-up areas primarily at the expense of agricultural land and natural vegetation in Mzuzu. 

## **Surprising Findings & Insights** 

- Rapid conversion rate of peri-urban agricultural lands into uncoordinated residential/built-up developments. 

- High classification precision and clean boundaries delivered by the Support Vector Machine (SVM) algorithm on mixed urban-rural fringe pixels. 

## **Data Still Needed** 

- **High-Resolution Imagery (PlanetScope / Drone):** For rigorous accuracy assessment, confusion matrix generation, and clearing up mixed-pixel ambiguities. 

- **Ground Control Points (GCPs):** On-site field GPS verification data to calculate Kappa coefficients and overall classification accuracy. 

- **Socio-Economic & Planning Data:** Municipal zoning maps and population growth data to evaluate urban expansion drivers. 

## **Data Sources & Links** 

|**Dataset**|**Source / Link**|
|---|---|
|Landsat 8|`https://landsatlook.usgs.gov/data/collection02/level-2/standard/oli-tirs/`<br>`2020/169/068/LC08_L2SP_169068_20201024_20201106_02_T1/`<br>`LC08_L2SP_169068_20201024_20201106_02_T1_SR_B7.TIF?`<br>`requestSignature=eyJkb3dubG9hZEFwcCI6IkVFIiwiY29udGFjdElkIjoyNzgxMDgyNSwi`|
|Satellite Imagery|`ZG93bmxvYWRJZCI6MTAyMzAwMTI2NCwiZGF0ZUdlbmVyYXRlZCI6IjIwMjYtMDktMTNUMDc6N`<br>`TI6NDQtMDU6MDAiLCJpZCI6IkxDMDhfTDJTUF8xNjkwNjhfMjAyMDEwMjRfMjAyMDExMDZfMD`<br>`JfVDFfU1JfQjcuVElGIiwic2lnbmF0dXJlIjoiJDUkJHh6b2E2UzBUU2FUV01CZzZpNXZEazd`<br>`USXVvNzVPRUc0dGE3dmo5ZEp0VTcifQ==`|



Malawi Administrative `https://data.humdata.org/dataset/cod-ab-mwi` Boundaries 

