# Question 2: How can we create a DataFrame with specific index labels using a dictionary in Pandas?

import numpy as np

# 2. Create a DataFrame from a specified dictionary data with index labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes']
}

# Creating DataFrame with index labels
df_exam = pd.DataFrame(exam_data)

# Display the DataFrame
print("\nDataFrame from the exam_data dictionary with index labels:")
print(df_exam)

# Output:
# DataFrame from the exam_data dictionary with index labels:
#         name  score  attempts qualify
# 0  Anastasia   12.5         1     yes
# 1        Dima    9.0         3      no
# 2  Katherine   16.5         2     yes
# 3      James    NaN         3      no
# 4      Emily    9.0         2      no
# 5   Michael   20.0         3     yes
# 6    Matthew   14.5         1     yes
# 7      Laura    NaN         1      no
# 8      Kevin    8.0         2      no
# 9      Jonas   19.0         1     yes
