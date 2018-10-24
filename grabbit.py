# $ pip install pandas
import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_P600_mountains_in_the_British_Isles", header=0)

# Run print(tables) to work out which table you need
df = tables[1]

print(df) # As a DataFrame
print(df.to_json(orient="records", date_format="iso")) # As JSON
df.to_csv("grab.csv", index=False, encoding='utf-8') # Export to CSV
df.to_json("grab.json", orient="records", date_format="iso") # Export to JSON
