  ## A simple keylogger
  # Title

**BoomBoomKeylogger**

# Description

Welcome to the Simple keylogger repo! A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer.
#
Check out below to learn how to install them. These keyloggers are simple and bare bones, however they work great!

## Installation

#### Download the repository

```bash
$ git clone https://github.com/Rabin321/Boomboomkeylogger.git
```
```bash
$ make && make install
```

It will log to victim_info.txt. This may require root access, but you can change that if you want. Set where you want it to log:

```bash
$ keylogger ~/logfile.txt
```




Want to make it start on system startup?
```bash
$ sudo make startup
```



That will run it on startup.

#### Uninstall
```bash
$ sudo make uninstall
```


Will uninstall the program, but not the logs.


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pynput.

```bash
pip install pynput
```

## Uses
Some uses of a keylogger are:

-Business Administration: Monitor what employees are doing.

-School/Institutions: Track keystrokes and log banned words in a file.

-Personal Control and File Backup: Make sure no one is using your computer 
 when you are away.

-Parental Control: Track what your children are doing.
Self analysis
