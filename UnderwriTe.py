import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import joblib

class ReinsuranceBaseModel:
    def __init__(self, model=None):
        # Initialize with a powerful model like XGBoost or LightGBM
        self.model = model or GradientBoostingClassifier()
        self.feature_names = None
        self.preprocessor = None  # Could be a ColumnTransformer

    def load_data(self, data_path):
        """Load and initial preparation of dataset."""
        self.df = pd.read_csv(data_path)
        print("Data loaded successfully.")

    def preprocess_and_engineer_features(self):
        """THE CORE OF THE SOLUTION - To be customized per problem statement."""
        # 1. Clean data (handle missing values, etc.)
        # 2. Create problem-specific features (see Feature Engineering module above)
        # 3. Split into features (X) and target variable (y)
        # Example:
        # self.X = self.df[['feature_1', 'feature_2', 'time_to_claim_days']]
        # self.y = self.df['is_fraud']  # Target variable

        # Placeholder for the specific logic
        print("Feature engineering complete.")

    def train(self):
        """Train the model on the prepared data."""
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2)
        self.model.fit(X_train, y_train)
        # Evaluate model
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model trained. Accuracy: {accuracy:.2f}")

    def predict(self, new_data):
        """Make a prediction on new data."""
        processed_data = self._apply_preprocessing(new_data)
        prediction = self.model.predict(processed_data)
        prediction_proba = self.model.predict_proba(processed_data)
        return prediction, prediction_proba

    def _apply_preprocessing(self, data):
        """Apply the same cleaning and feature engineering to new data."""
        # ... logic to transform a single record for prediction
        return data

    def save_model(self, filepath):
        """Save the trained model for later use."""
        joblib.dump(self.model, filepath)
        print("Model saved.")

# --- How to specialize for Fraud Detection ---
class FraudDetectionModel(ReinsuranceBaseModel):
    def preprocess_and_engineer_features(self):
        # Implement the specific feature engineering for fraud
        # e.g., Create 'time_to_claim_days', 'claim_amount_deviation'
        super().preprocess_and_engineer_features()  # Call base method if needed

# Usage Example:
if __name__ == "__main__":
    # Initialize the specialized model
    fraud_model = FraudDetectionModel()

    # Load the claims dataset
    fraud_model.load_data('claims_data_anonymized.csv')

    # Perform fraud-specific feature engineering
    fraud_model.preprocess_and_engineer_features()

    # Train the model
    fraud_model.train()

    # Save for the hackathon demo
    fraud_model.save_model('fraud_detection_model.pkl')
