import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating synthetic data
fake = Faker()

# Define the number of rows
num_rows = 1000

# Generate synthetic data
data = {
    'job_ad_id': range(1, num_rows + 1),
    'job_city': [fake.city() for _ in range(num_rows)],
    'job_industry': np.random.choice(['Tech', 'Finance', 'Healthcare', 'Education', 'Retail'], num_rows),
    'job_type': np.random.choice(['Software Engineer', 'Data Scientist', 'Machine Learning Engineer', 'Product Manager', 'Web Developer'], num_rows),
    'job_fed_contractor': np.random.choice([True, False], num_rows),
    'job_equal_opp_employer': np.random.choice([True, False], num_rows),
    'job_ownership': np.random.choice(['Private', 'Public'], num_rows),
    'job_req_any': np.random.choice(['Bachelor’s Degree', 'Master’s Degree', 'PhD', 'Associate Degree'], num_rows),
    'job_req_communication': np.random.choice(['Excellent', 'Good', 'Fair'], num_rows),
    'job_req_education': np.random.choice(['Bachelor', 'Master', 'PhD', 'Associate'], num_rows),
    'job_req_min_experience': np.random.randint(0, 10, num_rows),
    'job_req_computer': np.random.choice(['Python', 'R', 'Java', 'SQL', 'JavaScript'], num_rows),
    'job_req_organization': np.random.choice(['Organized', 'Detail-oriented', 'Leadership', 'Creative'], num_rows),
    'job_req_school': [fake.company() for _ in range(num_rows)],
    'received_callback': np.random.choice([True, False], num_rows),
    'firstname': [fake.first_name() for _ in range(num_rows)],
    'race': np.random.choice(['White', 'Asian', 'Black', 'Hispanic', 'Other'], num_rows),
    'gender': np.random.choice(['Male', 'Female', 'Non-Binary'], num_rows),
    'years_college': np.random.randint(2, 6, num_rows),
    'college_degree': np.random.choice(['Bachelor', 'Master', 'PhD', 'Associate'], num_rows),
    'honors': np.random.choice(['Yes', 'No'], num_rows),
    'worked_during_school': np.random.choice([True, False], num_rows),
    'years_experience': np.random.randint(0, 15, num_rows),
    'computer_skills': np.random.choice(['Python, SQL', 'R, Python', 'Java, SQL', 'JavaScript, HTML', 'C++, Java'], num_rows),
    'special_skills': np.random.choice(['Machine Learning', 'Data Analysis', 'Deep Learning', 'Product Strategy', 'Web Design'], num_rows),
    'volunteer': np.random.choice(['Yes', 'No'], num_rows),
    'military': np.random.choice(['No', 'Yes'], num_rows),
    'employment_holes': np.random.randint(0, 5, num_rows),
    'has_email_address': np.random.choice([True, False], num_rows),
    'resume_quality': np.random.choice(['High', 'Medium', 'Low'], num_rows)
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('synthetic_resume_dataset.csv', index=False)

print("Synthetic dataset with 1000 rows created and saved as 'synthetic_resume_dataset.csv'.")
