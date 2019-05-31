Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:

# Lesson 2:

- Question: What key simplifying assumption is made by the Naive Bayes Algorithm?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Features are independent given the class
	- Choices: Features are independent; Features are independent given the class; The data are independent; The data are features

- Question: Which distributions are commonly used by the Naive Bayes Algorithm?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Bernoulli; Multinomial; Gaussian
	- Choices: Bernoulli; Poisson; Multinomial; Gaussian

- Question: Which distribution should you use with the Naive Bayes Algorithm for continuous features?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Gaussian
	- Choices: Bernoulli; Poisson; Multinomial; Gaussian

- Question: Which distribution should you use with the Naive Bayes Algorithm for discrete binary features?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Bernoulli
	- Choices: Bernoulli; Poisson; Multinomial; Gaussian

- Question: Which distribution should you use with the Naive Bayes Algorithm for features with discrete mutually exclusive options?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Multinomial
	- Choices: Bernoulli; Poisson; Multinomial; Gaussian

- Question: Which of the possible classes does Naive Bayes typically select for the final classification?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: The class with the highest probability
	- Choices: The class with the highest probability; The class with the lowest probability; The feature with the highest probability; The feature with the highest probability

# Lesson3:
- Question: If a Gaussian distrbution is used to model data is the marginal distribution of any sibset of elements from a multivariate distribution normal?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Yes
	- Choices: Yes; No

- Question:For a Gaussian process which answer below best defines the infinite dimension.
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: An infinite collection of random variables, with any marginal subset having a Gaussian distribution.
	- Choices:An infinite collection of random variables, with any marginal subset having a Gaussian distribution.; A finite collection of random variables, with any marginal subset having a Gaussian distribution.; An infinite collection of non-random variables, with any marginal subset having a Gaussian distribution.; An finite collection of non-random variables, with any marginal subset having a Gaussian distribution.

- Question:Which libraries includes classes and/or functions tailored to Gaussian Process Models?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: scikit-learn; GPflow; PyMC3
	- Choices: scikit-learn; GPflow; PyMC3; math; matplotlib

- Question: Which library in sklearn contains a class that can create a Gaussian Process Regressor?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.gaussian_process.GaussianProcessRegressor
	- Choices: sklearn.gaussian_process.GaussianProcessRegressor; sklearn.gaussian_process.GaussianProcessClassifier; sklearn.gaussianProcess.GaussianProcessRegressor; sklearn.gaussianprocess.GaussianProcessRegressor

	- Question: Which library in sklearn contains a class that can create a Gaussian Process Classifer?
		- Type: Multiple Choice (Single Correct Answer)
		- Answer: sklearn.gaussian_process.GaussianProcessClassifier;
		- Choices: sklearn.gaussian_process.GaussianProcessRegressor; sklearn.gaussian_process.GaussianProcessClassifier; sklearn.gaussianProcess.GaussianProcessRegressor; sklearn.gaussianprocess.GaussianProcessRegressor

- Question: X and y are features and labels respectively. A GaussianProcessClassifier has been created from scikit-learn and defined as gpc. How do I fit gpc on the features and labels?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer:gpc.fit(X,y)
	- Choices: gpc.fit(X,y); gpc.fit(x,y); gpc.fit(y,X); gpc.fit(gpc, X, y)

- Question:Which of the following covariance functions are available in scikit-learn?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: ConstantKernel; Sum; Product; White Kernel; Radial Basis Function Kernel; Matern kernel; Dot-Product kernel; Exp-Sine-Squared kernel
	- Choices: ConstantKernel; Sum; Product; White Kernel; Radial Basis Function Kernel; Matern kernel; Black Kernel; Dot-Product kernel; Exp-Sine-Squared kernel; Red Kernel; random chair

- Question: Whats the primary hyperparameter for a gaussian process?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Kernel
	- Choices: Kernel; alpha; optimizer; random_state
