Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:

# Lesson 2:

- Question: How many outcomes are there in a binary classification process?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: 2
	- Choices: 1; 2; 3; 4;

- Question: Which of the following words are used to denote outcomes of a binary process?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Success; Failure
	- Choices: Success; Neutral; Failure; Medium

- Question: Which of the following functions map the real numbers to $$[0,1]$$?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: logit; probit
	- Choices: holdit; logit; bopit; probit; logit

- Question: In words, what is the logit function?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: log odds
	- Choices: odd logs; log odds; error odds; log error

- Question: What phrase best describes a Type I Error?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: False Positive
	- Choices: False Positive; False Negative; True Positive; True Negative

- Question: What phrase best describes a Type II Error?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: False Negative
	- Choices: False Positive; False Negative; True Positive; True Negative

- Question: Formally, how can the marginal effect of a feature be calculated in a logistic regression model?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Taking the partial derivative of the model with respect to the feature of interest
	- Choices: It can't be done; Adding the feature of interest to the model; Subtracting the feature of interest from the model; Taking the partial derivative of the model with respect to the feature of interest

- Question: When using categorical variables in logistic regression, why should you leave one category out of the model?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: To avoid multicollinearity
	- Choices: To avoid convergence; To avoid multicollinearity; To add correlation; To add multicollinearity

# Lesson 3:

- Question: Which of the following can be used to determined how to split a Decision Tree?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Variance Reduction; Gini Impurity; Information gain
	- Choices: Variance Reduction; Gini Impurity; Correlation; Information gain

- Question: What are terminal nodes in a decision tree called?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Leaf nodes
	- Choices: Trunk nodes; Root nodes; Stem nodes; Leaf nodes

- Question: What are terminal nodes in a decision tree called?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Leaf nodes
	- Choices: Trunk nodes; Root nodes; Stem nodes; Leaf nodes

- Question: Which method of sklearn.tree can be used to visualize a decision tree?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: export_graphviz
	- Choices: export_graphviz; export_treeviz; tree_viz; export_tree

- Question: Entropy provides:
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: A statistical measure of the information content; A measure of unexpectedness; A measure of purity
	- Choices: A measure of purity; A statistical measure of the information content; A measure of size; A measure of unexpectedness

- Question: Which of the following quantify how the selection of splitting on a given features affects other features of interest being split?
	- Type: Multiple Choice (Multiple Correct Answers)
	- Answer: Information Gain; Relative Entropy
	- Choices: Information Entropy; Relative Gain; Information Gain; Relative Entropy

- Question: What is the Decision Tree method for classification from sklearn.tree called?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: DecisionTreeClassifier
	- Choices: DecisionTreeClassifier; DecisionTree; DecisionClassifier; TreeClassifier

- Question: How can feature importance be determined in a Decision Tree?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Checking how many times a given feature determines a split
	- Choices: Calculating the Entropy; Checking how many times a given feature determines a split; Checking how many times a given split determines a feature; Calculating the prediction error

- Question: What is the Decision Tree method for regression from sklearn.tree called?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: DecisionTreeRegressor
	- Choices: DecisionTreeRegressor; DecisionTree; DecisionRegressor; TreeRegressor

# Lesson 4:
- Question:  In the Introduction to Support Vector Machine notebook what did the support vector machines perform in code blocks?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: To perform classification.
	- Choices: To perform classification.; To perform regression.; To perform feature selection.; To replace deep learning.

- Question: Which svm kernels are supported in sklearn?
	- Type: Multiple Choice (Multiple Correct Answer)
	- Answer: linear kernel, radial basis function kernel, polynomial kernel, sigmoid kernel, user defined functions
	- Choices: linear kernel, radial basis function kernel, polynomial kernel, sigmoid kernel, user defined functions

- Question: How do I create a support vector machine in sklearn?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: sklearn.svm.SVC()
	- Choices: sklearn.svm.SVC(), sklearn.svm.SVM(), sklearn.SVM(), SVM()

- Question: I have created a support vector machine named *model*. I have 2 numpy arrays X (contains featues) and y (contains labels). How do I train the classier using sklearn?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: model.fit(X, y)
	- Choices: model.fit(X, y); model.train(X, y); model.perform_train(X, y); model(X,y)

- Question: Which library has built-in support for SVMs?
	- Type:  Multiple Choice (Multiple Correct Answer)
	- Answer: sklearn
	- Choices: sklearn; math; random; fuzzywuzzy

- Question: What's the purpose of an ROC curve?
	- Type: Multiple Choiuce Single Correct Answer
	- Answer: To display the relationship between the number of false positives and true positives as a function of probability threshold.
	- Choices: To display the relationship between the number of false positives and true positives as a function of probability threshold.; To display the relationship between the number of true negatives and true positives as a function of probability threshold.; To display the relationship between the number of true negatives and false positives as a function of probability threshold.; 

- Question: If the area under a ROC curve is 0.5 what does this mean?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: My classifer is randomly guessing.
	- Choices: My classifer is not better than randomly guessing; My classifer is  better than randomly guessing; My classifer is very accurate.  my classifer is randomly guessing.

- Question: If the area under a ROC curve is less than 0.5 what does this mean?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: My classifer is not better than randomly guessing;
	- Choices: My classifer is not better than randomly guessing; My classifer is  better than randomly guessing; My classifer is very accurate.  my classifer is randomly guessing.

- Question: If the area under a ROC curve is greater than 0.5 what does this mean?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: My classifer is better than randomly guessing;
	- Choices: My classifer is not better than randomly guessing; My classifer is  better than randomly guessing; My classifer is not very accurate.  my classifer is randomly guessing.

- Question:  According the introduction to svm notebook, what is perhaps the most significant hyperparameter for an SVC?
	- Type: Multiple Choice (Single Correct Response)
	- Answer: the kernel
	- Choices: the kernel; C the peanalty parameter; gamma




