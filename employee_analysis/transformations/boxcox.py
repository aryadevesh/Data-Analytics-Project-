from .base import TransformationStrategy
import numpy as np
from scipy.stats import boxcox

class BoxCoxTransformation(TransformationStrategy):
    def apply(self, data):
        return boxcox(data + 1)[0]  # Adding 1 to avoid issues with zero values

    def name(self):
        return "Box-Cox"
