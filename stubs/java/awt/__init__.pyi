from java.lang import Object

class Color(Object):
    def __init__(self, *args) -> None: ...

class Component(Object): ...

class Container(Component):
    def add(self, *args) -> None: ...

class Image(Object): ...

class Toolkit(Object):
    def beep(self) -> None: ...
    @staticmethod
    def getDefaultToolkit(): ...

class Window(Container): ...
class Frame(Window): ...
