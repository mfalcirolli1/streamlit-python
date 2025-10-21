from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

class MachineLearningUseCase:

    def __init__(self, model, data_preprocessor):
        self.model = model
        self.data_preprocessor = data_preprocessor

    def train(self, raw_data, labels):
        pass
        # x = df.drop('delayed', axis=1)
        # y = df['delayed']

        # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # model = LogisticRegression(max_iter=1000)
        # model.fit(X_train, y_train)

        # preds = model.predict_proba(X_test)[:, 1]


    def predict(self, raw_data):
        processed_data = self.data_preprocessor.preprocess(raw_data)
        return self.model.predict(processed_data)
    