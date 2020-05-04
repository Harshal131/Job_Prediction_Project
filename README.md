# Job_Prediction_Project

 * Scrapped 800 job descriptions from glassdoor using python and selenium.

 * Created a tool that estimates salaries of data scientists to help them to negotiate their salaries with
   their future prospective employers.

 * Feature engineered text of each job description to quantify the value companies put on Python, R,
     SQL, Spark, AWS, Tableau, Excel.

 * Optimized Multiple Linear, Support Vector, and Random Forest Regressors using
   RandomizedSearchCV to reach the best model.

 * Built a client facing API using flask.

## Code and Resources Used

**Python Version** : 3.8.2

**Packages** : pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

**For Web Framework Requirements** : pip install -r requirements.txt

**Project was inspired by Ken Jee's project walkthrough** : https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

**Scraper to scrap glassdoor job description using selenium**: https://github.com/arapfaik/scraping-glassdoor-selenium

**Pandas cheat sheet** : https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

**Flask Productionization** : https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping for Job postings from Glassdoor.com

Scraped 800 job postings from glassdoor.com. With each job, got the following :

 * Job title
 * Salary Estimate
 * Job Description
 * Rating
 * Company
 * Location
 * Company Headquarters
 * Company Size
 * Company Founded Date
 * Type of Ownership
 * Industry
 * Sector
 * Revenue
 * Competitors

## Data Preprocessing

* Parsed numeric data out of salary
* Parsed rating out of company text
* Made a new column for company state
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
   * Python
   * SQL
   * Tableau
   * R
   * Excel
   * AWS
   * Spark
* Column for simplified job title and Seniority
* Column for description length

## Exploration Data Analysis (EDA)

Below are a few highlights from the pivot tables.

![alt text](https://github.com/Harshal131/Job_Prediction_Project/blob/master/EDA_findings/Corealtion%20Matrix.png "Corelation Matrix")
![alt text](https://github.com/Harshal131/Job_Prediction_Project/blob/master/EDA_findings/Sectors%20investment%20in%20data%20scientist.png "Job Opportunities by different Sectors")
![alt text](https://github.com/Harshal131/Job_Prediction_Project/blob/master/EDA_findings/State%20investment%20in%20data%20scientist.png "Job Opportunities by different States")

![alt text](https://github.com/Harshal131/Job_Prediction_Project/blob/master/EDA_findings/Ownerships%20investment%20in%20data%20scientist.png "Job Opportunities by different Ownerships" )
![alt text](https://github.com/Harshal131/Job_Prediction_Project/blob/master/EDA_findings/Companies_Revenue.png "Companies Revenue")

## Model Evaluation 

The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**MAE for multiple linear regression** > 19.066906227757443
* **MAE for support vector regression** > 29.64442258302692
* **MAE for random forest** > 15.539098732093738

## Productionization 

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the towards data science tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 

