# Rising Waters – Flood Prediction Using Machine Learning

## Project Overview

Rising Waters is a Machine Learning-based flood prediction system developed to predict the likelihood of flood occurrence using historical weather data. The system analyzes multiple weather-related parameters and classifies whether flood conditions are likely to occur. The trained machine learning model is integrated into a Flask web application, providing users with a simple and interactive interface for real-time flood prediction.

---

## Project Objectives

- Predict flood occurrence using historical weather data.
- Compare multiple Machine Learning classification algorithms.
- Select the best-performing model based on evaluation metrics.
- Deploy the trained model using a Flask web application.
- Provide a simple and user-friendly prediction interface.

---

## Features

- Machine Learning-based flood prediction
- Comparison of multiple classification algorithms
- Real-time prediction through a Flask web application
- Input validation for prediction form
- Saved trained model using Joblib
- Responsive web interface

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Model Storage
- Joblib

---

## Dataset

The dataset contains historical weather parameters used for flood prediction.

### Input Features

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Subdivision Rainfall

### Target Variable

- Flood (Yes / No)

---

## Machine Learning Models

The following machine learning algorithms were implemented and evaluated.

| Model | Accuracy |
|--------|----------|
| Decision Tree | 96.55% |
| Random Forest | 96.55% |
| K-Nearest Neighbors | 89.66% |
| Gradient Boosting | 96.55% |

Gradient Boosting was selected as the final deployment model due to its reliable prediction performance and strong generalization capability.

---

## Project Structure

```
Rising-Waters
│
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
│
├── data/
├── models/
│   ├── floods.save
│   └── transform.save
│
├── notebooks/
├── static/
├── templates/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Source Code

The project source code is organized as follows:

- **Machine Learning Implementation:** `notebooks/`
- **Dataset:** `data/`
- **Saved Models:** `models/`
- **HTML Templates:** `templates/`
- **CSS, JavaScript and Images:** `static/`
- **Flask Application:** `app.py`

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>.git
```

Navigate to the project directory.

```bash
cd <YOUR_REPOSITORY>
```

Install the required libraries.

```bash
pip install -r requirements.txt
```

Run the Flask application.

```bash
python app.py
```

Open the application in your browser.

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. Launch the Flask application.
2. Open the Home page.
3. Navigate to the Prediction page.
4. Enter the required weather parameters.
5. Submit the prediction request.
6. View the prediction result.

---

## Documentation

The complete project documentation is available in the following folders:

- 1. Brainstorming & Ideation
- 2. Requirement Analysis
- 3. Project Design Phase
- 4. Project Planning Phase
- 5. Project Development Phase
- 6. Project Testing
- 7. Project Documentation
- 8. Project Demonstration

---

## Demonstration Video

Project Demonstration Video:

**Link:** *(Add your YouTube or Google Drive video link here.)*

---

## Live Application

The deployed application can be accessed at:

**Link:** *(Add your Render deployment URL here.)*

---

## Future Enhancements

- Integration with real-time weather APIs
- Interactive flood risk visualization using maps
- SMS and Email alert system
- Cloud-based deployment for large-scale usage
- Mobile application support

---

## Author

**Dinesh Sai Tubati**

Bachelor of Technology

Computer Science and Engineering

SRM University – AP


