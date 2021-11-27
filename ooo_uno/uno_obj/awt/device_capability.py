# coding: utf-8
from ...base.const import ConstIntBase


class DeviceCapability(ConstIntBase):
    """
    defines which capabilities a device supports.

    See Also:
        `API DeviceCapability <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1DeviceCapability.html>`_
    """
    GETBITS = 2
    """
    supports the ``XDevice.createBitmap()``, the ``XDevice.createDevice()`` and the ``XGraphics.copy()`` methods.
    """
    RASTEROPERATIONS = 1
    """supports the device raster operations."""
