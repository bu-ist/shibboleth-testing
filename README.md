# shibboleth-testing

This will do simple Shibboleth IdP login checks.  It has only been tested with the Boston University Shibboleth IdP.  It can be used in a few different ways:

## Install

### VSCode devcontainer

This should be as straightforward as `Ctrl-Shift-P` and typing `Remote-Container: Reopen window in container`

### Command line on system

The default `docker-compose.yml` file can be used to start a standalone Selenium server in the background which can then be used by the tool.  This requires `docker-compose` on the local system.  If you don't have it you can run it manually as:

```
$ docker run -d --name selenium -p 4444:4444 selenium/standalone-chrome
```

that the python3 interpreter have the `selenium` module.  This can be installed with the following if you have virtualenv:

```
  $ mkdir ~/pythonenv
  $ virtualenv ~/pythonenv
  $ . ~/pythonenv/bin/activate
  $ pip install selenium
```

Or globally for the system by doing:

```
  $ sudo yum install python3-pip
  $ sudo pip install selenium
```

## Password configuration

The username/password combinations are stored in a json file - edit `sample-.bupw.json` to reflect the username/passwords you want to use for testing and store in `${HOME}/.bupw.json`
 
## Running tests

### Running in VSCode

Use `Control-X Control D` to bring up the Debug panel.  You can then select which backend you want to test in the pop up and 
click the run button.  This helps development of the tool since you can set breakpoints and test configurations.

### Manual 

The `shiblogin` command has the following help:

```bash
$ ./shiblogin --help
usage: shiblogin [-h] [--landscape LANDSCAPE] [--host HOST] [--sp SP]
                 [--pwfile PWFILE] [--verbose]

Test Shibboleth authentication using Selenium

optional arguments:
  -h, --help            show this help message and exit
  --landscape LANDSCAPE
  --host HOST           Shibboleth IdP hostname
  --sp SP               SP entity-ID to test
  --pwfile PWFILE       JSON file contains passwords
  --verbose             Verbose output
```

Here is an example of validating the shib-test infrastructure including on-prem and AWS:

```bash
$ ./shiblogin --landscape test --host shib-test-crc.bu.edu
OK: Validated shib-test-crc.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
$ ./shiblogin --landscape test --host ist-shib-idp-test04.bu.edu
OK: Validated ist-shib-idp-test04.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
$ ./shiblogin --landscape test --host ist-shib-idp-test04.bu.edu
OK: Validated ist-shib-idp-test04.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
$ ./shiblogin --landscape test --host shib-test-aws.bu.edu
OK: Validated shib-test-aws.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
$ ./shiblogin --landscape test --host ist-idp-test101.bu.edu
OK: Validated ist-idp-test101.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
$ ./shiblogin --landscape test --host ist-idp-test102.bu.edu
OK: Validated ist-idp-test102.bu.edu IdP using http%3A%2F%2Fist-shib-verify-syst.bu.edu%2Fshibboleth SP Entity-ID|ret=1
```