from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

api.add_listener(ON_CONNECT, CheckiOReferee(TESTS).on_ready)
api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover_codes.unwrap_args,  # or None
            'python-3': cover_codes.unwrap_args
        },).on_ready)
