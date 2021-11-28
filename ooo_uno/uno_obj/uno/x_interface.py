# coding: utf-8
from abc import ABC, abstractmethod


class XInterface(ABC):
    """
    base interface of all UNO interfaces

    It provides lifetime control by reference counting and the possibility of querying for other
    interfaces of the same logical object.

    "Logical Object" in this case means that the interfaces actually can be supported by internal
    (e.g. aggregated) physical objects.

    Deriving from this interface is mandatory for all UNO interfaces.

    Each language binding (Java, C++, StarBasic, Python, ... ) may provide a different mapping
    of this interface, please look into the language dependent documentation.

    The UNO object does not export the state of the reference count (acquire() and release()
    do not have return values). In general, also the UNO object itself should not make any assumption
    on the concrete value of the reference count (except on the transition from one to zero ).

    See Also:
        `API XInterface <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XInterface.html>`_
    """
    @abstractmethod
    def release(self):
        """
        decreases the reference counter by one.

        When the reference counter reaches 0, the object gets deleted.

        Calling release() on the object is often called releasing or clearing the reference to an object.
        """

    @abstractmethod
    def acquire(self):
        """
        increases the reference counter by one.

        When you have called acquire() on the UNO object, it is often said, that you have a
        reference or a hard reference to the object.

        It is only allowed to invoke a method on a UNO object, when you keep a hard reference to it.

        Every call to acquire must be followed by a corresponding call to release some time later,
        which may eventually lead to the destruction of the object.
        """

    @abstractmethod
    def queryInterface(self, aType: object) -> object:
        """
        queries for a new interface to an existing UNO object.

        The queryInterface() method is the entry point to obtain other interfaces which
        are exported by the object. The caller asks the implementation of the object,
        if it supports the interface specified by the type argument.
        The call may either return with an interface reference of the requested type or with a void any.

        There are certain specifications, a queryInterface() implementation must not violate.

        1.
            If queryInterface on a specific object has once returned a valid interface reference for a given type,
            it must return a valid reference for any successive queryInterface calls on this object for the same type.
        2.
            If queryInterface on a specific object has once returned a null reference for a given type,
            it must always return a null reference for the same type.
        3.
            If queryInterface on a reference A returns reference B, queryInterface on B for Type A must return
            interface reference A or calls made on the returned reference must be equivalent to calls made
            on reference A.
        4.
            If queryInterface on a reference A returns reference B, queryInterface on A and B for
            XInterface must return the same interface reference (object identity).

        The reason for the strong specification is, that a Uno Runtime Environment (URE) may choose to cache
        queryInterface() calls.

        As mentioned above, certain language bindings may map this function
        differently also with different specifications, please visit the language dependent specification for it.
        The current C++ binding sticks to the specification state

        The rules mentioned above are basically identical to the rules of QueryInterface in MS COM.

        Args:
            aType (object): a UNO interface type, for which an object reference shall be obtained.

        Return:
            an interface reference in case the requested interface is supported by the object, a void any otherwise.
        """
