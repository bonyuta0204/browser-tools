# browser-tools
ブラウザを用いた自動化ツール

# prerequisite
This tool uses Selenium chrome driver.
chromedriver is required to this application.

[chromedriver](https://chromedriver.chromium.org/downloads)

# install
```sh
pip3 install git+ssh://git@github.com/bonyuta0204/browser-tools.git
```

# usage
```
Usage: browser-tools [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  shukkin
  taikin
```

```
Usage: browser-tools shukkin [OPTIONS] EMAIL PASSWORD

Arguments:
  EMAIL     [required]
  PASSWORD  [required]

Options:
  --help  Show this message and exit.
```

```
Usage: browser-tools taikin [OPTIONS] EMAIL PASSWORD

Arguments:
  EMAIL     [required]
  PASSWORD  [required]

Options:
  --help  Show this message and exit.
```
