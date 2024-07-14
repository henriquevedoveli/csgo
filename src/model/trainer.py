from sklearn.model_selection import train_test_split


class Trainer:
    def __init__(self, model) -> None:
        self.model = model
        self.test_size = 0.2

    def split_data(self, data):
        X,y = data.drop(["t_win"], axis=1), data["t_win"]

        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=self.test_size)

        return X_train, X_test, y_train, y_test
