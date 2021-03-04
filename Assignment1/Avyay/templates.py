"""
Module to create template classes for Autodifferentiable losses/activations/layers
"""


class AutoDiffFunction():
    """Format for any function in general which has to be auto-differentiable
    """

    def __init__(self, *args, **kwds) -> None:
        self.saved_for_backward = {}
        self.grad = {}

    def __call__(self, *args, **kwds):

        output = self.forward(*args, **kwds)
        self.grad = self.compute_grad(*args, **kwds)
        return output

    def forward(self, *args, **kwds):
        pass

    def compute_grad(self, *args, **kwds):
        pass

    def backward(self, *args, **kwds):
        pass


class Layer(AutoDiffFunction):
    """Format to create your own custom layer for the model
    """
    def __init__(self, *args, **kwds) -> None:
        super().__init__(*args, **kwds)

        self.weights = {}
        self.optimizer = None

    def initialize_weights(self, *args, **kwds):
        pass

    def update_weights(self):

        self.optimizer.step(self)


class Loss(AutoDiffFunction):
    """Format to create a custom loss function
    """
    def __init__(self, num_classes):
        self.num_classes = num_classes
    
    def forward(self, y_true, y_pred):
        pass 

    def backward(self):
        return self.grad["x"]

    def compute_grad(self, y_true, y_pred):
        pass


class Optimizer():
    """Format to create a custom optimizer
    """
    def __init__(self, *args, **kwds):
        self.remember = {}
        pass

    def add_params(self, *args, **kwds):
        pass

    def step(self, layer):
        pass    