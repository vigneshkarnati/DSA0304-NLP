from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Python is used for machine learning",
    "Machine learning is a branch of artificial intelligence",
    "Natural language processing uses machine learning"
]

query = "Python machine learning"

vectorizer = TfidfVectorizer()

# Convert documents and query into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Separate document vectors and query vector
document_vectors = tfidf_matrix[:-1]
query_vector = tfidf_matrix[-1]

# Calculate cosine similarity
similarities = cosine_similarity(query_vector, document_vectors)[0]

# Rank documents
ranking = sorted(
    enumerate(similarities),
    key=lambda x: x[1],
    reverse=True
)

print("Document Ranking:")

for index, score in ranking:
    print(
        "Document", index + 1,
        "-> Score:", round(score, 4),
        "->", documents[index]
    )