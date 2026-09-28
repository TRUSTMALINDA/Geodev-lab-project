Week 2. Project brief

Part 1 : the question

What are the spatial and temporal changes in land use and land cover in Mzuzu District, Malawi, from 2020 to 2025.

Part 2: why it matters

Land use and land cover change is important in Mzuzu because changes in vegetation, agricultural land, built-up areas, water bodies and bare land can affect environmental management, agriculture, settlement planning and natural resources. By comparing satellite images from different years, the study can identify where land cover has changed and determine which classes have increased or decreased. This information can help planners, environmental managers and local authorities understand the spatial pattern of development and environmental change in Mzuzu.

Part 3: the data needed

- I. Landsat satellite imagery 2020

- II. Landsat satellite imagery 2025

- III. Malawi boundary

Part 4: where the data come from

| Dataset | Purpose | Source | Geometry type |
| --- | --- | --- | --- |
| Landsat | Used to | https://earthexplorer.usgs.gov/ | TIF |
| satellite images (2020) cover at the | classify land start of the study period |   |   |
| Landsat | Used to | https://earthexplorer.usgs.gov/ | TIF |
| satellite images (2025) cover at the | classify land end of the study period, for comparison |   |   |
| Google earth pro engine | Used as a reference to check the | A software | Web map |


| Dataset | Purpose | Source | Geometry type |
| --- | --- | --- | --- |
|   | accuracy of the land cover classification |   |   |
| Malawi | Used to | https://data.humdata.org/dataset/cod-ab-mwi | SHAPEFILE.shp |
| administrative define and boundary data | cut out the exact study area | mwi_admin_boundaries.gdb.zipGeodatabase(24.1M) Resource ID: a4360362-52d4-43f8- 8251-606653c0db53 Modified : 26 January 2026 |   |

## Part 5 : what I will build

I will build an interactive web-based land use and land cover change visualization tool for Mzuzu District. The map could be updated as new changes are happening in the districts

## short data flow

- I. adding folder connection to where the Landsat data was

- II. selecting the required bands (band 1 to 6) and adding them to current map using the catalog.

- III. Arrange the bands in order from band 1 to band 6

- IV. Raster composite, it combines multiple datasets into one multiband, on imagery tab-processing and then the composite.

- V. Combine the bands through the symbology

Natural color (4,3,2)

Infrared color (5,4,3)

Soft wave infrared (7,6,4)

Agriculture (6,5,2)

- VI. Adding a shapefile of the area of focus or study area Mzuzu,


- VII. Clip raster to area of focus

- VIII. The navigate to imagery-classification tools -training sample manager

- IX. Add the class boundary and start doing supervised classification by digitizing the classes for training samples

- X. The classify, by choosing any classification method like SVM or Random Forest

- XI. Then convert raster to polygon to get the area changes

- XII. Then, attribute, add fields to do the geometry calculator and field calculator to determine the area how the land use land cover has changed over the selected years

- XIII. In the excel, using the pivot tables we establish a bar chat to detect the area of change over the years .
