import pandas as pd


"""
A program that exctracts data for 3 companies, from 3 Pitchbook CSV files.
Then stores them in a Pandas DataFrame, and saved to a CSV file.

Requires these three Pitchbook Data files in the program directory:
	Company.csv
	CompanyFinancialRelation.csv
	CompanyInvestorRelation.csv

By Fredrik E. Juell, fredrik.e.juell@bi.no, at BI Library.
"""



# Printing column names from three CSV files
print("Column headers in files: ")
c_columns = pd.read_csv("Company.csv", nrows=1).columns.tolist()
print("\nCompany.csv :\n", c_columns)

cfr_columns = pd.read_csv("CompanyFinancialRelation.csv", nrows=1).columns.tolist()
print("\nCompanyFinancialRelation.csv :\n", cfr_columns)

cir_columns = pd.read_csv("CompanyInvestorRelation.csv", nrows=1).columns.tolist()
print("\nCompany.csv :\n", cir_columns)

# Border
print("\n--------------------------------------------------\n")

# Columns of interest (coi). CompanyID is key for later lookups
c_coi = ['CompanyID', 'CompanyName', 'Ticker']
cfr_coi = ['CompanyID', 'NetIncome', 'EnterpriseValue']
cir_coi = ['CompanyID', 'InvestorName']

# Make DataFrames of the columns of interest
c_df = pd.read_csv("Company.csv", usecols=c_coi)
cfr_df = pd.read_csv("CompanyFinancialRelation.csv", usecols=cfr_coi)
cir_df = pd.read_csv("CompanyInvestorRelation.csv", usecols=cir_coi)

# My companies of interest. Must be spelled exactly as in Company.csv
company_names = ['Apple', 'Hertz', 'Intel']

# Empty Dataframe to store result
my_df = pd.DataFrame(columns=['CompanyID','CompanyName','Ticker','NetIncome','EnterpriseValue','InvestorName'])


# Building my_df with my data/companies of interest
i = 0 # index of my_df
for name in company_names:
	# Store companyID
	companyID = c_df.loc[c_df['CompanyName']==name, 'CompanyID'].iloc[0]
	# Use companyID to look up the values with loc, and store them in my_df with loc
	# Using iloc for single value cells. If there are more than one row that matches,
	# this method will only get you the first value.
	my_df.loc[i, 'CompanyID'] = c_df.loc[c_df['CompanyName']==name, 'CompanyID'].iloc[0]
	my_df.loc[i, 'CompanyName'] = name
	my_df.loc[i, 'Ticker'] = c_df.loc[c_df['CompanyID']==companyID, 'Ticker'].iloc[0]
	my_df.loc[i, 'NetIncome'] = cfr_df.loc[cfr_df['CompanyID']==companyID, 'NetIncome'].iloc[0]
	my_df.loc[i, 'EnterpriseValue'] = cfr_df.loc[cfr_df['CompanyID']==companyID, 'EnterpriseValue'].iloc[0]
	# InvestorName has multiple values. Storing it as a python list in the DataFrame cell.
	my_df.loc[i, 'InvestorName'] = list(cir_df.loc[cir_df['CompanyID']==companyID, 'InvestorName'])
	i += 1


# Show the DataFrame
print("Resulting DataFrame:\n", my_df)

# Save it as a CSV file
my_df.to_csv('my_pitchbook_data.csv')

