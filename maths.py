import pandas as pd

df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")

summary = {

    'Total Employees': len(df),

    'Unique departments': df['Department'].unique().tolist(),

    'Employees per Department': df['Department'].value_counts().tolist(),

    'Gender Breakdown': df['Gender'].value_counts().to_dict(),

    'Average Work-life Balance': df['WorkLifeBalance'].mean(),

    'Age': {
        'Min': int(df['Age'].min()),
        'Max': int(df['Age'].max()),
        'Average': int(round(df['Age'].mean()))
},
    'Hourly rate':{
        'Min': int(df['HourlyRate'].min()),
        'max': int(df['HourlyRate'].max()),
        'average': int(round(df['HourlyRate'].mean()))
    },

    'Distance From Home': {
        'min': int(df['DistanceFromHome'].min()),
        'max': int(df['DistanceFromHome'].max()),
        'average': int(df['DistanceFromHome'].mean()),
    },

    'Marital Status (%)': (
    (df['MaritalStatus'].value_counts(normalize=True) * 100)
    .round(2)
    .to_dict()),

    'total Attrition': (df['Attrition'] == 'yes').sum()
}

print(f'{"Key":<15} | {"Value":<25}')
print("-" * 45)

for key, value in summary.items():
    print(f'{key:<15} | {str(value):<25}')


df = pd.read_csv("/Users/becky/Downloads/nurse_attrition 01 10 2025 (1).csv")
print(df.columns)