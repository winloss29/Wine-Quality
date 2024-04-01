import pandas as pd

# Importing the dataset
data = pd.read_csv("C:/Users/Vijayvardhan reddy/Desktop/Wine_Quality_Data.csv")
# Creating the target variable 'y'
data['y'] = (data['color'] == 'red').astype(int)
# Step 3: Pair Plot for a Subset of Features
subset_columns = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'quality']
sns.pairplot(data[subset_columns])
plt.show()
# Calculating correlations with the target variable 'y'
correlations = data.corr()['y'].drop('y')

# Creating a bar plot
plt.figure(figsize=(10, 6))
correlations.abs().sort_values(ascending=False).plot(kind='bar')
plt.title('Correlations with Target Variable (Absolute Values)')
plt.xlabel('Features')
plt.ylabel('Absolute Correlation')
plt.show()
# Selecting the two most correlated fields
top_2_correlated_features = correlations.abs().nlargest(2).index
X = data[top_2_correlated_features]
from sklearn.preprocessing import MinMaxScaler

# Scaling X using MinMaxScaler
scaler = MinMaxScaler()
X_scaled_array = scaler.fit_transform(X)
# Converting scaled X back to a DataFrame and renaming columns
X_scaled = pd.DataFrame(X_scaled_array, columns=X.columns)
X_scaled.columns = ['scaled_' + col for col in X_scaled.columns]

# Displaying the first few rows of the scaled X DataFrame
print(X_scaled.head())
