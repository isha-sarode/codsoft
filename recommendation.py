import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


user_item_data = np.array([
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1]
])


sparse_data = csr_matrix(user_item_data)


knn = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')
knn.fit(sparse_data)


def get_recommendations(user_id, num_recommendations):
    
    distances, indices = knn.kneighbors(sparse_data[user_id])
    
    
    recommended_item_indices = indices[0][1:]
    
    
    return recommended_item_indices
user_id = 4
num_recommendations = 2
recommended_item_indices = get_recommendations(user_id, num_recommendations)
print("Recommended items for user", user_id, ":", recommended_item_indices)