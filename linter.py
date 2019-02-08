"""SublimeLinter-remark."""
from SublimeLinter.lint import Linter
from SublimeLinter.lint import util


class RemarkLint(Linter):  # pylint: disable=too-few-public-methods
    """remark implementation for SublimeLinter.

    Lint Markdown via remark:
    https://remark.js.org/

    Extends:
        Linter

    Variables:
        cmd {string} -- remark command
        regex {tuple} -- parsing regex
        error_stream {string} -- parse STDERR
        defaults {dict} -- scopes, where remark will accepted
    """

    cmd = 'remark --no-stdout'
    regex = (
        r'^\s+(?P<line>\d+):(?P<col>\d+)(?:-\d+:\d+)?\s{2}'
        r'(?P<error>error)?(?P<warning>warning)?\s{2}'
        r'(?P<message>(?:\S+)(?:\s{1}\S+)*)(?:\s{2,}\S+\s{2,}\S+)?$'
    )
    error_stream = util.STREAM_STDERR
    defaults = {
        "selector": "text.html.markdown"
    }
