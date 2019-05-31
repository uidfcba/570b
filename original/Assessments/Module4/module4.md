Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:


# Lesson 2:
- Question: Which of following best describes bias-varience tradeoff?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Finding a model that is complex enough to learn from data but not too complex that is captures noise in the data.
	Choices: Finding a model that is complex enough to learn from data but not too complex that is captures noise in the data.; Finding a model that is not complex enough to learn from data but too complex that is captures noise in the data.; Learning the regularlization term; It is a synonym for cross-validation.

- Question: Which function or Class contains an implementation for LinearRegression in sklearn?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: sklearn.linear_model.LinearRegression
	- Choices: sklearn.linear_model.LinearRegression; sklearn.linear_model.Linear_Regression; sklearn.linear_model.linearregression; sklearn.linear_model.linear_regression

- Question: Are KFold and StratifiedKFold the same type of cross-validation iterator? Why or Why not?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: No. One preserves the relative ratio the other does not of labeled classes.
	- Choices: No. One preserves the relative ratio the other does not of labeled classes.; Yes. They are just synonyms.; No. KFold relies on StratifiedKFold.; Yes. they both use the same algorithm and preserve the relative ratio of labeled classes.

- Question: What class or function contains cross-validation iterators that were talked about in the Introduction to Overfitting notebook?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: sklearn.model_selection
		-Choices: sklearn.model_selection; sklearn.modelSelection; sklearn.ModelSelection; sklearn.mod_sel

- Question: What is the purpose of a validation curve?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: To provide insight into the selection of an optimal hyperparameter value.
	- Choice: To provide insight into the selection of an optimal hyperparameter value.; Shows a convergence in the performance of an estimator on the training and validation data sets; Useful to validate that a model is not stupid.; Makes interesting plots.

	- Question: What is the purpose of a learning curve?
		- Type: Multiple Choice (Single Correct Response)
		- Answer: Shows a convergence in the performance of an estimator on the training and validation data sets
		- Choice: To provide insight into the selection of an optimal hyperparameter value.; Shows a convergence in the performance of an estimator on the training and validation data sets; Useful to validate that a model is not stupid.; Makes interesting plots.

# Lesson 3:

- Question: Which of the following best describes Model Selection?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Choosing the best model for a given dataset
	- Choices: Choosing the best model for a given dataset; Removing bad models from a dataset; Adding parameters to a dataset; Removing parameters from a dataset

- Question: How does Grid Search work?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: It defines a grid of parameter value combinations and finds the best combination
	- Choices: It defines a grid of parameter value combinations and finds the best combination; It randomly tries different combinations of parameters and finds the best combination; It defines a grid of parameter value combinations and finds the worst combination; It randomly tries different combinations of parameters and finds the worst combination

- Question: How does Randomized Grid Search work?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: It randomly tries different combinations of parameters and finds the best combination
	- Choices: It defines a grid of parameter value combinations and finds the best combination; It randomly tries different combinations of parameters and finds the best combination; It defines a grid of parameter value combinations and finds the worst combination; It randomly tries different combinations of parameters and finds the worst combination

- Question: What method from sklearn.model_selection can be used to conduct a Randomized Grid Search?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: RandomizedSearchCV
	- Choices: RandomizedSearchCV; RandomizedSearch; RandomizedCV; GridSearchCV

- Question: What method from sklearn.model_selection can be used to conduct a Grid Search?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: GridSearchCV
	- Choices: GridSearchCV; GridSearch; GridCV; RandomizedSearchCV


# Lesson 4:

- Question: What is regularization primarily used for?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: To prevent overfitting
	- Choices: To prevent overfitting; To encourage overfitting; To scale data; To scale features

- Question: Which of the following best describes overfitting?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: The model works well for training data but does not generalize
	- Choices: The model works well for training data but does not generalize; The model works well for training data and generalizes well; The model does not work well for training data and does not generalize; The model does not work well for training data but generalizes well

- Question: What is the fundamental idea in regularization?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Add additional information to the model selection process to affect the model behavior
	- Choices: Add additional information to the model selection process to affect the model behavior; Remove information from the model selection process to affect the model behavior; Remove parameters from the model; Add data to the model

- Question: What is another name for Ridge Regression?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Tikhonov Regularization
	- Choices: Tikhonov Regularization; Ridge Regularization; Brunner Regularization; 0-Regulariztion

- Question: What does Ridge Regression do?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Adds a penalty term which is the l2-norm of the coefficients
	- Choices: Adds a penalty term which is the l2-norm of the coefficients; Adds a penalty term which is the sum of the coefficients; Adds the l2-norm of the coefficients to each coefficient; Adds a penalty term which is the l1-norm of the coefficients
