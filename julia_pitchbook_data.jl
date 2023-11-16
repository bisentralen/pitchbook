using CSV, DataFrames, DataFramesMeta

"""
A Julia program that exctracts data for 3 companies, from 3 Pitchbook CSV files.
Then stores them in a DataFrame.

Requires these three Pitchbook Data files in the program directory:
	Company.csv
	CompanyFinancialRelation.csv
	CompanyInvestorRelation.csv

By Fredrik E. Juell, fredrik.e.juell@bi.no, at BI Library.
"""

function readColumnNamesOf(csvFiles)
	# Read first line in files
	for file in csvFiles
		println(CSV.File(file, limit=1))
	end
end


# Read CSV
c = CSV.File("Company.csv", select=["CompanyID", "CompanyName", "Ticker"])
cfr = CSV.File("CompanyFinancialRelation.csv", select=["CompanyID", "NetIncome", "EnterpriseValue"])
cir = CSV.File("CompanyInvestorRelation.csv", select=["CompanyID", "InvestorName"])
# Make DataFrames
c_df = DataFrame(c)
cfr_df = DataFrame(cfr)
cir_df = DataFrame(cir)



# My companies of interest. Must be spelled exactly as in Company.csv
company_names = ["Apple", "Hertz", "Intel"]

# Empty DataFrame with columns
my_df = DataFrame(CompanyID=String[],CompanyName=String[],Ticker=String[],NetIncome=Float64[],EnterpriseValue=Float64[],InvestorName=Vector{String}[])


# Build my_df
for name in company_names
	compID = c_df[c_df.CompanyName .== name, :].CompanyID[1]
	tick = c_df[c_df.CompanyName .== name, :].Ticker[1]
	netInc = cfr_df[cfr_df.CompanyID .== compID, :].NetIncome[1]
	entVal = cfr_df[cfr_df.CompanyID .== compID, :].EnterpriseValue[1]
	invName = cir_df[cir_df.CompanyID .== compID, :].InvestorName
	push!(my_df, (compID, name, tick, netInc, entVal, invName); promote=true)
end


# Show it
readColumnNamesOf(["Company.csv", "CompanyFinancialRelation.csv", "CompanyInvestorRelation.csv"])
println(my_df)

