import asyncore
import logging
import os
import sys

sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from mopidy import config, ConfigError
from mopidy.server import MpdServer
from mopidy.backends.despotify import DespotifyBackend

def main():
    _setup_logging(2)
    backend = DespotifyBackend()
    MpdServer(backend=backend)
    asyncore.loop()

def _setup_logging(verbosity_level):
    if verbosity_level == 0:
        level = logging.WARNING
    elif verbosity_level == 2:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(
        format=config.CONSOLE_LOG_FORMAT,
        level=level,
    )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
    except ConfigError, e:
        sys.exit('%s' % e)
