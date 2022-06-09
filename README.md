# STATS170_Project
Capstone Project in conjuction with Accenture

## File Descriptions
- Data Wrangling & Management.ipynb - Notebook for cleaning inconsistent variables and combines data from all years into one
- data_preprocessing.ipynb - Notebook for preprocessing the data for building machine learning models
- exploration.ipynb - Notebook for exploring the data by analyzing certain features in the dataset and creating visualizations
- clean_labels.py - Python script that parses through each ADULT_LABEL.SAS file for each year, stores the variable and its feature in a dataframe, and exports the dataframe as variables12to20.csv
- DatabaseSchema.pdf - PDF document of a database diagram with tables and all the features
- DatabaseSetUp.sql - PostgreSQL code for creating all tables in a PostgreSQL database
- metrics_summary.py - Python script for displaying all the metrics of the machine learning model
- decision_trees.ipynb - Notebook for fitting Decision Tree models
- knn.ipynb - Notebook for fitting K-Nearest Neighbors models
- random_forest.ipynb - Notebook for fitting Random Forest models
- sgd.ipynb - Notebook for fitting Stochastic Gradient Descent models
- xgboost.ipynb - Notebook for fitting XGBoost models
- all_models.ipynb - Notebook for plotting all models ROC curve in one visualization
- model.ipynb - Notebook for showcasing on a small sample of the data
- sample_data.csv - CSV file of a small sample of the entire data

## How To Run (with complete data - not provided due to restricted access)
1. Run Data Wrangling & Management.ipynb
2. Run data_preprocessing.ipynb
3. Run the model you would like to run
    - decision_trees.ipynb for Decision Trees
    - knn.ipynb for K-Nearest Neighbors
    - random_forest.ipynb for Random Forest
    - sgd.ipynb for Stochastic Gradient Descent
    - xgboost.ipynb for XGBoost
4. Run all models to run all_models.ipynb

## How To Run (with sample_data.csv - GitHub Repository for the purpose of our final report)
1. Run project.ipynb