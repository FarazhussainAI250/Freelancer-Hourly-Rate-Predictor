<img width="1913" height="916" alt="image" src="https://github.com/user-attachments/assets/ad68e947-25e4-42e2-83b2-96b877bf9f92" />

# 💼 Freelancer Hourly Rate Predictor

A machine learning-powered Streamlit web app that predicts the hourly rate of a freelancer based on various features such as job title, country, experience level, etc.

## 🚀 Features

- Predict freelancer hourly rate in real-time using a trained ML model
- Inputs include job title, country, experience level, etc.
- Clean and user-friendly Streamlit UI
- Dataset analysis and model training done in Jupyter notebook

## 📁 Project Structure

```
📦 Freelancer-Hourly-Rate-Predictor
├── app.py                      # Streamlit application
├── global_freelancers.ipynb    # Notebook with EDA and training
├── global_freelancers_raw.csv  # Raw freelancer dataset
├── hourly_rate_predictor.pkl   # Trained ML model
├── requirement.txt             # Python dependencies
```

## 💻 Getting Started

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/FarazhussainAI250/Freelancer-Hourly-Rate-Predictor.git
cd Freelancer-Hourly-Rate-Predictor
```

### 📦 2. Install Dependencies

```bash
pip install -r requirement.txt
```

### ▶️ 3. Run the App

```bash
streamlit run app.py
```

The app will open in your default browser (usually at `http://localhost:8501/`).

## 🧠 Model Details

- Trained using scikit-learn
- Uses preprocessed categorical and numerical features
- Saved model loaded from `hourly_rate_predictor.pkl`

## 📊 Dataset

- File: `global_freelancers_raw.csv`
- Contains features like job title, rate, location, experience, etc.

## 🛠️ Future Additions

- Upload your own CSV to predict hourly rates in bulk
- Model optimization and explainability (SHAP, etc.)
- Global hourly rate map

## 🧾 License

This project is open-source and available under the MIT License.

## 🙋 Contact

For queries or feedback:  
**Faraz Hussain**  
GitHub: [@FarazhussainAI250](https://github.com/FarazhussainAI250)
