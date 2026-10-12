# 🎬 Movie Recommendation System Using SVD

## 📌 Project Overview

This project implements a **Movie Recommendation System** using collaborative filtering and Singular Value Decomposition (SVD). Built with Python and the Surprise library, the system learns patterns from historical user ratings to predict how a user might rate a particular movie.

The project demonstrates how machine learning can power personalized movie recommendations by analyzing user–movie interactions.

## 🎯 Objectives

- Build a collaborative filtering recommendation model using SVD.
- Predict ratings for specific users and movies.
- Evaluate recommendation accuracy using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE).
- Explore movie rating patterns through data visualization.
- Understand the fundamentals of recommender systems.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Pandas** – Dataset loading and preprocessing.
- **Surprise** – Collaborative filtering and SVD implementation.
- **Matplotlib** – Data visualization.
- **Seaborn** – Statistical visualization.

## ⚙️ How It Works

1. **Data Loading:** Load the movie ratings dataset containing user IDs, movie IDs, ratings, and optionally timestamps.
2. **Preprocessing:** Remove unnecessary columns and handle missing values.
3. **Data Splitting:** Divide the dataset into training and testing sets using an 80:20 ratio.
4. **Model Training:** Train an SVD collaborative filtering model on the training data.
5. **Model Evaluation:** Evaluate predictions on the test set using RMSE and MAE.
6. **Rating Prediction:** Estimate the rating a particular user may give to a movie.
7. **Visualization:** Plot the distribution of movie ratings to understand user rating patterns.

## 📂 Project Structure

```text
Movie-rating/
│
├── main.py
├── rating.csv
├── README.md
└── requirements.txt
```

*Note: `rating.csv` is your dataset file. Avoid committing large or restricted datasets to GitHub; provide download instructions when necessary.*

## 📊 Model Evaluation

The model is evaluated using two regression metrics:

- **RMSE (Root Mean Squared Error):** Measures the square root of the average squared difference between actual and predicted ratings. Lower values generally indicate better predictions.
- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted ratings. Lower values generally indicate better predictions.

The actual scores are printed when the program runs. Performance depends on the dataset, its rating scale, and the model configuration.

## 🔮 Example Prediction

The program predicts a rating for user ID `196` and movie ID `242`.

Example output format:

```text
Predicted rating for user 196 on movie 242: 3.85
```

*The rating above is illustrative; your actual prediction will depend on your dataset and trained model.*

The model's prediction is an estimate of the user's likely rating, not a guarantee of how the user will rate the movie.

## 📈 Data Visualization

The project uses Seaborn and Matplotlib to visualize the distribution of movie ratings. This helps identify common rating values and understand the overall rating patterns in the dataset.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/Movie-rating.git
cd Movie-rating
```

### 2. Create a virtual environment (optional but recommended)

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
pandas
numpy
scikit-surprise
matplotlib
seaborn
```

Then install the packages:

```bash
python -m pip install -r requirements.txt
```

### 4. Add the dataset

Place `rating.csv` in the project directory and update the file path in `main.py` if necessary.

The dataset must contain the following columns:

- `userId` – Unique identifier for each user.
- `movieId` – Unique identifier for each movie.
- `rating` – Rating given by the user.
- `timestamp` – Optional rating timestamp.

The rating scale in the code is configured for values from 1 to 5.

### 5. Run the project

```bash
python main.py
```

The program trains the model, displays evaluation metrics, predicts a rating for a selected user–movie pair, and plots the rating distribution.

## 🔧 Future Improvements

- Generate personalized top-N movie recommendations.
- Compare SVD with K-Nearest Neighbors and other collaborative filtering algorithms.
- Tune hyperparameters using cross-validation.
- Incorporate movie genres and other metadata.
- Build an interactive recommendation interface using Streamlit or Flask.
- Deploy the model as a web application.

## 📚 Key Learnings

Through this project, I explored:

- Collaborative filtering and recommender systems.
- Matrix factorization using Singular Value Decomposition.
- Model evaluation with RMSE and MAE.
- Data preprocessing and visualization.
- Building a machine learning workflow with Python.

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | Machine Learning Enthusiast | Python Developer | Future AI Engineer

- GitHub: [Vedline2547](https://github.com/Vedline2547)
- LinkedIn: [Vedline Ochieng](https://www.linkedin.com/in/vedline-ochieng-025146290/)

---

⭐ If you find this project useful, consider starring the repository!
