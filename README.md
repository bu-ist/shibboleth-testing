# shibboleth-testing

This will do simple Shibboleth IdP login checks.  It has only been tested with the Boston University Shibboleth IdP.  It can be used in a few different ways:

## Install

### Command line on system

The default `docker-compose.yml` file can be used to start a standalone Selenium server in the background which can then be used by the tool.  This requires `docker-compose` on the local system.  If you don't have it you can run it manually as:

```
$ docker run -d --name selenium -p 4444:4444 selenium/standalone-chrome
```

that the python3 interpreter have the `selenium` module.  This can be installed with the following if you have virtualenv:

```
  $ mkdir pythonenv
  $ virtualenv pythonenv
  $ . pythonenv/bin/activate
  $ pip install selenium
```

Or globally for the system by doing:

```
  $ sudo yum install python3-pip
  $ sudo pip install selenium
```

### VSCode devcontainer

This should be as straightforward as `Ctrl-Shift-P` and typing `Remote-Container: Reopen window in container`

## Password configuration

The username/password combinations are stored in a json file - edit `sample-.bupw.json` to reflect the username/passwords you want to use for testing and store in `${HOME}/.bupw.json`
 
## Running tests

### Running in VSCode

Use `Control-X Control D` to bring up the Debug panel.  You can then select which backend you want to test in the pop up and 
click the run button.  This helps development of the tool since you can set breakpoints and test configurations.

### Manual 

The `shiblogin.py` program is configured using the following environment variables (with default in parentheses):
- `LANDSCAPE` (`prod`) Selects which landscape we are testing to set general defaults.
- `SHIB_HOST` (set by `LANDSCAPE`) The Shibboleth IdP to test - this can be a load balancer or even a backend system.
- `SHIB_SP` (set by `LANDSCAPE`) The Shibboleth SP entity-ID to use for the IdP initiated authentication - generally the Shibboleth verify system if available. 