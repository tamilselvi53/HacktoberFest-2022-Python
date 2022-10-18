import numpy as np

class LinearRegression():
    
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, X, y, lr=0.01, epochs=100):
        self.w = np.zeros(X.shape[1])
        self.b = 0
        for _ in range(epochs):
            y_pred = self.predict(X)
            dw = np.mean((y_pred - y) * X, axis=0)
            db = np.mean(y_pred - y)
            self.w -= lr * dw
            self.b -= lr * db

    def predict(self, X):
        return X @ self.w + self.b

    def score(self, X, y):
        y_pred = self.predict(X)
        return 1 - np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2)

def main():
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m, c = 2, 3
    y = m * X[:, 0] + c
    model = LinearRegression()
    model.fit(X, y)
    print(f"Accuracy: {model.score(X, y)}")

if __name__ == '__main__':
    main()