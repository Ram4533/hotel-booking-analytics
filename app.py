from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data
df = pd.read_csv("cleaned_hotel_bookings.csv")
revenue_trends = pd.read_csv("revenue_trends.csv")
cancellations = pd.read_csv("cancellations.csv")
room_distribution = pd.read_csv("room_distribution.csv")

# Prepare TF-IDF model for search
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["search_text"].astype(str))

# Search function
def search_bookings(query, top_n=5):
    query_tfidf = vectorizer.transform([query.lower()])
    cosine_sim = cosine_similarity(query_tfidf, tfidf_matrix).flatten()
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    return df.iloc[top_indices].to_dict(orient="records")

@app.route("/")
def home():
    return "Hotel Booking Analytics API"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    results = search_bookings(query)
    return jsonify(results)

@app.route("/analytics/revenue_trends", methods=["GET"])
def get_revenue_trends():
    return jsonify(revenue_trends.to_dict(orient="records"))

@app.route("/analytics/cancellations", methods=["GET"])
def get_cancellations():
    return jsonify(cancellations.to_dict(orient="records"))

@app.route("/analytics/room_distribution", methods=["GET"])
def get_room_distribution():
    return jsonify(room_distribution.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
