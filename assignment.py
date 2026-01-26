"""
Activity 1: Refactoring repeated code into functions.
Goal: Replace repeated stats logic with reusable functions.
"""

def calculate_stats(data):
  mean = sum(data) / len(data)
  maximum = max(data)

  return{"mean":mean,"max":maximum}


# Sample data
cat_a = [1, 2, 3, 4, 5]
cat_b = [10, 20, 30]

stats_a = calculate_stats(cat_a)
stats_b = calculate_stats(cat_b)

print("Cat A:", stats_a)
print("Cat B:", stats_b)

#---------------------------------------------------------------------------------------------------------------

""" Activity 2: Build a utility library with reusable functions.
Required functions:
1) calculate_statistics(data)
2) normalize_data(data, method)
3) remove_outliers(data, threshold)
4) train_test_split(data, ratio)
5) encode_labels(labels)
"""

# 1) calculate_statistics(data)
def calculate_statistics(data):
  mean = sum(data) / len(data)
  maximum = max(data)
  minimum = min(data)
  data_range = max(data) - min(data)

  return {"mean":mean,"range":data_range,"max":maximum,"min":minimum}

# test for Function

data1 = [10, 20, 30, 40]


print(calculate_statistics(data1))

#---------------------------------------------------------------------------------------------------------------

# 2) normalize_data(data, method)

def normalize_data(data, method="minmax"):
    min_value = min(data)
    max_value = max(data)
    normalize_data = [(x - min_value) / (max_value - min_value) for x in data]
    return normalize_data


# test
data1 = [10, 20, 30]
print(normalize_data(data1))  # [0.0, 0.5, 1.0]

#---------------------------------------------------------------------------------------------------------------

# 3) remove_outliers(data, threshold)
from typing import List

def remove_outliers(data: List[float], threshold: float) -> List[float]:
    clean_data = [x for x in data if x <= threshold]
    return clean_data

# test 

data = [5.0, 12.5, 8.2, 20.0, 3.3]
threshold = 10.0

cleaned = remove_outliers(data, threshold)
print("before", data)
print("after", cleaned)

#---------------------------------------------------------------------------------------------------------------

# 4) train_test_split(data, ratio)

from typing import List, Tuple

def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
    train_size = int(len(data) * ratio)       
    train = data[:train_size]               
    test = data[train_size:]                 
    return train, test
    
# test 
data = [1,2,3,4,5,6,7,8,9,10]
train, test = train_test_split(data, 0.8)

print("Train:", train)
print("Test:", test)

#---------------------------------------------------------------------------------------------------------------

# 5) encode_labels(labels)

from typing import List, Dict

def encode_labels(labels):
    unique_labels = list(set(labels))        
    numbers = list(range(len(unique_labels))) 
    return dict(zip(unique_labels, numbers)) 

# test
labels = ["cat", "dog", "cat", "bird", "dog"]
encoded = encode_labels(labels)
print(encoded)

#---------------------------------------------------------------------------------------------------------------

"""
Activity 3: Use lambda and .apply() to clean a dataset.
Tasks:
1) Clean price (remove $ and commas)
2) Fill missing quantity with 0
3) Create total = price * quantity
4) Categorize price: low / med / high
"""
#
import pandas as pd

raw = {
   "product": ["Widget A", "Widget B", "Widget C"],
   "price": ["$1,234.50", "$567.89", "$2,345.00"],
   "quantity": [10, 5, None],
}

df = pd.DataFrame(raw)

# 1) Clean price column
df["price"] = df["price"].apply(lambda x: float(x.replace("$","").replace(",","")))

# 2) Fill missing quantity with 0
df["quantity"] = df["quantity"].fillna(0)

# 3) Create total column
df["total"] = df["price"] * df["quantity"]

# 4) Categorize price
df["price_category"] = df["price"].apply(lambda x: "low" if x < 1000 else ("med" if x < 2000 else "high"))

print(df)