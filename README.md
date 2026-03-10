# 🛍️ AI-Enabled Recommendation Engine for an E-Commerce Platform

---

## 📌 Project Overview

Modern **e-commerce platforms contain thousands of products**, making it difficult for users to quickly find relevant items. A recommendation system helps users discover products based on their **behavior, interests, and purchase history**.

This project develops an **AI-enabled Hybrid Recommendation System** that generates **personalized product suggestions** using machine learning techniques.

The system combines:

- **User-Based Collaborative Filtering**
- **Content-Based Filtering (TF-IDF)**
- **Cosine Similarity**
- **Ranking-based Evaluation Metrics**

---

## 🎯 Project Objectives

The primary goal of this project is to:

- Improve **user experience**
- Enhance **product discovery**
- Provide **personalized recommendations**
- Increase **customer engagement**
- Support intelligent **product suggestions**

---

## 🚀 Project Status

| Milestone | Description | Status |
|----------|-------------|--------|
| Milestone 1 | Data Preparation | ✅ Completed |
| Milestone 2 | Model Building | ✅ Completed |
| Milestone 3 | Evaluation & Refinement | ✅ Completed |
| Milestone 4 | System Deployment | ✅ Completed |

---

## 🏗 System Architecture

```
User Login / Product Search
          ↓
   Streamlit Web Application
          ↓
   Recommendation Engine
      ↙            ↘
Collaborative   Content-Based
  Filtering     Filtering (TF-IDF)
          ↓
   Cosine Similarity Ranking
          ↓
   Top-N Product Recommendations
          ↓
 Dynamic Product Images (API)
          ↓
      Final Output
```

---

# 📊 Milestone Implementation

---

## ✅ Milestone 1 – Data Preparation

### Objective
Prepare a **clean and structured dataset** suitable for building the recommendation model.

### Tasks Performed

- Collected **Online Retail Dataset from Kaggle**
- Selected relevant columns:
  - Customer ID
  - Product ID (StockCode)
  - Quantity
  - Invoice Date
- Removed **missing values**
- Removed **negative quantities (returns)**
- Created **User-Item Interaction Dataset**
- Built the **User-Item Interaction Matrix**
- Performed **basic exploratory analysis**

### Output

The dataset was successfully cleaned and transformed into a **structured interaction matrix used for training the recommendation system**.

![Milestone1 Output](images/milestone1_output.png)

---

## ✅ Milestone 2 – Model Building

### Objective
Develop the **core recommendation model** capable of generating personalized product suggestions.

### Approach Used

**User-Based Collaborative Filtering**

### Implementation Steps

- Loaded the **User-Item Interaction Matrix**
- Computed **user similarity using cosine similarity**
- Identified **Top-K similar users**
- Generated **personalized recommendations**
- Tested the model with different user IDs

### Output

The model successfully generated **product recommendations based on user similarity**.

![Milestone2 Output](images/milestone2_output.png)

---

## ✅ Milestone 3 – Evaluation & Refinement

### Objective
Evaluate the recommendation model and improve its performance.

### Evaluation Metrics Used

- **Precision**
- **Recall**
- **F1-Score**

⚠ Traditional accuracy is **not suitable for recommendation systems**.

### Improvements

- Tuned number of **similar users**
- Adjusted **Top-N recommendations**
- Optimized **ranking logic**

### Output

Evaluation confirmed that the model provides **relevant recommendations**.

![Milestone3 Output](images/milestone3_output.png)

---

## ✅ Milestone 4 – System Deployment

### Objective
Deploy the recommendation engine with a **user-friendly web interface**.

### Deployment Platform

**Streamlit Web Application**

### Features Implemented

- User **Login & Signup System**
- **Session Management**
- **Keyword-based Product Search**
- **Real-time Recommendations**
- **TF-IDF Content Similarity**
- **Dynamic Product Images using API**
- **Dashboard Metrics**
- **Responsive UI**

### Output

A **fully functional AI-powered recommendation system** capable of generating product suggestions in real time.

![System Output](images/milestone4_output.png)

---

## 🔥 Recommendation Strategy (Hybrid Model)

This system combines two recommendation approaches.

### Collaborative Filtering

- Uses **user purchase behavior**
- Finds **similar users**
- Recommends products purchased by similar users

### Content-Based Filtering

- Uses **product descriptions**
- Applies **TF-IDF Vectorization**
- Computes product similarity using **cosine similarity**

✔ This hybrid model improves **recommendation relevance and personalization**.

---

## 📈 Business Impact

An AI-powered recommendation system can help e-commerce platforms:

- Increase **user engagement**
- Improve **product discoverability**
- Boost **conversion rates**
- Improve **customer retention**
- Reduce **search effort**

---

## 🗂 Repository Structure

```
Milestone_1/
│ ├── Milestone1.ipynb
│ ├── user_item_matrix.csv
│ └── product_lookup.csv

Milestone_2/
│ ├── Milestone2.ipynb
│ └── user_similarity.pkl

Milestone_3/
│ └── Milestone3.ipynb

Milestone_4/
│ ├── app.py
│ ├── users.csv
│ ├── static/
│ └── templates/

README.md
requirements.txt
```

---

## 🛠 Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**
- **Streamlit**
- **Jupyter Notebook**
- **VS Code**
- **GitHub**
- **Kaggle Dataset**
- **Pexels API**

---

## 🔮 Future Enhancements

- Deep Learning Recommendation Models
- Cloud Deployment (AWS / GCP / Azure)
- Real-time Database Integration
- Cold-Start Problem Handling
- Rating Prediction System
- Large-scale Production Deployment

---

## 👩‍💻 Author

**Madhuja Deb Adhikari**  
AI-Enabled Recommendation Engine Project
