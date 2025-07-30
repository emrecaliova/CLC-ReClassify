"""
CORINE Land Cover Reclassification Script
-----------------------------------------

This script reclassifies CORINE Land Cover (CLC) raster data into generalized hydrologically meaningful land use categories.

Categories:
    1 - Forest
    2 - Impervious
    3 - Pervious
    48 - NODATA (should be interpreted as 255 in mHM .asc input)

Author: Emre Çalıova - caliova94@gmail.com
Created: 23.07.2025
"""

import rasterio
import numpy as np
import os

# Input/Output File Paths
INPUT_CLC_FILE_PATH_NAME = "./CORINE/CLC2018_V2020_20u1.tif"
OUTPUT_FILE_PATH_NAME = "./CORINE/ReClassifiedData/ReClassified_CLC2018_V2020_20u1.tif"

# Load CORINE Raster
data_storaged = rasterio.open(INPUT_CLC_FILE_PATH_NAME)

# Read CORINE Land Cover Data
clc_data = data_storaged.read(1)

# Copy Data for ReClassification
reClass_data = clc_data.copy()


# ReClassification Rules

# All Artificial Surfaces → Impervious
reClass_data[np.where((reClass_data >= 1) & (reClass_data <= 11))] = 2
# Agricultural Surfaces [Arable Land > Non-irrigated arable land & Permanently irrigated land] → Pervious
reClass_data[np.where((reClass_data >= 12) & (reClass_data <= 13))] = 3
# Agricultural Surfaces [Arable Land > Rice fields] → Impervious
reClass_data[np.where(reClass_data == 14)] = 2
# Agricultural Surfaces [Permanent Crops] → Forest
reClass_data[np.where((reClass_data >= 15) & (reClass_data <= 17))] = 1
# Agricultural Surfaces [Pastures] → Pervious
reClass_data[np.where(reClass_data == 18)] = 3
# Agricultural Surfaces [Heterogeneous Agricultural Areas > Annual crops associated with permanent crops & complex cultivtion patterns & land principilly occupied by agriculture with significant areas of natural vegetatiton] → Pervious
reClass_data[np.where((reClass_data >= 19) & (reClass_data <= 21))] = 3
# Agricultural Surfaces [Heterogeneous Agricultural Areas > Agro-forestry areas] → Forest
reClass_data[np.where(reClass_data == 22)] = 1
# Forest And Semi Natural Areas [Forests] → Forest
reClass_data[np.where((reClass_data >= 23) & (reClass_data <= 25))] = 1
# Forest And Semi Natural Areas [Scrub And/Or Herbaceous Vegetation Associations > Natural grasslands & moors and healthland & sclerophyllous vegetation] → Pervious
reClass_data[np.where((reClass_data >= 26) & (reClass_data <= 28))] = 3
# Forest And Semi Natural Areas [Scrub And/Or Herbaceous Vegetation Associations > Transitional woodland-shrub] → Forest
reClass_data[np.where(reClass_data == 29)] = 1
# Forest And Semi Natural Areas [Open spaces with little or no vegetation > Beaches, dunes, sands] → Pervious
reClass_data[np.where(reClass_data == 30)] = 3
# Forest And Semi Natural Areas [Open spaces with little or no vegetation > Bare rocks] → Impervious
reClass_data[np.where(reClass_data == 31)] = 2
# Forest And Semi Natural Areas [Open spaces with little or no vegetation > Sparsely vegetated areas & burnt areas] → Pervious
reClass_data[np.where((reClass_data >= 32) & (reClass_data <= 33))] = 3
# Forest And Semi Natural Areas [Open spaces with little or no vegetation > Glaciers and perpetual snow] → Impervious
reClass_data[np.where(reClass_data == 34)] = 2
# All Wetlands → Impervious
reClass_data[np.where((reClass_data >= 35) & (reClass_data <= 39))] = 2
# All Water Bodies → Impervious
reClass_data[np.where((reClass_data >= 40) & (reClass_data <= 44))] = 2
# No Data → NODATA
reClass_data[np.where((reClass_data >= 48) & (reClass_data <= 50))] = 48
# Undefined NODATA → NODATA
reClass_data[np.where(reClass_data == -128)] = 48

# Remove existing output if present
if os.path.exists(OUTPUT_FILE_PATH_NAME):
    os.remove(OUTPUT_FILE_PATH_NAME)

# Save the ReClassified Raster
with rasterio.open(OUTPUT_FILE_PATH_NAME, 'w',
                    driver=data_storaged.driver,
                    height=data_storaged.height,
                    width=data_storaged.width,
                    count=data_storaged.count,
                    crs=data_storaged.crs,
                    transform=data_storaged.transform,
                    dtype=clc_data.dtype
                    ) as dst:
    dst.write(reClass_data, indexes = 1)
    dst.close()

data_storaged.close()