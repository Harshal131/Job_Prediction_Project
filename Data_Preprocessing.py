import pandas as pd

df= pd.read_csv('scraped_jobs.csv')
print(df)


df = df.drop(['Unnamed: 0'], axis =1)

# To remove Nan values from the salary estimate column before splitting the column as it is not possible to perform splitting if the column contains Nan values

df.dropna(subset=['Salary Estimate'], inplace=True)
df['Hourly_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employeer_provided_salary'] = df['Salary Estimate'].apply \
    (lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
remove_k_from_salary = salary.apply(lambda x : x.replace('K' ,'').replace('$' ,''))

hr= remove_k_from_salary.apply(lambda x: x.lower().replace('per hour' ,'').replace('employer provided salary:' ,''))

df['Min_salary' ]= hr.apply(lambda x : int(x.split('-')[0]))
df['Max_salary' ]= hr.apply(lambda x : int(x.split('-')[1]))
df['Avg_salary'] = (df['Min_salary' ] +df['Max_salary']).div(2)

df['Company' ]= df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)
df['State'] = df['Location'].apply(lambda x: x.split(',')[1])

# Replacing Los Angeles
df['State'] = df.State.apply(lambda x: x.strip() if x.strip().lower() != 'los angeles' else 'CA')
df['Similar_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
df['Age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)


def Categorized_title(Job_title):
    if 'data scientist' in Job_title.lower():
        return 'Data Scientist'
    elif 'data engineer' in Job_title.lower():
        return 'Data Engineer'
    elif 'analyst' in Job_title.lower():
        return 'Analyst'
    elif 'machine learning' in Job_title.lower():
        return 'Mle'
    elif 'manager' in Job_title.lower():
        return 'Manager'
    elif 'director' in Job_title.lower():
        return 'Director'
    else:
        return 'NA'


def seniority(Job_title):
    if 'sr' in Job_title.lower() or 'senior' in Job_title.lower() or 'sr' in Job_title.lower() or 'lead' in Job_title.lower() or 'principal' in Job_title.lower():
        return 'Senior'
    elif 'jr' in Job_title.lower() or 'junior' in Job_title.lower():
        return 'Junior'
    else:
        return 'NA'


df['Categorized_title'] = df['Job Title'].apply(Categorized_title)
df['Seniority'] = df['Job Title'].apply(seniority)

df.to_csv('Preprocessed_Data.csv', index=False)