# Mushroom Classification Project
by: Gabriela Tijerina 
****

### Project Summary:




**Data Source:** 
****

### Goals:
* 
* 
**** 

### Deliverables:
* README.md file explaining what the project is, how to reproduce our work, and our notes from project planning
* 
* 
**** 

### Data Dictionary

| Features | Description | Data Type |
|---------|-------------|-----------|
|  |  |  |


\* - Indicates the target feature in this data
***


### Data Science Pipeline:

#### 1. Acquire
- Connect to the SQL company database (login credentials required)
- Summarize initial data to determine how data needs to be prepared and cleaned 
- Define functions to:
    - Create a connection url to access the CodeUp's SQL database using personal credentials
    - Acquire Zillow data from MySQL and return as a dataframe
    - Create a .csv file of acquired data 
- All functions to acquire data are included in [acquire.py](link here)

#### 2. Prepare
- Review data and address any missing or erroneous values 
- Define functions to:
    - Clean Zillow data and return as a clean dataframe 
    - Visualize nulls 
    - Handle missing values 
    - Remove columns 
    - Create features 
    - Handle/remove outliers 
- All functions to prepare the data are included in [prepare.py](link here)

#### 3. Explore
- Address questions posed in planning and brainstorming and figure out drivers of log error
- Create visualizations of variables 
- Run statistical tests 
- Summarize key findings and takeaways
- Define functions to:
    - Split the data to explore on the training data set
    - Run univariate, bivariate, and multivariate visualizations for how features interact with each other and the target, logerror
    - Use clustering to further determine features driving log error and engineer new features as discovered
- All functions to explore the data are included in [explore.py](link here)

#### 4. Model/Evaluate
- Goal: develop a model that performs better than the baseline
- Develop a baseline model and linear regression model without controlling for counties
- Iterate process for each of the three counties
- Evaluate if the individualized county models performed better than the all counties model
- Summarize performance, interpret, and document results
- Define functions to:
    - Evaluate model using standard techniques: plotting the residuals, computing the evaluation metrics (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by y-hat
- All functions to evaluate models are included in [evaluate.py](link here)

#### 5. Deliver
- A final Jupyter Notebook [(notebook_name.ipynb)](link here) for presentation that includes discoveries we made and work we have done related to uncovering what the drivers of the error in the Zestimate® are 

### Conclusion:
-  

### Next Steps: 
- 

****

### Instructions for Reproducing Project:  
All files are reproducible and available for download and use. You will need login credentials for access to the Zillow company database.

1.  Read and follow this README.md. 

2.  Download the following files to your working directory:  
 - [file-name.ipynb](link here)
 - [acquire.py](link here)
 - [prepare.py](link here)
 - [explore.py](link here)
 - [evaluate.py](link here)
  

3. Run my final Jupyter Notebook [file-name.ipynb](link here) to reproduce our findings and analysis. 