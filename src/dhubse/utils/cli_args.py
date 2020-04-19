import argparse
from .meta_v import VERSION, ERROR_MSG, DEFAULT_ARG


def set_args():
    parser = argparse.ArgumentParser(
        prog='dhubse',
        description='Docker image search tool.',
        epilog='https://github.com/unihon/dhubse'
    )
    parser.add_argument(
        'image',
        help='image'
    )
    parser.add_argument(
        '-m',
        '--mode',
        choices=['search', 'tag'],
        default=DEFAULT_ARG['mode']
    )
    parser.add_argument(
        '-s',
        '--page_size',
        help='page size, default 20',
        default=DEFAULT_ARG['page_size'],
        type=int
    )
    parser.add_argument(
        '-p',
        '--page',
        help='page number, default 1',
        default=DEFAULT_ARG['page'],
        type=int
    )
    parser.add_argument(
        '--timeout',
        help='request timeout, default 30',
        default=DEFAULT_ARG['timeout'],
        type=int
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s ' + VERSION,
    )

    args_obj = parser.parse_args()

    try:
        assert args_obj.page_size > 0 and args_obj.page_size < 100, ERROR_MSG['page_size_error']
        assert args_obj.page > 0, ERROR_MSG['page_error']
    except AssertionError as e:
        print(str(e))
        sys.exit()

    return dict(args_obj._get_kwargs()), args_obj
