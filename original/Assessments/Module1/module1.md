Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:

# Lesson 2:

- Question: Which of the following best describes Classification?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Identify which data points are in a set of classes
	- Choices: Identify a functional relationship between input and output attributes; Identify which data points are in a set of classes; Identify (and optionally rank) the most important new dimensions for a data set.; Identify clusters of data points in an $$N$$-dimensional space

- Question: Which of the following best describes Clustering?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Identify clusters of data points in an $$N$$-dimensional space
	- Choices: Identify a functional relationship between input and output attributes; Identify which data points are in a set of classes; Identify (and optionally rank) the most important new dimensions for a data set.; Identify clusters of data points in an $$N$$-dimensional space

- Question: Which of the following best describes Regression?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Identify a functional relationship between input and output attributes
	- Choices: Identify a functional relationship between input and output attributes; Identify which data points are in a set of classes; Identify (and optionally rank) the most important new dimensions for a data set.; Identify clusters of data points in an $$N$$-dimensional space

- Question: Which of the following best describes Dimensionality Reduction?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Identify (and optionally rank) the most important new dimensions for a data set.
	- Choices: Identify a functional relationship between input and output attributes; Identify which data points are in a set of classes; Identify (and optionally rank) the most important new dimensions for a data set.; Identify clusters of data points in an $$N$$-dimensional space

- Question: Which of the following best describes Supervised Learning?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Using training data to build a model
	- Choices: Watching an algorithm while it learns; Using training to provide some level of supervision of in building a model; Building a model that is later applied to data of interest; Using training data to build a model

- Question: Which of the following best describes Unsupervised Learning?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Building a model that is later applied to data of interest
	- Choices: Watching an algorithm while it learns; Using training to provide some level of supervision of in building a model; Building a model that is later applied to data of interest; Using training data to build a model

- Question: Which class or function in sci-kit learn can be used to split training and testing data?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.model_selection.train_test_split
	- Choices: sklearn.model_selection.train_test_split; sklearn.model_selection.split_data; sklearn.model_selection.SplitData; sklearn.model_selection.splitData

- Question: Which forms of data scaling are in scikit-learn?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Binarization; Range; Normalization; Standardization
	- Choices: Binarization; Range; Normalization; Standardization; Privacy; Security

- Question: When dealing with a large, multi-dimensional dataset what approach could we take to simplify any sibsequent analysis?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Dimensionality Reduction
	- Choices: Dimensionality Reduction; Obtaining Powerful Compute Resources; Moving over to Cloud Computing; Using R

- Question: Which class or function in sci-kit learn can be used to perform principal component analysis?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.decomposition.PCA
	- Choices: sklearn.decomposition.PCA; sklearn.decomposition.PrincipalComponentAnalysis; sklearn.decomposition.pca; sklearn.reducedim.PCA

# Lesson 3: 
- Question: scipy.stats has been imported as sts. Assuming x and y are variables that are formatted correctly, how do I compute a linear model of x and y with scipy.stats?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sts.linregress(x, y)
	- Choices: sts.linregress(x, y); sts.regress(x, y), sts.linmodel(x, y), sts.model(x, y)

- Question: Given the following function: $f(x_i) = \beta * x_i + \alpha + \epsilon_i$; what does $\epsilon_i$ represent?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: $\epsilon_i$ accounts for the difference between the model and the data for each data point
	- Choices: $\epsilon_i$ accounts for the difference between the model and the data for each data point; $\epsilon_i$ accounts for the predicted value; $\epsilon_i$ accounts for the actual value; $\epsilon_i$ accounts for the regularzation term; $\epsilon_i$ accounts for the loss function

- Question: When should you expect $\epsilon_i$ to be 0?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: When $y_i = f(x_i)$; If we have a perfect model
	- Choices: When $y_i = f(x_i)$; If we have a perfect model; When $y_i \neq f(x_i)$; If we don't have a perfect model; When the regularzation term is 0; If we are making predictions using Python

- Question: Which parameters from the following function helps reduce $\epsilon_i$: $f(x_i) = \beta * x_i + \alpha + \epsilon_i$?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: $\hat{\beta}$; $\hat{\alpha}$
	- Choices: $\hat{\beta}$; $\hat{\alpha}$; $f(x_i) $; $\hat{\gamma}

- Question: seaborn has been imported as sns. A pandas dataframe df with columns 'x' and 'y' have been initalized as well. How do I use seaborn to create a Regression Plot?
	- Type:  Multiple Choiuce (Single Correct Answer)
	- Answer: sns.regplot(x='x', y='y', data=df)
	- Choices: sns.regplot(x='x', y='y', data=df); sns.regplot(x='x', y='y', data=adfi, fit_reg=False); sns.regressionplot(x='x', y='y', data=df); sns.reg_plot(x='x', y='y', data=df); sns.regPlot(x='x', y='y', data=df);

- Question: What is a common l2-norm?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: $\left( \ y_i - f(x_i) \ \right)^2$, where $f(x_i)$ is defined by our model parameters
	- Choices: $\left( \ y_i - f(x_i) \ \right)^2$, where $f(x_i)$ is defined by our model parameters; $\left( \ y_i - f(x_i) \ \right)^2$, where $f(x_i)$ is defined by another model parameters; $\left( \ y_i - f(x_i) \ \right)^3$, where $f(x_i)$ is defined by our model parameters; $\left( \ y_i + f(x_i) \ \right)^2$, where $f(x_i)$ is defined by our model parameters

- Question: Which function or class in Sklearn can be used for Linear Regression?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.linear_model.LinearRegression
	- Choices: sklearn.linear_model.LinearRegression; sklearn.linear_model.Linear_Regression; sklearn.linear_model.lr; sklearn.linear_model.Regression

- Question: Which function or class in Sklearn can be used for One Hot Encoding
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.preprocessing.OneHotEncoder
	- Choices: sklearn.preprocessing.OneHotEncoder; sklearn.preprocessing.ohe; sklearn.preprocessing.one_hot_encoder; sklearn.preprocessing.onehotencoder

- Question: Which function or class in statsmodels can be used to perform linear regression?
	- Type: 
	- Answer: statsmodels.formula.api.ols
	- Choices: statsmodels.formula.api.ols; statsmodels.formula.api.LinearRegression; statsmodels.formula.api.OrdinaryLeastSquares; statsmodels.formula.api.linear_regression

# Lesson 4:


- Question: The "k" in k nearest neighbors is an example of a:
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Tuning parameter
	- Choices: Tuning parameter; Turning parameter; Priori parameter; Simple parameter

- Question: How many training data points are used by k-NN to classify a new data point?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: k
	- Choices: N; k; NN; All of them

- Question: For which tasks is k-NN typically used?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Classification, Regression
	- Choices: Classification; Normalization; Regression; Scaling

- Question: Which properties does k-NN possess? 
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: non-linear, non-parametric
	- Choices: linear; non-parametric; non-linear; parametric

- Question: Which of the following are hyperparameters of k-NN?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: number of neighbors, weighting scheme
	- Choices: weighting scheme; regression; number of neighbors; density

- Question: What information can be seen from the decision surface?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: How a new observation would be classified
	- Choices: How a new observation would be classified; The number of neighbors used; The weighting scheme used; The regression used  

- Question: The l2-norm gives what type of distance?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Euclidean
	- Choices: Manhattan, Euclidean, Haversine, Chebyshev

- Question: The l1-norm gives what type of distance?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Manhattan
	- Choices: Manhattan, Euclidean, Haversine, Chebyshev

- Question: k-NN is contained in which scikit-learn module?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: neighbors
	- Choices: k_nn, k-neighbors, knn, neighbors


