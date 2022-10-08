# Hacktoberfest 2022 

### K means clustering
K means clustering is an unsupervised learning algorithm. There is no labeled data for this clustering, unlike in supervised learning. K-Means performs the division of objects into clusters that share similarities and are dissimilar to the objects belonging to another cluster.

### Task
You have to create a k means clustering model using the scikit-learn library. The model should return the cluster centers. A graphical representation of the centroid is appreciated.

### Example
```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# create dataset
X, y = make_blobs(
   n_samples=150, n_features=2,
   centers=3, cluster_std=0.5,
   shuffle=True, random_state=0
)

# train the model
km = KMeans(
    n_clusters=3, init='random',
    n_init=10, max_iter=300, 
    tol=1e-04, random_state=0
)

# make the predictions
y_km = km.fit_predict(X)

# plot the centroids
```

### Rules
- Implement the task in `k_means_clustering.ipynb`.
- The model should be able to handle any dataset that is in the same format as the generated blobs dataset.
- Please read the [scikit-learn documentation](https://scikit-learn.org/stable/) to learn how to use the scikit-learn library.
- Please read the [Code of Conduct](../../CODE_OF_CONDUCT.md).

### Style Guide
- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Use docstrings to document the function.
- Use comments to explain the code.

## Maintainer
- [Anamaya](https://www.linkedin.com/in/anamaya1729/)
- [Kartik](https://github.com/kartik007007)
- [Shantanu](https://github.com/neutralWire)
- [Shailesh](https://github.com/ShaileshKumar007)

## License
**This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](../../LICENSE) file for details**

## Happy Coding! :smile: :tada: