from abc import ABC, abstractmethod
import numpy as np
from scipy.stats import shapiro

class TransformationStrategy(ABC):
    @abstractmethod
    def apply(self, data):
        pass

    @abstractmethod
    def name(self):
        pass

    def test_normality(self, data):
        data = data[~np.isnan(data) & ~np.isinf(data)]  # Remove NaN and Inf
        stat, p_value = shapiro(data)
        return stat, p_value
