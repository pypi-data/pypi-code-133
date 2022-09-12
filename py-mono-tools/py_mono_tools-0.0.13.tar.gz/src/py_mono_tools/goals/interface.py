"""Contains the interfaces that goals will implement."""
import abc
import typing as t
from enum import Enum


class Language(Enum):
    """The languages that the linters can check."""

    TERRAFORM = "terraform"
    PYTHON = "python"


class Linter(abc.ABC):
    """The interface that all linters will implement."""

    name: str
    parallel_run: bool
    language: Language
    weight: int = 0

    def __init__(self, args: t.Optional[t.List[str]] = None):
        """Will initialize the linter.

        Args are passed through to the linter.
        """
        if args is None:
            args = []
        self._args = args

    @abc.abstractmethod
    def run(self):
        """Will run the linter.

        Depending on the linter this may have side effects
        """
        raise NotImplementedError

    @abc.abstractmethod
    def check(self):
        """Will run the linter in check mode.This should NEVER change any files."""
        raise NotImplementedError


class Tester(abc.ABC):
    """The interface that all Testers will implement."""

    name: str
    language: Language

    def __init__(self, args: t.Optional[t.List[str]] = None, test_dir=None):
        """Will initialize the Tester.

        Args are passed through to the Tester.
        """
        if args is None:
            args = []
        self._args = args
        self._test_dir = test_dir

    @abc.abstractmethod
    def run(self):
        """Will run the tester."""
        raise NotImplementedError
