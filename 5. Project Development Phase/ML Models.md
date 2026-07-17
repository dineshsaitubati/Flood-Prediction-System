## Machine Learning Model Development and Evaluation

To identify the most suitable algorithm for flood prediction, four classification models were implemented and evaluated using the processed dataset.

### 1. Decision Tree

The **Decision Tree** algorithm classifies data by creating decision rules based on feature values. It is simple to interpret, computationally efficient, and provides fast predictions.

**Testing Accuracy:** 96.55%

---

### 2. Random Forest

The **Random Forest** algorithm combines multiple decision trees to improve prediction accuracy and reduce overfitting. It provides more reliable predictions by using an ensemble learning approach.

**Testing Accuracy:** 96.55%

---

### 3. K-Nearest Neighbors (KNN)

The **K-Nearest Neighbors (KNN)** algorithm predicts the class of a new data sample based on the majority class among its nearest neighboring data points.

**Testing Accuracy:** 89.66%

---

### 4. Gradient Boosting

The **Gradient Boosting** algorithm builds multiple weak learners sequentially, where each new model focuses on correcting the errors made by previous models.

It achieved strong predictive performance and was selected as the final deployment model due to its high accuracy and good generalization capability.

**Testing Accuracy:** 96.55%

---

### Model Performance Comparison

| Model | Accuracy |
|-------|----------|
| Decision Tree | 96.55% |
| Random Forest | 96.55% |
| K-Nearest Neighbors (KNN) | 89.66% |
| Gradient Boosting | 96.55% |

Based on the evaluation results, **Gradient Boosting** was selected as the final model for integration with the Flask web application.
