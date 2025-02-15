from sentence_transformers import SentenceTransformer
import numpy as np
from scipy.spatial.distance import cosine

# Load local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read comments from file
file_path = r"C:\data\comments.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        comments = [line.strip() for line in file.readlines()]
    print(f"Loaded {len(comments)} comments.")
except FileNotFoundError:
    print("Error: comments.txt not found!")
    exit()

# Get embeddings using local model
embeddings = np.array([model.encode(comment) for comment in comments])

# Compute similarity
min_distance = float("inf")
similar_pair = ("", "")

for i in range(len(comments)):
    for j in range(i + 1, len(comments)):
        distance = cosine(embeddings[i], embeddings[j])
        if distance < min_distance:
            min_distance = distance
            similar_pair = (comments[i], comments[j])

# Save most similar comments
output_path = r"C:\data\comments-similar.txt"
with open(output_path, "w", encoding="utf-8") as file:
    file.write("\n".join(similar_pair))

print(f"Most similar comments saved to {output_path}")
