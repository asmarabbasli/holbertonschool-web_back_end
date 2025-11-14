#!/usr/bin/env python3
"""
Module for filtering sensitive data from log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of field names to redact.
        redaction (str): Replacement string for sensitive values.
        message (str): Log message string containing key-value pairs.
        separator (str): Character that separates fields in the message.

    Returns:
        str: Log message with sensitive fields redacted.
    """
    pattern = rf'({"|".join(fields)})=[^ {separator}]*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
