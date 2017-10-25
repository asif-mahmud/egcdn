"""Configurator implementation."""
import argparse
import logging
import sys

from . import __version__


class Configurator(object):

    def __init__(self):
        self._config = None
        self._config_parser = argparse.ArgumentParser(
            prog='egcdn',
            description='A Glue Application between web applications and CDN servers.',
            epilog='This software is distributed under GPLv2',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        self._prepare()

    def _prepare(self):
        self._config_parser.add_argument(
            '-T', '--protocol', type=str, default='amqp', help='Message Queue server\s protocol.'
        )
        self._config_parser.add_argument(
            '-H', '--host', type=str, default='localhost', help='Host of Message Queue server.'
        )
        self._config_parser.add_argument(
            '-P', '--port', type=int, default=5672, help='Message Queue server\s port.'
        )
        self._config_parser.add_argument(
            '-W', '--workers', type=int, default=2, help='Number of worker processes to spawn.'
        )
        self._config_parser.add_argument(
            '-V', '--verbosity', type=int, default=0, choices=[0, 1, 2, 3], help='Log level. The larger the value, the more log messages will be printed out.'
        )
        self._config_parser.add_argument(
            '-v', '--version', action='version', version='{} {}'.format(
                self._config_parser.prog, __version__
            )
        )

    def parse(self):
        """Parse command line arguments and set logger."""
        self._config = self._config_parser.parse_args()
        self._set_logger()

    def _set_logger(self):
        """Set logger settings."""
        log_level = logging.ERROR
        if self._config.verbosity == 1:
            log_level = logging.WARN
        elif self._config.verbosity == 2:
            log_level = logging.INFO
        elif self._config.verbosity == 3:
            log_level = logging.DEBUG
        logging.basicConfig(
            level=log_level,
            stream=sys.stderr,
            format='[%(asctime)s] [%(levelname)-8s] [egcdn:%(threadName)s:%(name)s] %(message)s'
        )

    @property
    def config(self):
        """Get the `config` instance."""
        return self._config
