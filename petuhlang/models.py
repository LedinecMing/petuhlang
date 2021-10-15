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
"""Models for isinstance() checks in petuhlang."""

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from petuhlang.__future__converters.abstract import ConverterABC


__all__: tuple[str, ...] = ("Convertable",)


@typing.runtime_checkable
class Convertable(typing.Protocol):
    """``runtime_checkable``

    Checks if a class supports converters.

    Example:
    --------

    ```py
    if isinstance(obj, Convertable):
        ...
    ```

    !!! note:
        This is a Future object that will be relevant in
        future versions of petuhlang. There is no point
        in using it right now.
    """

    def add_converter(self, converter: ConverterABC) -> None:
        raise NotImplementedError
