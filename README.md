# Insurance-premium-prediction

Sofwares used for the Insuarance-premium-prediction

1.[Python](https://www.python.org/)
2.[Anaconda-navigator](https://www.anaconda.com/products/distribution)
3.[Visual studio code ](https://code.visualstudio.com/)

# Libraries used for Data preparation and modeling

1.Pandas
2.Numpy
3.Matplotlib
4.Seaborn
5.Plotly
6.Sklearn

### Uses of above libraries

1.Pandas used for data loading, preprocessing and modification of the data.
2.NumPy can be used to perform a wide variety of mathematical operations on arrays.
3.Seaborn,matplotlib and plotly are used for Data visualization. with the help of the libraries we understand the data. 4. sklearn is machine learning librariy this is used conver the categorical data to numerical, divided the data into train and test, then finally model buliding used various algorithms to preidct the charges.

# [About the data](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)

## QUESTION: ACME Insurance Inc. offers affordable health insurance to thousands of customer all over the United States. As the lead data scientist at ACME, you're tasked with creating an automated system to estimate the annual medical expenditure for new customers, using information such as their age, sex, BMI, children, smoking habits and region of residence.

#### Estimates from your system will be used to determine the annual insurance premium (amount paid every month) offered to the customer. Due to regulatory requirements, you must be able to explain why your system outputs a certain prediction

# What we do in the data

"The data is taken from the kaggle website. We began the project import the some libraries,these libraries mention above". Netx we check the information data this step we get how many categorical columns and numerical columns in the data. Check the shape,null values. After that we use the statstic function to now the median,mean values. Then we visualize the correlation matrix using he beautiful libraries seaborn after the data preprocessing move to EDA(EXplore data analysis).

"in the EDA process we understand the data, we visualize the some bargraphs,piechart and histograms etc."
Once we done the EDA process then move to the Model buliding before we bulid the model Check the categorical columns are availbel in the data,Firstly we convert the categorical data to numerical they are different methods availbel but we used LabelEncoder the function is avilble in sklearn with the function help convert the data into numerical.Then we divided the data into input and target variabels.

  Once we divided the data into input and target then split the data into train and test using the sklearn librires with the train_test function we used test data 20 % and train data 80% once divided then ready for model fit. This is regression prolem we used Regression algorithms to predict chrages. We used algorithmns in the mode such as
         1) Linear Regression
         2) DecisionTree Regressor
         3)Raandom Forest Regressor
         4) XGB Regresssor
         5) GradientBoostingRegressor
      One install the model then fit the model with train data and we get the prediction of the test data. then we check the model evoluation using the r2_score, along with mean_squared_error.
         From the above algorithms the XGB and GradientBoostingRegressor is given 88% accuracy score then we save the model using the pickle, we dump the model in pickle format with high accuracy alogrithm. Then move to model deploment

# Model deploment

We used flask frame work for the model deploment. in the deploment we load the pickel file, define the functions for the take the inputs form the html format and predict the charges. Once we deployee the model in local system then we run the model in cloud.
