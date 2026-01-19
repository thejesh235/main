import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset
data = {
    'area': [800, 1000, 1200, 1500, 1800],
    'bedrooms': [1, 2, 2, 3, 3],
    'price': [4000000, 5000000, 6000000, 7500000, 9000000]
}

df = pd.DataFrame(data)

X = df[['area', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Save model
with open('house_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained & saved!")
