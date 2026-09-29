# models/__init__.py
from .base import BaseModel

# import the modules (not the classes) so every model registers with Base
from . import user
from . import game
from . import review
# add future models here as needed

__all__ = ["BaseModel"]