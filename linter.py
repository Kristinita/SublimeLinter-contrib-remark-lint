from SublimeLinter.lint import Linter, util


class RemarkLint(Linter):
    syntax = ("markdown")
    cmd = ("remark", "--use", "remark-preset-lint-markdown-style-guide")
    regex = (
        r'^\s+(?P<line>\d+):(?P<col>\d+)(?:-\d+:\d+)?\s{2}'
        r'(?P<error>error)?(?P<warning>warning)?\s{2}'
        r'(?P<message>(?:\S+)(?:\s{1}\S+)*)(?:\s{2,}\S+\s{2,}\S+)?$'
        )
    error_stream = util.STREAM_STDERR
