#  Product Recommendation System

A Content-Based Product Recommendation System built using **Natural Language Processing (NLP)**. The system recommends products similar to a selected product by analyzing product names using **TF-IDF Vectorization** and **Cosine Similarity**.

##  Features

- Content-based recommendation system
- NLP text preprocessing
- TF-IDF Vectorization
- Cosine Similarity for finding similar products
- Interactive Streamlit web application
- Fast recommendations using precomputed similarity matrix

---

##  Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- SpaCy
- Joblib
- Streamlit

---

##  Project Structure

```
Product-Recommendation-System/
│
├── app.py                  # Streamlit application
├── model.ipynb             # Model training notebook
├── products_dataset.csv    # Product dataset
├── products.pkl            # Saved dataframe
├── similarity.pkl          # Cosine similarity matrix
├── tfidf.pkl               # TF-IDF vectorizer
├── requirements.txt
├── README.md
```

---

##  How It Works

1. Load the product dataset.
2. Preprocess the product names.
3. Convert product names into numerical vectors using TF-IDF.
4. Compute cosine similarity between all products.
5. Save the trained objects using Joblib.
6. Load the saved files in Streamlit.
7. Select a product to receive the top 5 similar product recommendations.

---

##  Workflow

```
Product Dataset
       │
       ▼
Text Preprocessing
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Cosine Similarity Matrix
       │
       ▼
Save Model (Joblib)
       │
       ▼
Streamlit Application
       │
       ▼
Top 5 Recommended Products
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Product-Recommendation-System.git
```

### Navigate to the project

```bash
cd Product-Recommendation-System
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Streamlit App

```bash
streamlit run app.py
```

---

##  Model

The recommendation engine uses:

- TF-IDF Vectorizer
- Cosine Similarity

The trained objects are stored using Joblib:

- `tfidf.pkl`
- `similarity.pkl`
- `products.pkl`

---

##  Application

The Streamlit application allows users to:

- Select a product
- Click the recommend button
- View the Top 5 similar products

---



---

##  Author

**Manasi Subhedar**

GitHub: https://github.com/ManasiSubhedar