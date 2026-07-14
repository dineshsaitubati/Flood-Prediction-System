Dataset Collection

The dataset used in this project consists of historical weather-related parameters that influence flood occurrence. It contains features such as temperature, humidity, cloud cover, annual rainfall, seasonal rainfall, average June rainfall, subdivision rainfall, and the flood label. After loading the dataset into a Pandas DataFrame, the data was examined using functions such as head(), info(), and describe() to understand its structure and identify any missing or inconsistent values.


Data Preprocessing

Before training the models, the dataset was preprocessed to improve the quality of the input data. Missing values and duplicate records were checked, and outliers were handled using the Interquartile Range (IQR) method. This reduced the influence of extreme values on model performance. Finally, the features and target variable were separated for further processing.

