from .base import TransformationStrategy
import numpy as np

class InverseTransformation(TransformationStrategy):
    def apply(self, data):
        return 1.0 / (data + 1)  # Adding 1 to avoid division by zero

    def name(self):
        return "Inverse"
