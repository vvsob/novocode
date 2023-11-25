from .icpc import format_icpc
from .common import format_testing, format_judge_error


def format_verdict(verdict):
    formatters = {
        'testing': format_testing,
        'icpc': format_icpc,
        'judge_error': format_judge_error
    }
    return formatters[verdict['format']](verdict)
