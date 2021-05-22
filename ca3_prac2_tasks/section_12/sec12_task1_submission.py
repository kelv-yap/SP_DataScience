import numpy as np

# Read the csv file with the loadtxt() function
filename = "data/singapore-residents-by-ethnic-group-and-sex-end-june-annual.csv"
data = np.loadtxt(filename,
                  skiprows=1,
                  dtype=[('year', 'i8'),
                         ('level_1', 'U50'),
                         ('value', 'i8')],
                  delimiter=",")

# Print out total rows of data in the file
total_rows = str(len(data))
print("There are altogether " + total_rows + " rows of data in the file " + filename)
print()

# Print out the number of years of data captured
data_years = data['year']  # Just extract the year column
years = np.unique(data_years)   # Get the unique values in this column
number_of_years = str(len(years))
from_year = str(min(years))
to_year = str(max(years))
print("There are " + number_of_years + " years of data captured from " + from_year + " to " + to_year)
print()

# Extract only the rows with “Total Residents" in the “level_1” column
keyword = 'Total Residents'
column_to_search = data['level_1']
out = [i for i, v in enumerate(column_to_search) if keyword in v]
data_total_residents = data[out]

# Print out the year which has the highest total number of residents
max = data_total_residents['value'].max()
argmax = data_total_residents['value'].argmax()
print("Year with the highest total number of residents: " + str(data_total_residents[argmax]['year']))
print("Population Count: " + str(max))
print()

# Print out the year which has the lowest total number of residents
min = data_total_residents['value'].min()
argmin = data_total_residents['value'].argmin()
print("Year with the lowest total number of residents: " + str(data_total_residents[argmin]['year']))
print("Population Count: " + str(min))
print()
