FSKV
====

A simple key-value store implemented directly on the file system.

Overview
--------

The fskv.py file provides a very basic framework to interacting with files on the file system using a limited SQL dialect. Supported operations:

- `insert or update into data (key, value) values (7, 'value')` - Writes a file named `data/7` containting the text "value".
- `select value from data where key=7` - Gets the contents of the file named `data/7`.
- `delete from data where key=7` - Removes the file named `data/7`.

Assignment
----------

The provided Python file `fskv.py` is missing the implementation for three key functions. Implement these functions such that all supplied doctests pass.

Doctests may be run either using:

`make`

or by directly calling:

`python3 -m doctest fskv.py`
