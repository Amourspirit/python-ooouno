===========
Const Class
===========

Const classes represent a const

Static
======

Const classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are static classes.

Example static:
    .. code-block:: python

        from ooo.lo.awt.device_capability import DeviceCapability
        assert DeviceCapability.RASTEROPERATIONS == 1
        assert DeviceCapability.GETBITS == 2

Const classes in ``ooo.lo`` and ``ooo.csslo`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.lo.awt.device_capability import DeviceCapability as LoDeviceCapability
        from ooo.csslo.awt import DeviceCapability as CssDeviceCapability
        from ooo.dyn.awt.device_capability import DeviceCapability as DynDeviceCapability
        same = LoDeviceCapability is CssDeviceCapability
        assert same == True
        same = CssDeviceCapability is DynDeviceCapability
        assert same == False

Dynamic
=======

Const classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are dynamic classes
and are changed during runtime.

Each const class in the ``ooo.dyn`` and ``ooo.cssdyn`` namespaces have a corrsponding enum class as well.
The enum class is always the name of the UNO class with ``Enum`` appended.

For instance:
    Class ``ooo.cssdyn.DeviceCapability`` will have corresponding ``ooo.cssdyn.DeviceCapabilityEnum`` class
    containing same values. This is for convenience.

Example dynamic:
    .. code-block:: python

        from ooo.dyn.awt.device_capability import DeviceCapability, DeviceCapabilityEnum
        assert DeviceCapability.GETBITS == DeviceCapabilityEnum.GETBITS
        assert DeviceCapability.RASTEROPERATIONS == DeviceCapabilityEnum.RASTEROPERATIONS
        assert DeviceCapability.GETBITS == DeviceCapabilityEnum.GETBITS.value
        assert DeviceCapability.RASTEROPERATIONS == DeviceCapabilityEnum.RASTEROPERATIONS.value
        assert DeviceCapability.__module__ == 'uno'


Const classes in ``ooo.dyn`` and ``ooo.cssdyn`` namespaces are the same classes.

Example:
    .. code-block:: python

        from ooo.dyn.awt.device_capability import DeviceCapability as DynDeviceCapability
        from ooo.cssdyn.awt import DeviceCapability as CssDeviceCapability
        from ooo.lo.awt.device_capability import DeviceCapability as LoDeviceCapability
        same = DynDeviceCapability is CssDeviceCapability
        assert same == True
        same = DynDeviceCapability is LoDeviceCapability
        assert same == False

.. note::
    This library is for Libre Office |lo_version|; However is somewhat backwards compatable.

    For instance ``ooo.cssdyn.style.NumberingType`` had the attributes
    **ARABIC_ZERO3**, **ARABIC_ZERO4**, **ARABIC_ZERO5**, **SZEKELY_ROVAS** added in LO 7.x.
    When dynamic  ``NumberingType`` or ``NumberingTypeEnum`` is generated in pre
    LO 7 environment these attributes will be missing.

    See: `API NumberingType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style_1_1NumberingType.html>`_
