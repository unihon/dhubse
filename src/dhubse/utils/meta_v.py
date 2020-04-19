import os

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
version_path = os.path.join(base_path, 'VERSION')
with open(version_path, 'r') as fh:
    VERSION = fh.read()

ERROR_MSG = {
    'timeout': 'request timeout.',
    'connect_error': 'connect error.',
    'page_error': 'page error.',
    'page_size_error': 'page size error.',
    'status_code_not_200': 'status code error.',
    'status_code_404': 'not found.',
}

DEFAULT_ARG = {
    'mode': 'search',
    'page_size': 20,
    'page': 1,
    'timeout': 30,
}
