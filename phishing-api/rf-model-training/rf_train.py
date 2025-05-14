import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load dataset
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# Step 2: Keep only numeric columns (automatically drops strings)
df = df.select_dtypes(include=["number"])


# Step 3: Split features and labels
X = df.drop("label", axis=1)
y = df["label"]

# Step 4: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 7: Save the model for later use
joblib.dump(model, "rf_model.pkl")


