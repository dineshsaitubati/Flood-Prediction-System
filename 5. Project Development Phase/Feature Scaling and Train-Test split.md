## Feature Scaling and Train-Test Split

### Feature Scaling

Since the dataset contains numerical features with different value ranges, feature scaling was applied before training the Machine Learning models.

The **StandardScaler** technique was used to standardize the features by transforming the data so that each feature has:

- Mean value = 0
- Standard deviation = 1

Feature scaling helps improve model performance by providing consistent input values and ensuring that features with larger ranges do not dominate the learning process.

---

### Train-Test Split

After preprocessing and feature scaling, the dataset was divided into training and testing sets using the `train_test_split()` function.

The dataset was split as follows:

| Dataset | Percentage |
|---------|------------|
| Training Data | 75% |
| Testing Data | 25% |

The training data was used to build the Machine Learning models, while the testing data was used to evaluate their performance on unseen data and measure prediction reliability.
