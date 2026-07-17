## System Flowchart

The overall workflow of the **Rising Waters Flood Prediction System** is shown below:

```mermaid
flowchart TD

    A([Start]) --> B[Enter Weather Data]
    B --> C[Validate Input]
    C --> D[Scale Data]
    D --> E[Machine Learning Model Prediction]
    E --> F{Flood Condition?}

    F -->|Yes| G[Flood Prediction Page]
    F -->|No| H[Safe Page<br>(No Flood Detected)]

    G --> I([End])
    H --> I([End])
