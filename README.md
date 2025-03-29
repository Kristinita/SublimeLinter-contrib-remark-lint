## 1. SublimeLinter-contrib-remark-lint

This linter plugin for [**SublimeLinter**](https://github.com/SublimeLinter/SublimeLinter)
provides an interface to [**remark-lint**](https://github.com/remarkjs/remark-lint).
It will be used with files that have the “Markdown" syntax.

## 2. Installation

SublimeLinter must be installed in order to use this plugin.

Please use [**Package Control**](https://packagecontrol.io) to install the linter
plugin.

Before installing this plugin, you must ensure that remark-cli is installed
on your system. This can be done using the command:

```shell
npm install --global remark-cli
```

Your [**presets**](https://www.npmjs.com/search?q=remark-preset) and/or [**rules**](https://github.com/remarkjs/remark-lint#rules) must be installed locally. Example command:

```shell
npm install --save-dev remark-preset-lint-markdown-style-guide preset-lint-recommended
```

See **<https://github.com/remarkjs/remark-lint>** for more details.

You must have the [**Remark configuration file**](https://github.com/remarkjs/remark/tree/main/packages/remark-cli#example-config-files-json-yaml-js).

In order for remark-cli to be executed by SublimeLinter, you must ensure
that its path is available to SublimeLinter. The docs cover [**troubleshooting PATH configuration**](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## 3. Settings

1. SublimeLinter settings: **<http://sublimelinter.readthedocs.org/en/latest/settings.html>**
1. Linter settings: **<http://sublimelinter.readthedocs.org/en/latest/linter_settings.html>**
