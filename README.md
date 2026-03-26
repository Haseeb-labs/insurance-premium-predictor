# Insurance Premium Category Predictor

> An end-to-end machine learning application that predicts an individual's insurance premium category based on personal, lifestyle, and financial inputs.

---

## Overview

This project combines a trained ML model with a **FastAPI** backend and a **Streamlit** frontend to deliver real-time insurance premium category predictions. Users simply enter their details, and the system instantly classifies their premium tier.

---

## Features

- Real-time insurance premium category prediction
- Smart feature engineering:
  - **BMI** — Body Mass Index
  - **Lifestyle Risk** — based on occupation and smoking habits
  - **Age Group** — bucketed age classification
  - **City Tier** — urban classification of the input city
- REST API powered by **FastAPI**
- Interactive UI built with **Streamlit**

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| ML Library | scikit-learn |
| Data Handling | Pandas |

---

## Project Structure

```
insurance-premium-predictor/
│
├── app.py                                  # FastAPI backend
├── frontend.py                             # Streamlit frontend
├── model.pkl                               # Trained ML model
├── requirements.txt                        # Python dependencies
├── insurance_premium_model_training.ipynb  # Model training notebook
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance-premium-predictor.git
cd insurance-premium-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend (FastAPI)

```bash
uvicorn app:app --reload
```

- Backend runs at: `http://127.0.0.1:8000`
- Interactive API docs at: `http://127.0.0.1:8000/docs`

### 4. Run the Frontend (Streamlit)

Open a **new terminal** and run:

```bash
streamlit run frontend.py
```

---

## How It Works

```
User Input (Streamlit UI)
        ↓
POST Request to FastAPI Backend
        ↓
Feature Engineering (BMI, Risk Score, Age Group, City Tier)
        ↓
ML Model Inference (model.pkl)
        ↓
Predicted Premium Category → Displayed in UI
```

---

## Example

**Input:**

| Field | Value |
|---|---|
| Age | 30 |
| Weight | 65 kg |
| Height | 1.7 m |
| Annual Income | 10 LPA |
| Smoker | No |
| City | Mumbai |
| Occupation | Private Job |

**Output:**

```
Predicted Insurance Premium Category: Low
```

---

## Important Notes

- Make sure the **FastAPI backend is running** before launching the Streamlit frontend.
- Verify the API URL in `frontend.py` is set to: `http://127.0.0.1:8000/predict`
- Keep `model.pkl` in the **root directory** of the project.

---

## Future Improvements

- [ ] Add prediction confidence scores
- [ ] Improve and modernize UI design
- [ ] Deploy the application online (e.g., Render, Hugging Face Spaces)
- [ ] Add user authentication
- [ ] Support batch predictions via CSV upload

---
