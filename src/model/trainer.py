from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


class Trainer:
    def __init__(self, model="full") -> None:
        self.model = model
        self.test_size = 0.3

    def split_data(self, data):
        X,y = data.drop(["t_win"], axis=1), data["t_win"]

        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=self.test_size)

        return X_train, X_test, y_train, y_test
    
    def save_model(self, model_dir, model_name):
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, model_name)
        joblib.dump(self.model, model_path)
        print(f"Modelo salvo em {model_path}")
    
    def train(self, data):
        X_train, X_test, y_train, y_test = self.split_data(data)

        scaler = StandardScaler()


        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        self.model = RandomForestClassifier(n_jobs=4)

        self.model.fit(X_train_scaled, y_train)

        self.save_model('models/', 'rf.joblib')
        print(self.model.score(X_test_scaled, y_test))


