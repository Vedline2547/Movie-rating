# Import necessary libraries
import pandas as pd
import numpy as np
from surprise import SVD
from surprise import Dataset,Reader
from surprise.model_selection import cross_validate,train_test_split
from surprise import accuracy
import seaborn as sns 
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv(r"C:\Users\HP\Desktop\ML\Movie-rating\rating.csv\rating.csv")
df.drop('timestamp',axis=1,inplace=True)
# Display first few rows
print("Dataset Preview: ")
print(df.head())
# Preprocessing dataset
# Define a reader object for surprise
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(df[['userId','movieId','rating']],reader)
# split dataset
trainset,testset = train_test_split(data,test_size=0.2,random_state=42)
# Build collaborative filtering model using SVD
model = SVD()
model.fit(trainset)
# Evaluate model
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)
print(f"RMSE: {rmse:.4f}")
# Make predictions for a specific user and movie
user_id = 196
movie_id = 242
predicted_rating = model.predict(user_id,movie_id).est
print(F"Predicted Rating For Usr {user_id} on {movie_id} : {predicted_rating:.2f}")
# Visualize distribution of rating
plt.figure(figsize=(10,6))
sns.histplot(df['rating'],bins=5,kde=True)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()