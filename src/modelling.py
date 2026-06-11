from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_models(X_train, y_train):

    models = {

        "Logistic Regression":
        LogisticRegression(max_iter=500),

        "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    }

    for model in models.values():
        model.fit(X_train, y_train)

    return models