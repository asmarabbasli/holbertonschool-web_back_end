#!/usr/bin/env python3
"""
Module for filtering sensitive data from log messages.
"""

import re
import logging
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


class RedactingFormatter(logging.Formatter):
    """
    Formatter that redacts sensitive fields from log messages.
    """

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Initialize the formatter with fields to redact.

        Args:
            fields (List[str]): List of field names to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: Formatted and redacted log message.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)
#!/usr/bin/env python3
"""
Main file
"""

import logging

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=["email", "ssn", "password"])
print(formatter.format(log_record))
