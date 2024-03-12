# to perform backtest
from untrade.client import Client


client = Client()

csv_file_path = "/Users/siddharthjain/Downloads/zelta_tech_7Feb_1.csv"  # must be in this formate:{datetime,open,high,low,close,volume,signals}

result = client.backtest(
    file_path=csv_file_path,
    leverage=1,
)

# Result is a generator object that can be iterated over to get the results
for i in result:
    print(i)

# Params and there default values
# leverage = 1
# chain = False
# commission = 0.15


## File Requirements

# **Format:** CSV (Comma-Separated Values)

# **Content Structure:** The CSV file must include the following headers in the exact order:

# - Index (int)
# - datetime (datetime) : Format YYYY-MM-DD HH:MM:SS
# - open (float)
# - high (float)
# - low (float)
# - close (float)
# - volume (float)
# - signals (int)

# Each row in the file should represent a different time point in the dataset.
