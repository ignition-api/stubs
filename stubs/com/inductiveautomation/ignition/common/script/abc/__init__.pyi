class JythonMap:
    def __contains__(self, item) -> None: ...
    def __finditem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def get(self, *args) -> None: ...
    def has_key(self, pyKey) -> None: ...
    def items(self) -> None: ...
    def iteritems(self) -> None: ...
    def iterkeys(self) -> None: ...
    def itervalues(self) -> None: ...
    def keys(self) -> None: ...
    def values(self) -> None: ...

class JythonSequence:
    def __contains__(self, item) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def __mul__(self, other) -> None: ...
    def __rmul__(self, other) -> None: ...
    def count(self, element) -> None: ...
    def index(self, element) -> None: ...

class MutableJythonMap:
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def clear(self) -> None: ...
    def pop(self, *args) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, *args) -> None: ...
    def update(self, *args, **kwargs) -> None: ...

class MutableJythonSequence:
    def __add__(self, other) -> None: ...
    def __imul__(self, other) -> None: ...
    def append(self, element) -> None: ...
    def extend(self, sequence) -> None: ...
    def insert(self, index, element) -> None: ...
    def pop(self, *args) -> None: ...
    def remove(self, element) -> None: ...
    def sort(self, *args, **kwargs) -> None: ...

class AbstractJythonMap(JythonMap):
    def __contains__(self, item) -> None: ...
    def __finditem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def get(self, *args) -> None: ...
    def has_key(self, pyKey) -> None: ...
    def items(self) -> None: ...
    def iteritems(self) -> None: ...
    def iterkeys(self) -> None: ...
    def itervalues(self) -> None: ...
    def keys(self) -> None: ...
    def values(self) -> None: ...

class AbstractJythonSequence(JythonSequence):
    def __contains__(self, item) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> None: ...
    def __mul__(self, other) -> None: ...
    def __rmul__(self, other) -> None: ...
    def count(self, element) -> None: ...
    def index(self, element) -> None: ...

class AbstractMutableJythonMap(MutableJythonMap):
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def clear(self) -> None: ...
    def pop(self, *args) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, *args) -> None: ...
    def update(self, *args, **kwargs) -> None: ...

class AbstractMutableJythonSequence(MutableJythonSequence):
    def __add__(self, other) -> None: ...
    def __imul__(self, other) -> None: ...
    def append(self, element) -> None: ...
    def extend(self, sequence) -> None: ...
    def insert(self, index, element) -> None: ...
    def pop(self, *args) -> None: ...
    def remove(self, element) -> None: ...
    def sort(self, *args, **kwargs) -> None: ...
