# AI Enabled Recommendation Engine for an E-commerce Platform

## Project Overview
This project focuses on building an AI-enabled recommendation engine for an e-commerce platform to provide personalized product recommendations based on user behavior and interaction patterns. The system aims to enhance user experience and improve product discovery using data-driven techniques.

---

## Project Status
✔ Repository initialized  
✔ Milestone 1 completed  
🔄 Upcoming milestones will be implemented as per the project schedule

---

## Milestones

### ✅ Milestone 1: Data Preparation (Completed)
**Objective:**  
Prepare clean, structured datasets suitable for training recommendation models.

**Tasks Performed:**
- Collected an authentic public e-commerce dataset from Kaggle (Online Retail Dataset)
- Selected relevant user and product attributes
- Handled data inconsistencies such as missing values and negative quantities
- Created a user–product interaction dataset based on purchase quantity
- Constructed a user–item interaction matrix
- Identified top purchased products for basic analysis

**Outputs:**
- Cleaned interaction dataset
- User–item interaction matrix
- Jupyter Notebook demonstrating the full data preparation pipeline

**Note:**  
Due to GitHub file size limitations, large dataset files are not uploaded. All results can be reproduced by running the provided notebook.

---

## ✅ Milestone 2: Model Building (Completed)

**Objective:**  
Develop and train the core recommendation model using the prepared data.

**Approach Used:**  
- User-based Collaborative Filtering  
- Cosine Similarity for user similarity computation  

**Tasks Performed:**
- Loaded user–item interaction matrix from Milestone 1
- Computed similarity between all users using cosine similarity
- Implemented recommendation logic to generate personalized product suggestions
- Tested the model by changing user IDs and observing different recommendations

**Outputs:**
- Trained recommendation model
- Sample personalized recommendations for users

**Note:**  
The model is implemented using Jupyter Notebook inside VS Code. Large data files are excluded due to GitHub file size limitations.

---

### 🔜 Milestone 3:
### 🔜 Milestone 4: 

---

## Repository Structure
Milestone_1/
├── Milestone1.ipynb
├── dataset_info.txt

Milestone_2/
├── Milestone2.ipynb

---

## Technologies Used
- Python
- VS Code  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Scikit-learn  
- Collaborative Filtering  
- Cosine Similarity  
- GitHub  
- Kaggle (Dataset Source)
- Google Colab

---

## Dataset Source
Online Retail Dataset – Kaggle  
https://www.kaggle.com/datasets/carrie1/ecommerce-data

---




