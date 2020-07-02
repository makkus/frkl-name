# -*- coding: utf-8 -*-
import os
import sys

from appdirs import AppDirs


frkl_name_app_dirs = AppDirs("frkl_name", "frkl")

if not hasattr(sys, "frozen"):
    FRKL_NAME_MODULE_BASE_FOLDER = os.path.dirname(__file__)
    """Marker to indicate the base folder for the `frkl_name` module."""
else:
    FRKL_NAME_MODULE_BASE_FOLDER = os.path.join(
        sys._MEIPASS, "frkl_name"  # type: ignore
    )
    """Marker to indicate the base folder for the `frkl_name` module."""

FRKL_NAME_RESOURCES_FOLDER = os.path.join(FRKL_NAME_MODULE_BASE_FOLDER, "resources")
