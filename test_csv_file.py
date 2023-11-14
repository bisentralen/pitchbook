import pandas as pd

"""
Python script that test the CSV file produced by pitchbook_data.py
"""


# Testing file
df = pd.read_csv("my_pitchbook_data.csv")

for row in df['InvestorName']:
	print(row)


