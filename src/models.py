class Model:
    def __init__(self):
        pass

    def setup(self):
        pass

    def learn(self):
        pass

    def predict(self):
        pass

    def evaluate(self, d_train, d_valid):
        # Zero-initialize all the variables (sX/vX/mX).

        # Execute setup instructions.
        self.setup()

        # Train
        for (x, y) in d_train:
            self.v0 = x  # x will now be accessible to Predict.
            self.predict()

            # s1 = Normalize(s1)  # Normalize the prediction.
            self.s0 = y  # y will now be accessible to Learn.
            self.learn()  # Execute learning instructions.

        # Validate
        sum_loss = 0.0
        for (x, y) in d_valid:
            self.v0 = x
            self.predict()  # Only execute Predict(), not Learn().
            # s1 = Normalize(s1)
            # sum_loss += Loss(y, s1)

        mean_loss = sum_loss / len(d_valid)

        # Use validation loss to evaluate the algorithm.
        return mean_loss


def evaluate(model, d_train, d_valid):
    # Zero-initialize all the variables (sX/vX/mX).

    # Execute setup instructions.
    model.setup()

    for (x, y) in d_train:
        v0 = x  # x will now be accessible to Predict.
        model.predict()

        # s1 = Normalize(s1)  # Normalize the prediction.
        s0 = y  # y will now be accessible to Learn.
        model.learn()  # Execute learning instructions.

    sum_loss = 0.0

    for (x, y) in d_valid:
        v0 = x
        model.predict()  # Only execute Predict(), not Learn().
        # s1 = Normalize(s1)
        # sum_loss += Loss(y, s1)

    mean_loss = sum_loss / len(d_valid)

    # Use validation loss to evaluate the algorithm.
    return mean_loss


