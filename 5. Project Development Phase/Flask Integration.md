## Model Integration with Flask Application

The trained Machine Learning model was integrated into a **Flask-based web application** to enable real-time flood prediction.

The prediction workflow is as follows:

- User enters weather-related parameters through the prediction form.
- The input values are converted into a **Pandas DataFrame**.
- The data is transformed using the saved **StandardScaler** to maintain the same preprocessing applied during model training.
- The processed input is passed to the trained Machine Learning model.
- The model generates the flood prediction result.
- Based on the prediction output, the application displays one of the following result pages:

  - **Flood Risk Detected Page**
  - **No Flood Predicted Page**

This integration allows users to interact with the Machine Learning model through a simple and user-friendly web interface.
