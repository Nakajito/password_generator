"""Utility functions for the password generator app.

This module contains the reusable password generation logic extracted from
the component state so it can be tested independently.
"""

from __future__ import annotations

import secrets
import string
from typing import Optional


def generate_password(length: int, charset: Optional[str] = None) -> str:
    """Generate a secure random password.

    Args:
        length: The length of the password to generate. Must be >= 0.
        charset: Optional custom set of characters to use. If None, a default
            set is used (letters + digits + common punctuation).

    Returns:
        A randomly generated password string of the requested length.

    Raises:
        ValueError: If length is negative.
    """
    if length < 0:
        raise ValueError("length must be non-negative")

    if charset is None:
        charset = string.ascii_letters + string.digits + "!@#$%&*"

    # Use secrets.choice for cryptographically secure random generation.
    return "".join(secrets.choice(charset) for _ in range(length))
