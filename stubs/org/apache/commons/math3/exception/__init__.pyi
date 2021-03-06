from java.lang import IllegalArgumentException

class MathIllegalArgumentException(IllegalArgumentException):
    def __init__(self, pattern, *args) -> None: ...
    def getContext(self) -> None: ...

class MathIllegalNumberException(MathIllegalArgumentException):
    INTEGER_ZERO: int
    def getArgument(self) -> None: ...

class DimensionMismatchException(MathIllegalNumberException):
    def __init__(self, *args) -> None: ...
    def getDimension(self) -> None: ...
