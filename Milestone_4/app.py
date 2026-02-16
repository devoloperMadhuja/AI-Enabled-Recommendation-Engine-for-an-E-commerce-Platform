import streamlit as st
import pandas as pd
import pickle
import os
import urllib.parse
import requests
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(page_title="AI E-Commerce System", layout="wide")
st.write("NEW VERSION RUNNING")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    user_item_matrix = pd.read_csv("user_item_matrix.csv", index_col=0)

    with open("user_similarity.pkl", "rb") as f:
        user_similarity_df = pickle.load(f)

    product_lookup = pd.read_csv("product_lookup.csv")
    product_lookup["product_id"] = product_lookup["product_id"].astype(str)

    return user_item_matrix, user_similarity_df, product_lookup

user_item_matrix, user_similarity_df, product_lookup = load_data()

# -------------------------
# LOGIN & SIGNUP SYSTEM
# -------------------------

USER_DB = "users.csv"

# Create users.csv if not exists
if not os.path.exists(USER_DB):
    pd.DataFrame(columns=["username", "password"]).to_csv(USER_DB, index=False)

def load_users():
    return pd.read_csv(USER_DB)

def save_user(username, password):
    users = load_users()
    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USER_DB, index=False)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # ---------------- LOGIN ----------------
    with tab1:
        st.subheader("Login")

        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):

            users = load_users()
            
            users["username"] = users["username"].astype(str).str.strip()
            users["password"] = users["password"].astype(str).str.strip()

            username = username.strip()
            password = password.strip()
            
            user_match = users[
                (users["username"] == username) &
                (users["password"] == password)
            ]

            if not user_match.empty:
                st.session_state.logged_in = True
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

    # ---------------- SIGN UP ----------------
    with tab2:
        st.subheader("Create Account")

        new_username = st.text_input("Choose Username", key="signup_user")
        new_password = st.text_input("Choose Password", type="password", key="signup_pass")

        if st.button("Create Account"):

            users = load_users()

            if new_username in users["username"].values:
                st.error("Username already exists!")
            elif new_username == "" or new_password == "":
                st.error("Fields cannot be empty")
            else:
                save_user(new_username, new_password)
                st.success("Account created successfully! Please login.")

    st.stop()

# -------------------------
# DASHBOARD
# -------------------------

st.sidebar.title("📊 System Dashboard")
st.sidebar.metric("Total Users", len(user_item_matrix.index))
st.sidebar.metric("Total Products", len(user_item_matrix.columns))
st.sidebar.metric("Total Interactions", int(user_item_matrix.sum().sum()))

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# -------------------------
# PRODUCT-BASED RECOMMENDATION
# -------------------------

@st.cache_data
def build_similarity(product_lookup):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(product_lookup["description"].astype(str))
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

cosine_sim = build_similarity(product_lookup)

def recommend_similar_products(product_name, top_n=5):

    product_lookup["description"] = product_lookup["description"].fillna("")
    product_lookup["description_lower"] = product_lookup["description"].str.lower()

    # Split search into words
    words = product_name.lower().split()

    # Create smart mask
    mask = False
    for word in words:
        mask |= product_lookup["description_lower"].str.contains(word, na=False)

    matches = product_lookup[mask]

    if matches.empty:
        return pd.DataFrame()

    idx = matches.index[0]

    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similar_indices = [i[0] for i in similarity_scores[1:top_n+1]]

    return product_lookup.iloc[similar_indices]

#--------------------------
#API
#--------------------------
PEXELS_API_KEY = "J15ihELcs1I9B7Pq30tS1XinE2AEXctQhddp2jpw0djeWWmb0VYlxTz8"

def get_product_image(query):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["photos"]:
            return data["photos"][0]["src"]["medium"]

    return None


# -------------------------
# MAIN PAGE
# -------------------------

st.title("🛍️ AI-Powered E-Commerce Recommendation System")

search_product = st.text_input("Enter Product Name (example: spoon, jar, party, ceramic)")

if st.button("Get Recommendations"):

    results = recommend_similar_products(search_product)

    if not results.empty:

        st.subheader("Recommended Products")

        cols = st.columns(2)

        for i, row in results.iterrows():

            with cols[i % 2]:

                st.markdown(f"### 🛍️ {row['description']}")
                st.write(f"Product ID: {row['product_id']}")

                image_url = get_product_image(row["description"])

                if image_url:
                    st.image(image_url, use_container_width=True)
                else:
                    st.write("No image found")




                st.markdown("---")

    else:
        st.error("No similar products found.")
