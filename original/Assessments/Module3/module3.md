Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:

# Lesson 2:

- Question: What is bagging short for?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: Bagging is short for bootstrap aggregation.
	- Choices: Bagging is short for bootstrap aggregation.; Bagging is short for Baggingnoplis.; Bagging is short for deep learning. Bagging is short for bootstrap propogation. Bagging is short for back propogation.

- Question: What is the concept behind bagging?
	- Type: Multiple choice (Single Correct Response)
	- Answer: Trees are made with subsets of the data. Each tree is consider a weak learner. A more powerful estimator is constructed as a by product of many weak learners.
	- Choices: Trees are made with subsets of the data. Each tree is consider a weak learner. A more powerful estimator is constructed as a by product of many weak learners.; Trees are made with subsets of the data. Each tree is consider a strong learner. A more powerful estimator is constructed choosing 1 strong learner.; Trees are made with all of the data. Each tree is consider a strong learner. A more powerful estimator is constructed as a by product of many strong learners.

- Question: What is the purpose of the base_estimator hyperparameter in a BaggingClassifier or BaggingRegressor?
	- Type: Single Choice (Single Correct Response)
	- Answer: The estimator to use on each sample, by default this is a decision tree.
	- Choices: The estimator to use on each sample, by default this is a decision tree.; The number of base estimators to create for the ensemble, by default this is ten.; The number of instances to draw from the parent population to train each base estimator, by default this is one.; The number of features to draw from the parent population to train each base estimator, by default this is one.

- Question: What is the purpose of the n_estimators hyperparameter in a BaggingClassifier or BaggingRegressor?
	- Type: Single Choice (Single Correct Response)
	- Answer: The number of base estimators to create for the ensemble, by default this is ten.
	- Choices: The estimator to use on each sample, by default this is a decision tree.; The number of base estimators to create for the ensemble, by default this is ten.; The number of instances to draw from the parent population to train each base estimator, by default this is one.; The number of features to draw from the parent population to train each base estimator, by default this is one.

- Question: What is the purpose of the max_samples hyperparameter in a BaggingClassifier or BaggingRegressor?
	- Type: Single Choice (Single Correct Response)
	- Answer: The number of instances to draw from the parent population to train each base estimator, by default this is one.
	- Choices: The estimator to use on each sample, by default this is a decision tree.; The number of base estimators to create for the ensemble, by default this is ten.; The number of instances to draw from the parent population to train each base estimator, by default this is one.; The number of features to draw from the parent population to train each base estimator, by default this is one.

- Question: What is the purpose of the max_features hyperparameter in a BaggingClassifier or BaggingRegressor?
	- Type: Single Choice (Single Correct Response)
	- Answer: The number of features to draw from the parent population to train each base estimator, by default this is one.
	- Choices: The estimator to use on each sample, by default this is a decision tree.; The number of base estimators to create for the ensemble, by default this is ten.; The number of instances to draw from the parent population to train each base estimator, by default this is one.; The number of features to draw from the parent population to train each base estimator, by default this is one.

- Question: Formally what is a Bootstrap?
	- Type: Single Choice (Single Correct Response)
	- Answer: Bootstrap refers to any statistical process that relies on the generation of random samples with replacement.
	- Choices: Bootstrap refers to any statistical process that relies on the generation of random samples with replacement; ootstrap refers to any statistical process that relies on the generation of random samples without replacement.; Bootstrap refers to any statistical process that does not rely on the generation of random samples with replacement.; Bootstrap refers to any statistical process that does not rely on the generation of random samples without replacement.

- Question: When using a Random forest is it required to shift and scale your data during training?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: No
	- Choices: No; Yes

- Question: Can Random Forest Tress only perform classification?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: No
	- Choices: No; Yes

# Lesson 3:

- Question: Which term is used to describe combining many weak learning algorithms and then producing a stronger one via generating unequal weights for training data?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Boosting
	- Choices: Bagging; Boosting; Roosting; Nagging;

- Question: Which boosting algorithm supports arbitrary cost or loss functions?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Gradient Tree Boosting
	- Choices: Gradient Tree Boosting; Adaboost; Random Boost; Gradient Adaboost

- Question: What does the "n_estimators" hyperparameter of the Gradient Boosting Algorithm in Python control?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: The number of individual learners at each iteration
	- Choices: The number of individual learners at each iteration; The amount of training data used; The number of iterations; The number of features

- Question: What type of plot can be used to show the relationship between the model and a specific set of features?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Partial dependence plot
	- Choices: Independence plot; Dependence plot; Partial independence plot; Partial dependence plot

- Question: What does the "learning_rate" hyperparameter of the Adaboost algorithm in Python control?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: How each successive iteration affects the boosting process
	- Choices: The number of individual learners at each iteration; How each successive iteration affects the boosting process; The number of iterations; The number of features

- Question: Which method from scikit learn allows us to view the accuracy of a boosting algorithm at each estimator?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: staged_predict
	- Choices: staged_predict; predict_stage; f1_score; stage_accuracy



# Lesson 4:

- Question:  Can every class in sci-kit learn be used in sklearn's implementation of a Pipeline?
	- Type: Multiple Choice (Single Response Answer)
	- Answer: No
	- Choices: No; Yes

- Question: What is a quick test that you can perform to see if a class can be used in sklearn?
	- Type: Multiple choice (Single Response Answer)
	- Answer: Check if the class has a transformation method
	- Choices: Check if the class has a transformation method; Check if the class has a predict method; Check if the class has a fit method; Check if the class has a get_params method

- Question: Which class or function do I use to create a Pipeline object in sklearn?
	- Type: Multiple choice (Single Response Answer)
	- Answer: sklearn.pipeline.Pipeline
	- Choices: sklearn.pipeline.Pipeline; sklearn.pipeline; sklearn.Pipeline; Pipeline

- Question: Which best defines "hard" voting?
	- Type: Multiple choice (Single Response Answer)
	- Answer: majority voting based on input classifications
	- Choices: majority voting based on input classifications; majority voting on summed classification probabilities;minority voting based on input classifications; minority voting on summed classification probabilities 

- Question: Which best defines "soft" voting?
	- Type: Multiple choice (Single Response Answer)
	- Answer: majority voting on summed classification probabilities
	- Choices: majority voting based on input classifications; majority voting on summed classification probabilities;minority voting based on input classifications; minority voting on summed classification probabilities 

- Question: Which best defines the term for filling in missing values?
	- Type: Multiple choice (Single Response Answer)
	- Answer: Imputing
	- Choices: Imputing; Preprocessing; Standardizing; Pipeline

- Question: What does the StandardScaler method from sklearn.preprocessing do?
	- Type: Multiple choice (Single Response Answer)
	- Answer: Transform data to have zero mean and unit standard deviation
	- Choices: Transform data to have zero mean and unit standard deviation; Transforms data to lie between a minimum and maximum value, often the range [0, 1] ; Transforms data to lie between a zero and maximum value; Transform data to have unit mean

- Question: What does the Binarizer method from sklearn.preprocessing do?
	- Type: Multiple choice (Single Response Answer)
	- Answer: Threshold numerical features to generate a new, Boolean feature
	- Choices: Threshold numerical features to generate a new, Boolean feature; Transforms data to lie between a minimum and maximum value, often the range [0, 1] ; Transforms data to lie between a zero and maximum value; Transform data to have unit mean
