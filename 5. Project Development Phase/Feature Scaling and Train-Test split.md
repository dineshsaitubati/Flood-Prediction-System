Feature Scaling

Since the dataset contains numerical features with different ranges, feature scaling was performed using the StandardScaler technique. Standardization transforms the data so that each feature has a mean of zero and a standard deviation of one. This helps improve the performance of distance-based algorithms and ensures consistent input for model training.


Train-Test Split

The processed dataset was divided into training and testing sets using the train_test_split() function. Approximately 75% of the data was used for training the models, while the remaining 25% was reserved for testing. This ensures that the models are evaluated on unseen data, providing a reliable estimate of their performance.

