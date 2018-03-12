# SublimeLinter-contrib-remark-lint

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-remark-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-remark-lint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)
provides an interface to [remark-lint](https://github.com/remarkjs/remark-lint).
It will be used with files that have the “markdown" syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter
plugin.

Before installing this plugin, you must ensure that `remark-lint` is installed
on your system. This can be done using the command:
```bash
sudo npm install -g remark remark-preset-lint-markdown-style-guide
```
See <https://github.com/remarkjs/remark-lint> for more details.

In order for `remark-lint` to be executed by SublimeLinter, you must ensure
that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: <http://sublimelinter.readthedocs.org/en/latest/settings.html>
- Linter settings: <http://sublimelinter.readthedocs.org/en/latest/linter_settings.html>