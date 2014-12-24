from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS


def checker(result, test_data):
    return result['code_result']

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
        check_result=checker,
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
