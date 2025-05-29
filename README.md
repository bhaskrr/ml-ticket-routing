![banner-image](/media/banner.png)

# 🧠 AI Support Ticket Triage System

An AI-powered app that classifies IT support tickets (e.g., software issues, hardware failures, network errors) into predefined categories. It exposes a REST API and includes a frontend built with Next.js and TailwindCSS.

## Table of contents <!-- omit in toc -->

- [🧠 AI Support Ticket Triage System](#-ai-support-ticket-triage-system)
  - [✅ Requirements Gathering \& Planning](#-requirements-gathering--planning)
    - [📌 Problem Statement](#-problem-statement)
    - [🫡 Objective](#-objective)
    - [🎯 Goals \& Deliverables](#-goals--deliverables)
    - [🗂️ Ticket Types \& Labels (Multi-Class)](#️-ticket-types--labels-multi-class)
    - [🧠 Model Plan](#-model-plan)
    - [🏗️ Architecture Overview](#️-architecture-overview)
    - [🧱 Non-Functional Requirements](#-non-functional-requirements)
    - [🛠️ Tools \& Stack (Preview)](#️-tools--stack-preview)
  - [✅ Data Collection \& Preprocessing](#-data-collection--preprocessing)
    - [📦 Dataset](#-dataset)
    - [🔄 Preprocessing](#-preprocessing)
    - [📊 Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
  - [✅ Model Training \& Evaluation](#-model-training--evaluation)
    - [🧪 Data Split](#-data-split)
    - [🧠 Modeling Strategy](#-modeling-strategy)
    - [🧱 Baseline Model (Traditional ML)](#-baseline-model-traditional-ml)
    - [📈 Metrics to Track](#-metrics-to-track)
    - [📂 Outputs to Save](#-outputs-to-save)
    - [🧪 Experiment Tracking](#-experiment-tracking)
    - [📅 Results](#-results)
  - [✅ API Development \& Integration](#-api-development--integration)
    - [🎯 Goal](#-goal)
    - [🧰 Tech Stack](#-tech-stack)
    - [📁 Folder Structure](#-folder-structure)
  - [✅ Testing and Validation](#-testing-and-validation)
    - [🔄 Request-Response Sample](#-request-response-sample)
  - [✅ Deployment](#-deployment)
    - [🎯 Goal](#-goal-1)
    - [🚀 Deployment Checklist](#-deployment-checklist)
  - [✅ UI / Frontend](#-ui--frontend)
    - [🛠️ Tech Stack](#️-tech-stack)
    - [🧱 Features Implemented](#-features-implemented)
    - [🎨 Design Highlights](#-design-highlights)
  - [Documentation \& Reporting](#documentation--reporting)
  - [🔗 Live Site](#-live-site)
  - [🧪 How to Use](#-how-to-use)
  - [📌 Conclusion](#-conclusion)
    - [⚠️ Limitations](#️-limitations)
    - [🚫 Out of Scope](#-out-of-scope)
    - [✅ Possible Future Improvements](#-possible-future-improvements)
  - [🙏 Acknowledgements](#-acknowledgements)

## ✅ Requirements Gathering & Planning

### 📌 Problem Statement

Customer support teams receive hundreds or thousands of tickets daily. These tickets vary in type (bug reports, feature requests, billing issues, etc.) and urgency. Manually triaging them is time-consuming and error-prone.

### 🫡 Objective

Build a system that automatically classifies incoming support tickets by category and priority level using machine learning.

---

### 🎯 Goals & Deliverables

| Goal|Metric| Target Value|
| ----- | ----- | ------ |
| Accurate ticket categorization       | F1-Score, Accuracy             | ≥ 90% Accuracy  |
| Detect priority level (High/Med/Low) | Precision/Recall for High      | ≥ 85% Precision |
| Fast inference                       | API Response Time              | ≤ 300ms         |
| Usable API                           | REST API with `/predict` route | ✅              |
| Scalable system                      | Docker + CI/CD + Deployment    | ✅              |

---

### 🗂️ Ticket Types & Labels (Multi-Class)

We need a dataset with these types of tickets:

- bug
- billing
- feature_request
- technical_issue
- account_problem
- security
- maintenance
- general_inquiry
- other

And with the follwing set of priorities:

- high
- medium
- low

---

### 🧠 Model Plan

Start with:

- TF-IDF + RandomForestClassifier (Baseline)

- Move to better methods for better metrics as required

### 🏗️ Architecture Overview

The planned architecture is shown in the diagram below:

![architecture image](/media/architecture.png)

The steps in the planned architecture are:

1. User / System Submits Ticket →
2. `/predict` route of the api (FastAPI) receives the request→
3. Preprocessing + Inference Pipeline→
4. Response with Category & Priority
5. The response is displayed in the UI

---

### 🧱 Non-Functional Requirements

| Category        | Requirement                       |
| --------------- | --------------------------------- |
| Reliability     | Must not crash on malformed input |
| Latency         | Must respond within 300ms         |
| Scalability     | Dockerized, CI/CD enabled         |
| Security        | Validate inputs, no shell evals   |
| Maintainability | Testable, modular code            |

### 🛠️ Tools & Stack (Preview)

| Phase                                                 | Tool Stack                                          |
| ----------------------------------------------------- | --------------------------------------------------- |
| Data preprocessing(clean, visualze, extract features) | pandas, numpy, matplotlib, seaborn, scikitlearn, scipy  |
| Model Training                                        | scikit-learn                                        |
| Experiment Tracking                                   | MLflow                                              |
| API                                                   | FastAPI, Pydantic                                   |
| Testing                                               | pytest                                              |
| Deployment                                            | Docker, GitHub Actions, Google Cloud Platform       |
| Monitoring                                            | `logging` module, Google Cloud Platform             |
| Frontend                                              | Next.js, TailwindCSS, ShadcnUI, `lucide` for icons |

## ✅ Data Collection & Preprocessing

### 📦 Dataset

Since we need support tickets with categories and priorities:

- The [Customer IT Support - Ticket Dataset](https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets) dataset has been selected. The dataset provides email tickets categorized into departments and priority levels.

- The dataset contains:

  1. Category values: Specifies the department to which the email ticket is categorized. This helps in routing the ticket to the appropriate support team for resolution.

     - 💻 Technical Support: Technical issues and support requests.
     - 🈂️ Customer Service: Customer inquiries and service requests.
     - 💰 Billing and Payments: Billing issues and payment processing.
     - 🖥️ Product Support: Support for product-related issues.
     - 🌐 IT Support: Internal IT support and infrastructure issues.
     - 🔄 Returns and Exchanges: Product returns and exchanges.
     - 📞 Sales and Pre-Sales: Sales inquiries and pre-sales questions.
     - 🧑‍💻 Human Resources: Employee inquiries and HR-related issues.
     - ❌ Service Outages and Maintenance: Service interruptions and maintenance.
     - 📮 General Inquiry: General inquiries and information requests.

  2. Priority values: Indicates the urgency and importance of the issue. Helps in managing the workflow by prioritizing tickets that need immediate attention.

     - 🟢 1 (Low): Non-urgent issues that do not require immediate attention. Examples: general inquiries, minor inconveniences, routine updates, and feature requests.
     - 🟠 2 (Medium): Moderately urgent issues that need timely resolution but are not critical. Examples: performance issues, intermittent errors, and detailed user questions.
     - 🔴 3 (Critical): Urgent issues that require immediate attention and quick resolution. Examples: system outages, security breaches, data loss, and major malfunctions.

### 🔄 Preprocessing

Steps we have applied:

| Step                 | Tool                                     | Purpose                            |
| -------------------- | ---------------------------------------- | ---------------------------------- |
| Text cleaning        | spacy                                    | non-alphanumeric character removal |
| Feature extraction   | sklearn.feature_extraction.text          | extract TF-IDF vectors             |
| Label encoding       | sklearn.OrdinalEncoder                   | Encode category                    |
| Train/val/test split | sklearn.model_selection.train_test_split | Create reusable split              |

---

### 📊 Exploratory Data Analysis (EDA)

We have performed:

- Distribution of ticket categories
  ![ticket-category-distribution-image](/media/ticket-category-distribution.png)

- Distribution of priorities
  ![ticket-priority-distribution-image](/media/ticket-priority-distribution.png)

- Ticket count by category and priority
  ![ticket-count-image](/media/ticket-count.png)

- Distribution of ticket length
  ![ticket-length](/media/ticket-length.png)

- Word cloud
  ![word-cloud](/media/word-cloud.png)

## ✅ Model Training & Evaluation

We aim to build a model that classifies:

- Ticket category (bug, billing, feature_request, etc.)
- Ticket priority (high, medium, low)

This is a multi-class classification problem for both labels.

---

### 🧪 Data Split

Split the dataset for reliable training and evaluation. 80% of the dataset is used for training and 20% is used for evaluation.

---

### 🧠 Modeling Strategy

We'll build two independent classifiers:

- For category
- For priority

### 🧱 Baseline Model (Traditional ML)

We have used TF-IDF + Random Forest to build a fast, reliable baseline.

---

### 📈 Metrics to Track

| Task            | Metrics                                                | Threshold       |
| --------------- | ------------------------------------------------------ | --------------- |
| Category        | Accuracy, Precision, Recll, F1-Score, Confusion Matrix | ≥ 80% Accuracy  |
| Priority        | Accuracy, Precision, Recll, F1-Score, Confusion Matrix | ≥ 75% Precision |
| Inference Speed | Avg. response time (ms)                                | ≤ 300 ms        |

---

### 📂 Outputs to Save

| Artifact                 | Purpose                           |
| ------------------------ | --------------------------------- |
| Trained models (.joblib) | Reuse in API                      |
| Vectorizer               | Needed for consistent predictions |
| Category Encoder         | Reuse in API                      |
| Classification reports   | For model documentation           |
| Confusion matrices       | Visual diagnostics                |

---

### 🧪 Experiment Tracking

Used **MLflow** to track training experiments

Logged:

- Model version
- Hyperparameters
- Accuracy/F1
- Confusion matrix
- Time taken

---

### 📅 Results

| Model               | Accuracy | Precision | Recall | F1-score |
| ------------------- | -------- | --------- | ------ | -------- |
| Category classifier | 66.86%   | 0.6066    | 0.8214 | 0.6781   |
| Priority classifier | 70.65%   | 0.6498    | 0.7812 | 0.66733  |

## ✅ API Development & Integration

### 🎯 Goal

Build a REST API that takes a customer support ticket and returns:

- The predicted category (e.g., bug, billing)
- The predicted priority (e.g., high, medium, low)

---

### 🧰 Tech Stack

| Component        | Tool                | Reason                                                  |
| ---------------- | ------------------- | ------------------------------------------------------- |
| Web Framework    | FastAPI             | Modern, async, Swagger support                          |
| Model Serving    | joblib, Hugging Face Hub | Load .gzip model(from HuggingFace), vectorizer, encoder |
| Input Validation | Pydantic            | Ensure clean user inputs                                |
| Testing          | pytest, httpx       | API unit/integration testing                            |

### 📁 Folder Structure

```bash
app/
├── api/
|      └── v1
|           └── endpoints.py # Routes
├── ml/
|      ├── encoders/ # Encoder file to encode category values
|      ├── models/ # Model files loaded during runtime
|      ├── vectorizers/ # Vectorizer file
|      ├── category_encoder.py # Category encoder class
|      └── models_classes.py # Model classes
├── utils/ # Helper scripts(data cleaning, model_loading etc.)
├── config.py # Global configuration file
└── main.py # FastAPI app
```

## ✅ Testing and Validation

This is where we test and validate that everything behaves as expected, under both normal and edge-case scenarios. It covers:

1. Unit Testing

    - Test individual components
      - Data cleaning functions
      - Category encoders
      - Model classes

2. Integration Testing

    - Test full API routes
      - /predict
      - /health

3. Error & Edge Case Testing

    - Test valid, tricky and invalid inputs
      - Input within the allowed length
      - Input outside the allowed length
      - Invalid input field
      - Empty text field
      - Missing text field
      - Non-text input
      - List input
      - Input with special characters
      - Input with malformed json
      - Response time for maximum length input

---

### 🔄 Request-Response Sample

**Method: POST,
Endpoint: /predict**

- Request:

```json
{
    "text": "My card was charged twice but the invoice shows one payment"
}
```

- Response:

```json
{
    "category": "billing",
    "priority": "high",
    "response_time": 0.245159,
}
```

## ✅ Deployment

### 🎯 Goal

Make the application publicly accessible, scalable, and production-ready.

### 🚀 Deployment Checklist

|Task|Tool/Service|
|----|-------|
|✅ Containerization|Docker|
|✅ Environment Configuration|.env|
|✅ Model Hosting|Hugging Face Hub|
|✅ Web API Hosting|GCP(Cloud Run, for autoscaling, pay-per-use, container support and easy integration with frontend)|
|✅ Logging & Monitoring|Logging module, GCP|
|✅ Health Check Endpoint|/health|
|✅ CI/CD Pipeline|GitHub Actions|
|✅ CORS|FastAPI.middleware.cors|

## ✅ UI / Frontend

In this phase, a user-friendly frontend was developed to interact with the ML ticket triage API. The interface allows users to submit new support tickets and view the predicted department in real-time.

### 🛠️ Tech Stack

|Layer|Technology|
|----|-----|
|Structure|Next.js|
|Styling|Tailwind CSS|
|UI Components| Shadcn UI|
|Icons| Lucide |
|HTTP Requests|Native fetch API|
|Build Tool|Vite (via Next.js)|
|Deployment|Vercel|

---

### 🧱 Features Implemented

1. 📝 Ticket Submission Form

    - A clean form UI built using Tailwind CSS. Includes input fields for describing the issue.

    - A Submit button that triggers API call.

2. 🔁 Real-time department and priority prediction

    On submit, the form:

    - Sends a POST request to the deployed GCP Cloud Run API.

    - Displays the predicted department and priority level returned by the model.

3. 🚨 Error Handling

    Basic error messaging for failed predictions (e.g., server unreachable or invalid input).

4. 🧠 Dynamic UX Feedback

    - Button shows loading state during API call.

    - Input fields are disabled while waiting for the response to prevent multiple submissions.

5. Output Visualization

   - The predictions are shown in an animated pie chart.

### 🎨 Design Highlights

- Mobile-responsive layout using Tailwind's utility classes

- Clean, modern typography

- Form-centric UI focused on clarity

## Documentation & Reporting

|Task|Tool|
|----|----|
|Code Docs| Docstrings, Swagger(FastAPI)|
|Project Docs| README.md |
| Visuals | tldraw, matplotlib, seaborn |

## 🔗 Live Site

You can interact with the deployed app here:
<https://ml-ticket-routing.vercel.app/>

## 🧪 How to Use

![Video demonstration](/media/ticket-classifier-demo.gif)

1. Go to the live frontend

2. Fill out the form:

   - Write a brief message describing the issue
   - Or select from the sample messages

3. Click Submit

The app will display the predicted department and priority level based on your input.

## 📌 Conclusion

### ⚠️ Limitations

The model is trained on a limited dataset and may not generalize well to real-world tickets.

It doesn't handle:

- Multi-label classification (only one department predicted).
- Complex sentences or industry-specific jargon.
- Lacks user authentication and rate limiting.
- No spell-check or typo correction in the input.

### 🚫 Out of Scope

- Ticket assignment to specific agents or queues.
- Multi-language support
- Real-time updates or web sockets
- A full-fledged ticket management system (CRUD, status tracking, etc.)

### ✅ Possible Future Improvements

- 🧠 ML/AI Enhancements

  - A better model.

  - Support multi-label classification where tickets may belong to multiple departments.

  - Integrate confidence scores and show them in the UI.

  - Add explainability features like highlighting important words.

- 📦 API Enhancements

  - Add rate limiting and error monitoring.

---

This project demonstrates a complete end-to-end ML application workflow — from model development to API deployment and UI integration. It simulates how machine learning can enhance support operations by automatically routing tickets, improving efficiency and customer experience.

Although simplified, the system sets the groundwork for a production-ready pipeline. With more real-world data and further enhancements, this can evolve into a robust smart ticket triaging solution.

## 🙏 Acknowledgements

This project uses the [Email Ticket Classification Dataset](https://example.com/dataset-link) made available by [Tobias Bueck(Kaggle)](https://www.kaggle.com/tobiasbueck).

- The dataset contains labeled customer support tickets across multiple categories and was instrumental in training the machine learning classifiers.
- It is used strictly for educational and non-commercial purposes under the licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Full credit goes to the dataset creators for compiling and sharing this resource.
