import re
import os
from ast import literal_eval as make_tuple

def select(key):
    """ 
    Reads the file data\{key} from the data directory and returns its contents.

    Returns file contents or None if the file does not exist.
    """
    
    pass

def upsert(key, value):
    """
    Writes data\{key} with the contents of `value`

    Returns nothing.
    """
    
    pass

def delete(key):
    """
    Deletes data\{key}. Does nothing if data\{key} already exists.

    Returns nothing.
    """
    pass

def execute(query):
    """
    >>> execute("delete from data where key=1")
    >>> execute("select value from data where key=1")

    >>> execute("insert or update into data (key, value) values (1,'first')")
    >>> execute("select value from data where key=1")
    'first'

    >>> execute("insert or update into data (key, value) values (2,'second')")
    >>> execute("select value from data where key=2")
    'second'

    >>> execute("delete from data where key=1")
    >>> execute("select value from data where key=1")

    >>> execute("select value from data where key=2")
    'second'
    """

    statement_type = query.split()[0].lower()
    
    if statement_type == 'select':
        key = int(query.split('=')[-1])
        return select(key)

    if statement_type == 'delete':
        values = re.split('values', query, flags=re.I)[-1].strip()
        key = int(query.split('=')[-1])
        return delete(key)

    if statement_type == 'insert':
        values = re.split('values', query, flags=re.I)[-1].strip()
        key, value = make_tuple(values)
        return upsert(key, value)

    raise ValueError("Invalid SQL Expression")

if __name__ == '__main__':
    while True:
        expr = input('> ')
        print(execute(expr))