from .original import OriginalTransformation
from .log import LogTransformation
from .sqrt import SqrtTransformation
from .boxcox import BoxCoxTransformation
from .inverse import InverseTransformation

class TransformationFactory:
    @staticmethod
    def get_transformations():
        return [
            OriginalTransformation(),
            LogTransformation(),
            SqrtTransformation(),
            BoxCoxTransformation(),
            InverseTransformation()
        ]
