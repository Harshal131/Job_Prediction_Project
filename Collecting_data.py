import Glassdor_Job_Posting_Scrapper as s
import pandas as pd

path = "C:/Users/Harshal/PycharmProjects/Job_Prediction_Project/chromedriver"

df = s.get_jobs('data scientist',800, False, path, 20)

df.to_csv('scraped_jobs.csv', index = False)
