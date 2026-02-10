from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ---------------- LOAD DATA ---------------- #

# User–item matrix
user_item_matrix = pd.read_csv(
    "../Milestone_1/user_item_matrix.csv",
    index_col=0
)

# Product descriptions
product_df = pd.read_csv(
    "../Milestone_1/dataset/ecommerce_data.csv",
    encoding="ISO-8859-1"
)

product_map = (
    product_df[['StockCode', 'Description']]
    .drop_duplicates()
    .set_index('StockCode')['Description']
    .to_dict()
)

# ---------------- MODEL ---------------- #

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)

def recommend_products(user_id, top_n=5):
    if user_id not in user_item_matrix.index:
        return []

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:6]
    scores = user_item_matrix.loc[similar_users.index].T.dot(similar_users)
    scores = scores[user_item_matrix.loc[user_id] == 0]

    top_items = scores.sort_values(ascending=False).head(top_n)

    results = []
    for pid, score in zip(top_items.index, top_items.values):
        desc = product_map.get(pid, "Description not available")
        results.append((pid, desc, round(score, 2)))

    return results

# ---------------- DASHBOARD DATA ---------------- #

top_products = (
    product_df.groupby('StockCode')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products_display = [
    (pid, product_map.get(pid, "N/A"), int(qty))
    for pid, qty in top_products.items()
]

# ---------------- ROUTES ---------------- #

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    user_id = None

    if request.method == "POST":
        user_id = int(request.form["user_id"])
        recommendations = recommend_products(user_id)

    return render_template(
        "index.html",
        recommendations=recommendations,
        user_id=user_id,
        top_products=top_products_display,
        total_users=len(user_item_matrix),
        total_products=len(user_item_matrix.columns)
    )

if __name__ == "__main__":
    app.run(debug=True)
