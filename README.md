# Crime Analysis Project

This project focuses on the analysis of crime data, including cleaning, reshaping, filtering, and visualizing the data using Python and R. The data primarily involves crime types, occurrence year, date, and geographic locations (county, city, district).

## Reference Textbooks
- *Pandas資料清理、重塑、過濾、視覺化: Python資料分析必備套件!* by Matt Harrison & Theodore Petrou
- *R錦囊妙計 (第2版)* by J.D Long & Paul Teetor
- *精通大數據! R語言資料分析與應用 (第2版)* by Jared P. Lander

## Data Fields

The following fields are used in the dataset:
- **type** (Crime type)
- **oc_year** (Year of occurrence)
- **oc_data** (Date of occurrence)
- **oc_county** (County of occurrence)
- **oc_region** (District of occurrence)

Note: **Bold** fields are standard fields in the dataset.

## Data Source

- [Data.gov.tw Dataset](https://data.gov.tw/dataset/14200)
- [Medium Article on Data Analysis](https://medium.com/@jason8410271027/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E7%AC%AC%E4%B8%80%E6%AD%A5-%E8%B3%87%E6%96%99%E6%93%B7%E5%8F%96-%E6%95%B4%E7%90%86-%E5%8F%AF%E8%A6%96%E5%8C%96-efa30b4dde56)

## Known Issues

- **2024-10-04**: The format of `oc_data` is inconsistent in length. For example, `604` and `1121` have lengths of 3 and 4, respectively. When extracting months, ensure to use the first 1 or 2 digits from the left.
  
  ```R
  data$month <- as.numeric(substr(data$oc_data, 1, nchar(data$oc_data) - 2))
  ```
  This code assumes the month is at the beginning of the data, but the varying length may cause errors. Handle different lengths carefully.

## File Structure and Description

- **data warehouse**: Outputs the raw data for crime types and time in each county and city.
- **crime_stat110.py**: Joins raw data for the year 110 into a dataframe.
- **crime_stat111.py**: Joins raw data for the year 111 into a dataframe.
- **crime_stat112.py**: Joins raw data for the year 112 into a dataframe.
- **Descriptive_df110.csv**: Exports cleaned data for the year 110.
- **Descriptive_df111.csv**: Exports cleaned data for the year 111.
- **Descriptive_df112.csv**: Exports cleaned data for the year 112.
- **Merge_df110.csv**: Combines monthly data for the year 110.
- **Merge_df111.csv**: Combines monthly data for the year 111.
- **Merge_df112.csv**: Combines monthly data for the year 112.
- **finish.csv**: Contains combined data from `Merge_df110`, `Merge_df111`, and `Merge_df112`.
- **csv_merge.py**: Merges `Descriptive_df110`, `Descriptive_df111`, and `Descriptive_df112` into `finish.csv`.
- **Plt.py**: Visualizes correlations between various crime types.
- **easyStat.py**: Visualizes event type distribution, hard-to-distinguish distribution, and month distribution.
- **Corr.py**: Visualizes correlations between different crime types.
- **analysis.R**: Performs Chi-Square fitness test on the data.
- **OneWayANOVA.R**: Analyzes seasonal changes in the month and number of events.

## Getting Started

To get started with this project, clone the repository:

```bash
git clone https://github.com/yourusername/crime_analysis.git
cd crime_analysis
```

### Requirements

- Python 3.x
- R (for running analysis in `analysis.R` and `OneWayANOVA.R`)
- Required Python libraries:
  - Pandas
  - Matplotlib
  - NumPy
  - etc.

You can install the Python requirements using:

```bash
pip install -r requirements.txt
```

### Running the Code

1. Run the Python scripts for data processing:
   ```bash
   python crime_stat110.py
   python crime_stat111.py
   python crime_stat112.py
   ```

2. Merge the data:
   ```bash
   python csv_merge.py
   ```

3. Visualize crime data:
   ```bash
   python Plt.py
   ```

4. To run the R scripts for statistical analysis:
   ```bash
   Rscript analysis.R
   Rscript OneWayANOVA.R
   ```

## License