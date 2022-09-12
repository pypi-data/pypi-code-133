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
    from . import _model
else:
    import _model

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


SHARED_PTR_DISOWN = _model.SHARED_PTR_DISOWN
class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _model.delete_SwigPyIterator

    def value(self):
        return _model.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _model.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _model.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _model.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _model.SwigPyIterator_equal(self, x)

    def copy(self):
        return _model.SwigPyIterator_copy(self)

    def next(self):
        return _model.SwigPyIterator_next(self)

    def __next__(self):
        return _model.SwigPyIterator___next__(self)

    def previous(self):
        return _model.SwigPyIterator_previous(self)

    def advance(self, n):
        return _model.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _model.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _model.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _model.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _model.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _model.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _model.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _model:
_model.SwigPyIterator_swigregister(SwigPyIterator)

import libcellml.componententity
import libcellml.importedentity
import libcellml.namedentity
import libcellml.parentedentity
import libcellml.entity
import libcellml.types

# libCellML generated wrapper code starts here.

class Model(libcellml.componententity.ComponentEntity):
    r"""Represents a CellML model."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _model.delete_Model

    def addUnits(self, units):
        r"""Add a copy of the given Units to this model."""
        return _model.Model_addUnits(self, units)

    def removeAllUnits(self):
        r"""Removes all units stored in this model."""
        return _model.Model_removeAllUnits(self)

    def hasUnits(self, *args):
        r"""Tests to see if this model has the given units, specified by name."""
        return _model.Model_hasUnits(self, *args)

    def unitsCount(self):
        r"""Returns the number of units this model contains."""
        return _model.Model_unitsCount(self)

    def linkUnits(self):
        r"""Link units defined in the model to units used by variables."""
        return _model.Model_linkUnits(self)

    def hasUnlinkedUnits(self):
        r"""Determine if any units used by variables are not linked to model units."""
        return _model.Model_hasUnlinkedUnits(self)

    def hasImports(self):
        r"""Determine if any Component or Units is an import."""
        return _model.Model_hasImports(self)

    def hasUnresolvedImports(self):
        r"""Tests if this model has unresolved imports."""
        return _model.Model_hasUnresolvedImports(self)

    def clone(self):
        r"""Create a copy of this model."""
        return _model.Model_clone(self)

    def fixVariableInterfaces(self):
        r"""Fix variable interfaces throughout the model."""
        return _model.Model_fixVariableInterfaces(self)

    def clean(self):
        r"""Remove any empty units and any empty components from the model."""
        return _model.Model_clean(self)

    def importRequirements(self):
        r"""Return all URLs used by imports in the model."""
        return _model.Model_importRequirements(self)

    def removeUnits(self, *args):
        r"""
        Removes the Units specified by index, name or Units object.

        Only the first matching Units is removed.

        Returns `True` on success.
        """
        return _model.Model_removeUnits(self, *args)

    def units(self, *args):
        r"""
        Returns a Units object from this Model, specified by index or name.

        Only the first matching Units is returned.
        """
        return _model.Model_units(self, *args)

    def takeUnits(self, *args):
        r"""
        Removes and returns the Units specified by index or name.

        Only the first matching Units is removed and returned.
        """
        return _model.Model_takeUnits(self, *args)

    def replaceUnits(self, *args):
        r"""
        Replaces a Units object, specified by index, name or Units object, by another
        Units (second argument).

        Only the first matching Units is replaced.

        Returns `True` on success.
        """
        return _model.Model_replaceUnits(self, *args)

    def __init__(self, *args):
        _model.Model_swiginit(self, _model.new_Model(*args))

# Register Model in _model:
_model.Model_swigregister(Model)



