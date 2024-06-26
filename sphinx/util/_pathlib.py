"""What follows is awful and will be gone in Sphinx 8"""

from __future__ import annotations

import sys
import warnings
from pathlib import Path, PosixPath, PurePath, WindowsPath
from typing import Any

from sphinx.deprecation import RemovedInSphinx80Warning

_STR_METHODS = frozenset(str.__dict__)
_PATH_NAME = Path().__class__.__name__

_MSG = (
    'Sphinx 8 will drop support for representing paths as strings. '
    'Use "pathlib.Path" or "os.fspath" instead.'
)

# https://docs.python.org/3/library/stdtypes.html#typesseq-common
# https://docs.python.org/3/library/stdtypes.html#string-methods

if sys.platform == 'win32':
    class _StrPath(WindowsPath):
        def replace(  # type: ignore[override]
            self, old: str, new: str, count: int = -1, /,
        ) -> str:
            # replace exists in both Path and str;
            # in Path it makes filesystem changes, so we use the safer str version
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__().replace(old, new, count)  # NoQA:  PLC2801

        def __getattr__(self, item: str) -> Any:
            if item in _STR_METHODS:
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return getattr(self.__str__(), item)
            msg = f'{_PATH_NAME!r} has no attribute {item!r}'
            raise AttributeError(msg)

        def __add__(self, other: str) -> str:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__() + other

        def __bool__(self) -> bool:
            if not self.__str__():
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return False
            return True

        def __contains__(self, item: str) -> bool:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return item in self.__str__()

        def __eq__(self, other: object) -> bool:
            if isinstance(other, PurePath):
                return super().__eq__(other)
            if isinstance(other, str):
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return self.__str__() == other
            return NotImplemented

        def __hash__(self) -> int:
            return super().__hash__()

        def __getitem__(self, item: int | slice) -> str:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__()[item]

        def __len__(self) -> int:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return len(self.__str__())
else:
    class _StrPath(PosixPath):
        def replace(  # type: ignore[override]
            self, old: str, new: str, count: int = -1, /,
        ) -> str:
            # replace exists in both Path and str;
            # in Path it makes filesystem changes, so we use the safer str version
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__().replace(old, new, count)  # NoQA:  PLC2801

        def __getattr__(self, item: str) -> Any:
            if item in _STR_METHODS:
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return getattr(self.__str__(), item)
            msg = f'{_PATH_NAME!r} has no attribute {item!r}'
            raise AttributeError(msg)

        def __add__(self, other: str) -> str:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__() + other

        def __bool__(self) -> bool:
            if not self.__str__():
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return False
            return True

        def __contains__(self, item: str) -> bool:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return item in self.__str__()

        def __eq__(self, other: object) -> bool:
            if isinstance(other, PurePath):
                return super().__eq__(other)
            if isinstance(other, str):
                warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
                return self.__str__() == other
            return NotImplemented

        def __hash__(self) -> int:
            return super().__hash__()

        def __getitem__(self, item: int | slice) -> str:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return self.__str__()[item]

        def __len__(self) -> int:
            warnings.warn(_MSG, RemovedInSphinx80Warning, stacklevel=2)
            return len(self.__str__())
