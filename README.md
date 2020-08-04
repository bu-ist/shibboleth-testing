# shibboleth-testing

This will do simple Shibboleth IdP login checks.  It has only been tested with the Boston University Shibboleth IdP.  It can be used in a few different ways:

## Install

### Command line on system

The default `docker-compose.yml` file can be used to start a standalone Selenium server in the background which can then be used by the tool.  This requires
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
 
