## Dataset Collection and Data Preprocessing

### Dataset Collection

The dataset used in this project consists of historical weather-related parameters that influence flood occurrence. It contains important features such as:

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Seasonal Rainfall
- Average June Rainfall
- Subdivision Rainfall
- Flood Label

After loading the dataset into a **Pandas DataFrame**, the data was analyzed using functions such as `head()`, `info()`, and `describe()` to understand the dataset structure, identify missing values, and detect inconsistencies.

---

### Data Preprocessing

Before training the Machine Learning models, the dataset was preprocessed to improve data quality and model performance.

The preprocessing steps included:

- Checking and handling missing values.
- Removing duplicate records.
- Detecting and handling outliers using the **Interquartile Range (IQR) method**.
- Separating input features and target variable for model training.

These preprocessing techniques helped reduce the impact of noisy data and improved the reliability of flood prediction results.

