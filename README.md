A python-based client for propsd
--------

[Propsd](https://github.com/rapid7/propsd) does dynamic property management at scale, across thousands of servers and changes from hundreds of developers.

This python client allows applications to interact with the propsd service.

Installation
--------

`pip install git+https://github.com/rapid7/propsd-client-python.git@0.1.0`

Example usage
--------

```
import propsd
import sys

# create the propsd client
client = propsd.Client()

# print a variable
print(client.get(sys.argv[1]))

# define a property update callback and register it
def updated(search, properties, search_result):
  print("new value is %s" % search_result)
client.subscribe("$.'%s'" % sys.argv[1], updated)
```
