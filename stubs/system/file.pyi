from java.lang import String
from typing import Any, List, Optional

def fileExists(filepath: String) -> bool: ...
def getTempFile(extension: String) -> String: ...
def openFile(
    extension: Optional[String] = ..., defaultLocation: Optional[String] = ...
) -> Optional[String]: ...
def openFiles(
    extension: Optional[String] = ..., defaultLocation: Optional[String] = ...
) -> Optional[List[String]]: ...
def readFileAsBytes(filepath: String) -> Any: ...
def readFileAsString(filepath: String, encoding: Optional[String] = ...) -> String: ...
def saveFile(
    filename: String,
    extension: Optional[String] = ...,
    typeDesc: Optional[String] = ...,
) -> Optional[String]: ...
def writeFile(
    filepath: String, data: Any, append: bool = ..., encoding: String = ...
) -> None: ...
