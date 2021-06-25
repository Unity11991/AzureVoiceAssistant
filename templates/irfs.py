class LinearRegression:
    def __init__(self):
        pass

    def fit(self, x,y):
        n = x.count()
        x_mean = x.mean()
        y_mean = y.mean()
        self.slope = ((n*x_mean*y_mean)-(x*y).sum())/(n*(x_mean**2) - (x**2).sum())
        self.bias = (((x*y).sum()) - (self.slope * ((x**2).sum())))/ (n*x_mean)
        return None

    def predict(self, x):
            return self.slope*x + self.bias