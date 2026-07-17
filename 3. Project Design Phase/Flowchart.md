## System Flowchart

The workflow of the flood prediction system is as follows:

```text
Start
  ↓
Enter Weather Data
  ↓
Validate Input
  ↓
Scale Input Data
  ↓
Machine Learning Model Prediction
  ↓
Flood Condition?
  ↓
 ┌───────────────┴───────────────┐
 ↓                               ↓
Yes                             No
 ↓                               ↓
Flood Prediction Page            Safe Page
(Flood Detected)                 (No Flood)
 ↓                               ↓
          End
