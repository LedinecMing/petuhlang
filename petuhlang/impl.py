# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2021 DenyS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Classes implementation in petuhlang."""

from __future__ import annotations

import sys
import typing

from petuhlang import PetuhObject, errors

if typing.TYPE_CHECKING:
    from petuhlang.types import ArgsType, KwargsType

    ClsParents = typing.Sequence[type, ...] | type
__all__: tuple[str, ...] = ("PetuhClass",)

global_ = sys.modules["builtins"].__dict__


def _check_class_type(cls: typing.ClassVar, classes: ClsParents, /) -> str | None:
    """Checking if the class or classes was passed."""
    if isinstance(classes, type) or all([isinstance(object, type) for object in classes ]):
        return None
    wrong_types = "".join([f"{object}({type(object)});" for object in classes if not isinstance(object, type)])
    raise errors.BadParentClassPassedError(f"Excepted classes for {cls.__cls_name__}, got {wrong_types}")


def _create_instance(cls, *args: ArgsType, bindTo: str, **kwargs: KwargsType):
    """Body for classmethod."""
    global_[bindTo] = (instance := cls(*args, **kwargs))
    return instance


def _make_class(cls: typing.ClassVar, bases: tuple[ClsParents], *args: ArgsType, **kwargs: KwargsType) -> type:
    return type(
        cls.__cls_name__,
        bases,
        {
            "createInstance": classmethod(_create_instance),
            "__init__": lambda self_, *args, **kwargs: None,
        },
    )


class PetuhClass(PetuhObject):
    def __init__(self, cls_name: str, /) -> None:
        self.__cls_name__ = cls_name

    def __call__(self, *, extends: tuple[ClsParents] | None = None) -> type:
        bases = (PetuhObject,)
        if extends is not None:
            _check_class_type(self, extends)
            bases += extends
        cls = _make_class(self, bases)
        global_[self.__cls_name__] = cls

        return cls