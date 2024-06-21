from .base import TransformationStrategy
import numpy as np

class OriginalTransformation(TransformationStrategy):
    def apply(self, data):
        return data

    def name(self):
        return "Original"
