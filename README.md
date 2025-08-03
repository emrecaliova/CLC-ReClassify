# CORINE Land Cover Reclassification Tool

This repository provides a simple script for reclassifying **CORINE Land Cover (CLC)** raster data into generalized land use categories for hydrological modeling, especially for use in **mHM (mesoscale Hydrologic Model)**.

## 🧭 Overview

The script transforms the original CLC classes into three simplified categories:

- **1 - Forest**
- **2 - Impervious**
- **3 - Pervious**
- **48 - NODATA** (later to be mapped as `255` for mHM input file as .asc)

This preprocessing step helps in simplifying complex land cover types into meaningful hydrological classes.

---

## 📂 Input / Output

- **Input:**  
  `./CORINE/CLC2018_V2020_20u1.tif`  
  A raster file containing the original CORINE land cover data.

- **Output:**  
  `./CORINE/ReClassifiedData/ReClassified_CLC2018_V2020_20u1.tif`  
  A raster file with reclassified land cover values.

---

## 🧪 Reclassification Rules

| Original CLC Class Range | Description                                    | New Class |
|--------------------------|------------------------------------------------|-----------|
| 1–11                     | Artificial Surfaces                            | 2         |
| 12–13                    | Arable Land (non-irrigated, irrigated)         | 3         |
| 14                       | Rice Fields                                    | 2         |
| 15–17                    | Permanent Crops                                | 1         |
| 18                       | Pastures                                       | 3         |
| 19–21                    | Heterogeneous Agricultural Areas               | 3         |
| 22                       | Agro-forestry Areas                            | 1         |
| 23–25                    | Forests                                        | 1         |
| 26–28                    | Grasslands, Moors, Sclerophyllous Vegetation   | 3         |
| 29                       | Transitional Woodland-Shrub                    | 1         |
| 30                       | Beaches, Dunes, Sands                          | 3         |
| 31                       | Bare Rocks                                     | 2         |
| 32–33                    | Sparsely Vegetated / Burnt Areas               | 3         |
| 34                       | Glaciers, Snow                                 | 2         |
| 35–39                    | Wetlands                                       | 2         |
| 40–44                    | Water Bodies                                   | 2         |
| 48–50, -128              | NODATA / Undefined                             | 48        |

> 💡 `48` should be interpreted as `255` when used in mHM.

---

## 🛠 Dependencies

- Python 3.x
- [NumPy](https://numpy.org/)
- [rasterio](https://rasterio.readthedocs.io/en/latest/)

Install dependencies with:

```bash
pip install numpy rasterio
```

---

## 🚀 Usage

Just run the Python script:

```bash
python reclassify_corine.py
```

Ensure the input raster exists in the specified directory. The reclassified file will be saved to the output path.

---

## 👨‍💻 Author

**Emre Çalıova**  
Meteorological Engineer

📧 [Mail](mailto:caliova94@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/emrecaliova)  
📅 Created: 23.07.2025

---

## 📄 License

This project is licensed under the MIT License.
You may use, modify, and distribute it freely. Please credit the author where appropriate.
