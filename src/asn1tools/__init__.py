"""Alias of the asn1tools_ext package, to keep existing code that
imports asn1tools working.

"""

import importlib
import pkgutil
import sys

import asn1tools_ext
from asn1tools_ext import *  # noqa: F401,F403

# Make asn1tools and all its submodules the very same module objects
# as in asn1tools_ext, so that classes and exceptions are identical
# regardless of which name they were imported by.
for _module_info in pkgutil.walk_packages(asn1tools_ext.__path__, "asn1tools_ext."):
    sys.modules[__name__ + _module_info.name[len("asn1tools_ext") :]] = (
        importlib.import_module(_module_info.name)
    )

sys.modules[__name__] = asn1tools_ext
