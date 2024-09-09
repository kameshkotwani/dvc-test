import pandas as pd
from pathlib import Path
import os
data = pd.read_csv("https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv")

data:pd.DataFrame = data.iloc[:,3:]

data = data[data['Length of Membership'] > 3]

data.to_csv(os.path.join('data/raw','customer.csv'),index=False)