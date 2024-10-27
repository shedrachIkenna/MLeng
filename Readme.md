# Machine Learning Engineering and Operations (MLOps) Projects

## Projects Overview

### 1. **Batch Anomaly Detection Service**
- **Description**: A service to detect anomalous rides by analyzing unusual patterns in ride duration and distance.
- **Key Features**:
  - Automated anomaly detection in ride data
  - Real-time processing capabilities
  - Scalable batch processing
  
- **Tech Stack**:
  - **Language**: Python
  - **ML Libraries**: Scikit-learn, Pandas
  - **Backend**: Flask
  - **Containerization**: Docker

- **Pipeline Stages**:
  1. Data Collection & Preprocessing
  2. Feature Engineering
  3. Model Training
  4. Model Evaluation
  5. Containerized Deployment

- **Getting Started**:
  ```bash
  # Instructions for running the project
  git clone [repository-url]
  cd batch-anomaly-detection
  docker build -t anomaly-detection .
  docker run -p 5000:5000 anomaly-detection