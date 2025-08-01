import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
loan_data = pd.read_csv('Loan_default.csv')

# Preprocessing
label_enc = LabelEncoder()
categorical_cols = ['Education', 'EmploymentType', 'MaritalStatus', 
                    'HasMortgage', 'HasDependents', 'LoanPurpose', 
                    'HasCoSigner']
for col in categorical_cols:
    loan_data[col] = label_enc.fit_transform(loan_data[col])

# Feature and target variables
X = loan_data.drop(['LoanID', 'Default'], axis=1)
y = loan_data['Default']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model to disk
joblib.dump(model, 'rf_model.pkl')
print("Model saved successfully!")
