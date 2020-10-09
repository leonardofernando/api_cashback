"""Logger."""
import datetime
import json
import logging
import os
import sys


class Logger:  # pragma: no cover
    """Logger class."""

    __monostate = None

    def __init__(self, name="api-cashback"):
        """Class constructor."""
        log_format = (
            '{ "log_level": %(levelno)s, ' '"project_name": "' + name + '", ' '"message": %(message)s }'
        )

        if Logger.__monostate:
            self.__dict__ = self.__monostate

        if not Logger.__monostate:
            Logger.__monostate = self.__dict__
            self.logger = logging.getLogger(name)
            hdlr = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(log_format)
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)
            self.logger.setLevel(int(os.environ.get("LOG_LEVEL", 40)))

    @staticmethod
    def format_date(item):
        """Change format date to ISO."""
        if isinstance(item, (datetime.date, datetime.datetime)):
            return item.isoformat()
        return item

    def info(self, message, **kwargs):
        """Log info."""
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=Logger.format_date)
        self.logger.info(message_json, **kwargs)

    def success(self, message, **kwargs):
        """Log success."""
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=Logger.format_date)
        self.logger.info(message_json, **kwargs)

    def error(self, message, **kwargs):
        """Log error."""
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=Logger.format_date)
        self.logger.error(message_json, **kwargs)

    def critical(self, message, **kwargs):
        """Log critical."""
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=Logger.format_date)
        self.logger.critical(message_json, **kwargs)

    def debug(self, message, **kwargs):
        """Log critical."""
        message_json = json.dumps(message, ensure_ascii=False, sort_keys=True, default=Logger.format_date)
        self.logger.debug(message_json, **kwargs)
