import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("📁 Loading data...")
try:
    df = pd.read_csv('game.csv')
    print("✅ CSV loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'game.csv' not found.")
    exit()

print("🕒 Parsing dates...")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
if df['Date'].isnull().any():
    print("⚠️ Warning: Some dates couldn't be parsed.")

print("🎯 Creating target column...")
df['Long_Play'] = (df['Duration (mins)'] > 60).astype(int)

print("📅 Extracting day of week...")
df['DayOfWeek'] = df['Date'].dt.dayofweek

print("🧼 Encoding categorical data...")
df_encoded = pd.get_dummies(df[['Platform', 'DayOfWeek']], drop_first=True)

print("📊 Defining features and target...")
X = df_encoded
y = df['Long_Play']

print("🔀 Splitting train/test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("🧠 Training model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print("🤖 Predicting on test data...")
y_pred = model.predict(X_test)

print("📈 Evaluating results...")
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Model Accuracy: {accuracy:.2f}")

# Reset indices to ensure alignment
test_data = df.iloc[X_test.index].reset_index(drop=True)  # Reset index here
y_pred = pd.Series(y_pred).reset_index(drop=True)  # Reset index for predictions

# Now both have the same index
results = pd.DataFrame({
    'Game': test_data['Game'],   # Add the 'Game' column
    'Predicted': y_pred,         # Predicted play time (long or short)
    'Actual': y_test.reset_index(drop=True)  # Actual value
})

print("\n🔍 Sample Predictions with Game Names:")
print(results.head(10))  # Show a few results

results.to_csv('predictions_results.csv', index=False)

# Confirm the file has been saved
print("Predictions have been saved to 'predictions_results.csv'")