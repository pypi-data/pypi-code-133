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
    from . import _component
else:
    import _component

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


SHARED_PTR_DISOWN = _component.SHARED_PTR_DISOWN
import libcellml.componententity
import libcellml.importedentity
import libcellml.namedentity
import libcellml.parentedentity
import libcellml.entity
import libcellml.types

# libCellML generated wrapper code starts here.

class Component(libcellml.componententity.ComponentEntity, libcellml.importedentity.ImportedEntity):
    r"""Represents a CellML component."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _component.delete_Component

    def setSourceComponent(self, importSource, name):
        r"""
        Marks this component as an imported component by defining an
        `importSource` specifying the source of the import and the `name` of the
        component in the `importSource`.
        """
        return _component.Component_setSourceComponent(self, importSource, name)

    def appendMath(self, math):
        r"""Appends `math` to the existing math string for this component."""
        return _component.Component_appendMath(self, math)

    def math(self):
        r"""
        Returns a math string if one has been created for this component (empty string
        if not).
        """
        return _component.Component_math(self)

    def setMath(self, math):
        r"""
        Sets the math string for this component.
        If `math` is an empty string, math will be removed from the component.
        """
        return _component.Component_setMath(self, math)

    def removeMath(self):
        r"""Clears the math from this component."""
        return _component.Component_removeMath(self)

    def addVariable(self, variable):
        r"""Adds variable `variable` to this component."""
        return _component.Component_addVariable(self, variable)

    def removeAllVariables(self):
        r"""
        Clears all variables that have been added to this component.

        If any of the variables to be removed are in connections (are equivalent to
        other variables), this component will not be serialised in the connection.
        """
        return _component.Component_removeAllVariables(self)

    def takeVariable(self, *args):
        r"""
        Removes a variable and returns it from this component, specified by name, or
        index.

        Returns the `Variable` on success.
        """
        return _component.Component_takeVariable(self, *args)

    def variableCount(self):
        r"""Returns the number of variables the component directly contains."""
        return _component.Component_variableCount(self)

    def hasVariable(self, *args):
        r"""
        Tests if this component contains a given variable, specified by name or as
        `Variable` object.
        """
        return _component.Component_hasVariable(self, *args)

    def addReset(self, reset):
        r"""Add a reset `reset` to this component."""
        return _component.Component_addReset(self, reset)

    def takeReset(self, index):
        r"""
        Removes a reset and returns it from this component, specified by index.

        Returns the `Reset` on success.
        """
        return _component.Component_takeReset(self, index)

    def removeReset(self, *args):
        r"""
        Remove the reset at the given index from this component.
        If the index is not valid @c false is returned, the valid
        range for the index is [0, #resets).
        """
        return _component.Component_removeReset(self, *args)

    def removeAllResets(self):
        r"""Clears all resets that have been added to this component."""
        return _component.Component_removeAllResets(self)

    def reset(self, index):
        r"""
        Returns a reference to a reset at the index @p index for this
        component. If the index is not valid a @c nullptr is returned, the valid
        range for the index is [0, #resets).
        """
        return _component.Component_reset(self, index)

    def resetCount(self):
        r"""Returns the number of resets the component contains."""
        return _component.Component_resetCount(self)

    def hasReset(self, reset):
        r"""
        Tests whether the argument :param: reset exists in the set of this component's
        resets. Returns True if the :param: reset is in this component's
        resets and False otherwise.
        """
        return _component.Component_hasReset(self, reset)

    def clone(self):
        r"""Create a copy of this component."""
        return _component.Component_clone(self)

    def requiresImports(self):
        r"""
        Determines whether this component relies on any imports.  If this component
        or any of its encapsulated components are imported, returns @c true,
        otherwise @c false.
        """
        return _component.Component_requiresImports(self)

    def variable(self, *args):
        r"""
        Returns a Variable from this component, specified by name or index.

        Only the first matching variable is returned.
        """
        return _component.Component_variable(self, *args)

    def removeVariable(self, *args):
        r"""
        Removes a variable from this component, specified by name, index, or
        `Variable` object.

        Only the first matching variable is removed.

        If the variable to be removed is in a connection (is equivalent to another
        variable), this component will not be serialised in the connection.

        Returns `True` on success.
        """
        return _component.Component_removeVariable(self, *args)

    def __init__(self, *args):
        _component.Component_swiginit(self, _component.new_Component(*args))

# Register Component in _component:
_component.Component_swigregister(Component)



