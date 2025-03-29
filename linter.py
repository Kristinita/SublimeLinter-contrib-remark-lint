"""[OVERVIEW] SublimeLinter plugin for Remark.

[REMARK][INFO] Remark — the ecosystem of plugins that work with Markdown:
https://remark.js.org/

[REMARK][INFO] remark-cli — the command-line Remark interface.
https://github.com/remarkjs/remark/tree/main/packages/remark-cli

[REMARK][INFO] remark-lint — Remark plugins for checking Markdown code style:
https://github.com/remarkjs/remark-lint

[REMARK][INFO] remark-parse — the default Markdown parser of Remark:
https://github.com/remarkjs/remark/tree/main/packages/remark-parse
"""
from SublimeLinter.lint import Linter
from SublimeLinter.lint import util


class RemarkLint(Linter):  # pylint: disable=too-few-public-methods
    """[CLASS_DESCRIPTION] Parse Remark output with SublimeLinter.

    [LEARN][SUBLIMELINTER] Attributes of SublimeLinter plugins:
    https://sublimelinter.readthedocs.io/en/latest/linter_attributes.html

    Extends:
        Linter

    Variables:
        1. cmd {string} -- the remark-cli command
        2. defaults {dict} -- scopes for SublimeLinter Remark plugin
        3. error_stream {string} -- capture Remark standard streams
        4. regex {regex} -- the regular expression for parsing remark-cli stderr
    """

    # [CLI][REMARK] “--no-stdout” — don’t print file content to console
    #
    # [LEARN][SUBLIMELINTER] “${args}” — additional user arguments for remark-cli command:
    # https://sublimelinter.readthedocs.io/en/latest/linter_attributes.html#cmd-mandatory
    cmd = "remark --no-stdout ${args}"

    # [SUBLIME][INFO] “text.html.markdown” is the syntax scope of the “Markdown” syntax
    # from the “MarkdownEditing” package:
    # https://github.com/SublimeText-Markdown/MarkdownEditing/blob/88499d3bc4d25eedf472aff7cf160d82b1713182/syntaxes/Markdown.sublime-syntax#L13
    #
    # [LEARN][SUBLIME] “Syntax scopes” in Sublime Text:
    # https://kristinita.netlify.app/it-articles/how-to-get-current-%E2%80%A6-in-sublime-text#Syntax-scope
    defaults = {
        "selector": "text.html.markdown"
    }

    # [REMARK][INFO] Remark returns warnings solely to stderr
    error_stream = util.STREAM_STDERR

    # [REMARK][INFO] remark-lint returns solely warnings, not errors:
    # https://github.com/remarkjs/remark-lint#configure
    #
    # [LEARN][MARKDOWN] Markdown hasn’t such thing as “non-valid syntax”,
    # therefore, Markdown parsers doesn’t return parsing errors:
    # https://stackoverflow.com/a/5508742/5951529
    #
    #
    # [REMARK][REPORTER] vfile-reporter is the default reporter for remark-lint:
    # https://github.com/unifiedjs/unified-args#--report-reporter
    # https://github.com/vfile/vfile-reporter
    #
    # [REMARK][REPORTER] Example output of vfile-reporter:
    # 5:3      warning Remove 1 line before node  no-consecutive-blank-lines  remark-lint
    # 5:3-5:10 warning Marker style should be `+` unordered-list-marker-style remark-lint
    regex = r"^(?P<line>\d+):(?P<col>\d+)(?:-\d+:\d+)?\s+(?P<warning>warning)\s+(?P<message>.*)$"
