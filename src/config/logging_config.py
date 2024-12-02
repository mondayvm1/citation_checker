from logging.config import dictConfig

def setup_logging():
    logging_config = dict(
        version=1,
        formatters={
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        handlers={
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'app.log',
                'level': 'INFO',  # Only log errors to the file
            },
            'null': {
                'class': 'logging.NullHandler',  # This handler discards all log messages
            },
        },
        root={
            'handlers': ['file', 'null'],  # Use file handler and discard other handlers
            'level': 'INFO',  # Set root logger to handle only errors
        },
    )
    dictConfig(logging_config)

