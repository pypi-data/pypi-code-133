# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _analyservariable
else:
    import _analyservariable

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


SHARED_PTR_DISOWN = _analyservariable.SHARED_PTR_DISOWN
import libcellml.types

# libCellML generated wrapper code starts here.

class AnalyserVariable(object):
    r"""Creates an :class:`AnalyserVariable` object."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Type_VARIABLE_OF_INTEGRATION = _analyservariable.AnalyserVariable_Type_VARIABLE_OF_INTEGRATION
    Type_STATE = _analyservariable.AnalyserVariable_Type_STATE
    Type_CONSTANT = _analyservariable.AnalyserVariable_Type_CONSTANT
    Type_COMPUTED_CONSTANT = _analyservariable.AnalyserVariable_Type_COMPUTED_CONSTANT
    Type_ALGEBRAIC = _analyservariable.AnalyserVariable_Type_ALGEBRAIC
    Type_EXTERNAL = _analyservariable.AnalyserVariable_Type_EXTERNAL
    __swig_destroy__ = _analyservariable.delete_AnalyserVariable

    def type(self):
        r"""Returns the :enum:`AnalyserVariable::Type`."""
        return _analyservariable.AnalyserVariable_type(self)

    def index(self):
        r"""Returns the index."""
        return _analyservariable.AnalyserVariable_index(self)

    def initialisingVariable(self):
        r"""Returns the initialising :class:`Variable`."""
        return _analyservariable.AnalyserVariable_initialisingVariable(self)

    def variable(self):
        r"""Returns the :class:`Variable`."""
        return _analyservariable.AnalyserVariable_variable(self)

    def equation(self):
        r"""Returns the :class:`AnalyserEquation`."""
        return _analyservariable.AnalyserVariable_equation(self)

# Register AnalyserVariable in _analyservariable:
_analyservariable.AnalyserVariable_swigregister(AnalyserVariable)



