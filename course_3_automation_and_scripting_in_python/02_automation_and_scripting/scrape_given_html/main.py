# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())

# Step 3.2: Extract the Required Data
table = soup.find("table")

headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

data = []

for row in table.find("tbody").find_all("tr"):
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
    row_dict = dict(zip(headers, cells)) # map headers to row values
    data.append(row_dict)

for game in data:
    print(game)
# Step 4.1: Convert to a DataFrame
# Import pandas
import pandas as pd

# Convert the game data into a pandas DataFrame
df = pd.DataFrame(data)

# Inspect the DataFrame
print(df)

# Save and print the shaped data
shape = df.shape
print(f"DataFrame Shape: {shape}")

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
df.to_csv("sports_statistics.csv", index=False)