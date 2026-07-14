The overall architecture of the proposed system is illustrated below.

User
   ↓
Flask Web Application
   ↓
Input Validation
   ↓
Data Preprocessing
(StandardScaler)
   ↓
Gradient Boosting Model
   ↓
Prediction
   ↓
Flood Risk / No Flood Result


The architecture begins with the user entering weather-related parameters through the web interface. The Flask application receives these inputs and validates them before passing them to the preprocessing module. The StandardScaler transforms the input values using the same scaling applied during model training. The processed data is then provided to the trained Gradient Boosting model, which predicts whether flood conditions are likely to occur. Finally, the prediction result is displayed on the corresponding output page.