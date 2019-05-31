Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:

# Lesson 2:

- Question: What kind of learning technique does clustering generally fall under?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Unsupervised
	- Choices: Unsupervised; Supervised; Generalized; Parameter

- Question: In k-means what does $$k$$ stand for?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: The number of clusters
	- Choices: The number of clusters; The number of datapoints; The number of features; The number of mean of the clusters

- Question: Typically, how are cluster centers initialized?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Randomly
	- Choices: Randomly; By taking the mean of each feature; By taking the mean of each datapoint; By picking a random feature and finding its mean

- Question: What can the Elbow method be used for with the k-means algorithm?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Finding the best number of clusters
	- Choices: Finding the best number of clusters; Finding the best number of features; Finding the center of the clusters; Finding the best number of datapoints

- Question: In the context of k-means, what is inertia?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: The sum total distance of every point to its cluster center
	- Choices: the sum total distance of every point to its cluster center; the sum total variance of every point to its cluster center; the sum total distance of every cluster to the other clusters; the squared sum total distance of every point to its cluster center

- Question: What is one way to handle high dimensional data with k-means?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Apply dimension reduction first and fit k-means on the reduced data.
	- Choices: Apply dimension reduction first and fit k-means on the reduced data; Don't worry about it; Add more clusters; Randomly drop features

# Lesson3:

- Question: Can DBSCAN determine the number of clusters in an algorithm?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Yes
	- Choices: Yes; No

- Question:What does DBSCAN stand for?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer:Density-based spatial clustering of applications with noise
	- Choices:Density-based spatial clustering of applications with noise; Doubling brackets sparse coding applications noise; Doing bad sparse coding of applications with noise;

- Question:What type of algorithm is DBSCAN?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer:Density-based clustering algorithim
	- Choices:Density-based clustering algorithm; Regression algorithm; Classification algorithm; feature selection algorithm; spatial clustering algorithm

- Question: what is the purpose of the eps hyperparameter in DBSCAN?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Defines the max distance between 2 points for them to be considered in the same density neighborhood
	- Choices: Defines the max distance between 2 points for them to be considered in the same density neighborhood; Defines the min distance between 2 points for them to be considered in the same density neighborhood; Defines the max distance between N points for them to be considered in the same density neighborhood; Defines the min distance between N points for them to be considered in the same density neighborhood

- Question:What is the purpose of the min_samples hyperparameter in DBSCAN?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer:Defines the number of points that must lie within the neighborhood of the current point in order for it to be considered a core point
	- Choices:Defines the number of points that must lie within the neighborhood of the current point in order for it to be considered a core point; Defines the number of points that should not lie within the neighborhood of the current point in order for it to be considered a core point.; Defines the number of points that must lie within the neighborhood of the current point in order for it not to be considered a core point.;

- Question:which class in sci-kit learn contains the implementation for DBSCAN?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.cluster.DBSCAN
	- Choices:sklearn.cluster.DBSCAN; sci-kit.cluster.DBSCAN; DBSCAN; sklearn.Cluster.DBSCAN; sklearn.cluster.dbscan

- Question:As the dimensionality of the data increases, does it become less computationally intensive to use the DBSCAN algorithm?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer:No
	- Choices:No; Yes

- Question: X and y are labels and features that have been defined in Python. What will this snippet of code return? sklearn.cluster.DBSCAN().fit_predict(X, y)
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: returns cluster labels
	- Choices:returns cluster labels; returns DBSCAN model; returns clusters; returns self

# Lesson 4:

- Question: What does GMM stand for?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Gaussian Mixture Model
	- Choices: Gaussian Mixture Model; Gaussian Mass Model; Gaussian Manifold Model; Gaussian Mixture Manifold

- Question: What kind of classification does the GMM provide?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Probabilistic
	- Choices: Probabilistic; Deterministic; Mixture; Gaussian

- Question: What kind of classification does the GMM provide?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Probabilistic
	- Choices: Probabilistic; Deterministic; Mixture; Gaussian

- Question: What algorithm is used to construct the Gaussian Mixture Model?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: EM
	- Choices: EM; GMM; E-step; M-step

- Question: Which can be used to help determine the number of clusters to use for the Gaussian Mixture Model?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: BIC; AIC
	- Choices: BIC; EM; AIC; GMM


- Question: Which of the following are hyperparameters for the Gaussian Mixture Model?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Covariance Type; Number of clusters
	- Choices: Covariance Type; Number of clusters; AIC; Mean type
