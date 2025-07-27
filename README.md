## 💎 Diamond Price Prediction Web App

A machine learning-based web application that predicts the **price of a diamond** based on its physical characteristics like carat, cut, color, clarity, depth, and table. Built using **Python**, **scikit-learn**, **Flask**, and **HTML/CSS**.

---

### 📌 Table of Contents

* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Project Structure](#-project-structure)
* [How to Run Locally](#-how-to-run-locally)
* [Screenshots](#-screenshots)
* [Future Improvements](#-future-improvements)

---


## ✨ Features

* Train a regression model to predict diamond prices
* Use of real-world dataset with features like:

  * Carat, Cut, Color, Clarity, Depth, Table
* Flask-based web interface
* Clean, responsive frontend with HTML/CSS
* Logs all activities using Python logging
* Exception handling with custom errors
* Modular structure using OOP principles
* Automatically saves trained model and preprocessor as `.pkl` files

---

## 🛠 Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| 🧠 ML Model      | Scikit-learn                    |
| 🧪 Preprocessing | StandardScaler, OrdinalEncoder  |
| 🧰 Backend       | Flask                           |
| 🎨 Frontend      | HTML, CSS                       |
| 📦 Packaging     | Pickle                          |
| 🐍 Language      | Python 3.8+                     |
| 📊 Dataset       | Diamonds dataset (e.g., Kaggle) |

---

## 📂 Project Structure

```
DiamondPricePrediction/
├── artifacts/                # Model and preprocessor storage
├── app/                      # Flask app
│   ├── static/               # CSS files
│   ├── templates/            # HTML files
│   └── app.py                # Main Flask web app
├── src/                      # Core ML pipeline
│   ├── components/           # Data ingestion, transformation, training
│   ├── exception.py          # Custom exception handler
│   ├── logger.py             # Logger configuration
│   ├── pipelines/            # Training pipeline entrypoint
│   └── utils.py              # Utility functions
├── notebooks/                # Data exploration, if any
├── requirements.txt          # All Python dependencies
└── README.md                 # You're here!
```

---

## 💻 How to Run Locally

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/diamond-price-predictor.git
cd diamond-price-predictor
```

### 📦 Step 2: Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 📥 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧠 Step 4: Train the Model

```bash
python -m src.pipelines.training_pipeline
```

This generates:

* `artifacts/model.pkl`
* `artifacts/preprocesssor.pkl`

### 🚀 Step 5: Run the Web App

```bash
cd app
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🖼 Screenshots

![alt text](<Diamond web.png>)
---

## 🚀 Future Improvements

* 📁 Add CSV upload for batch predictions
* 📊 Visualize feature importance
* ☁️ Deploy to Heroku, Render, or AWS
* 🧪 Add unit tests for pipeline components
* 🎨 Add dark mode toggle

---

## 🤝 Credits

* Dataset Source: [Kaggle - Diamond Price Dataset](https://www.kaggle.com/datasets/shivam2503/diamonds)
* Created by: *Aditya Kumar Pandey*

---

## 📄 License

This project is open-source and available under the MIT License.



