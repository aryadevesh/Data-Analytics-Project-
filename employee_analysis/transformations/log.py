from .base import TransformationStrategy
import numpy as np

class LogTransformation(TransformationStrategy):
    def apply(self, data):
        return np.log(data + 1)  # Adding 1 to avoid log(0)

    def name(self):
        return "Log"
