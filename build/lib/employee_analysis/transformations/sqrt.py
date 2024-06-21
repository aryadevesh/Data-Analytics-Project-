from .base import TransformationStrategy
import numpy as np

class SqrtTransformation(TransformationStrategy):
    def apply(self, data):
        return np.sqrt(data)

    def name(self):
        return "Square Root"
