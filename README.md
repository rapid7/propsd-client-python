A python-based client for propsd
--------

[Propsd](https://github.com/rapid7/propsd) does dynamic property management at scale, across thousands of servers and changes from hundreds of developers.

This python client allows applications to interact with the propsd service.

Installation
--------

`pip install git+https://github.com/rapid7/propsd-client-python.git@0.1.0`

Example usage
--------

Create a client:
```
import propsd
import sys

client = propsd.Client()
```

Print a property:
```
print(client.get(sys.argv[1]))
```

Subscribe to property changes (the search parameter is [objectpath](http://objectpath.org/reference.html) syntax):
```
def updated(search, properties, search_result):
  print("new value is %s" % search_result)

client.subscribe("$.'%s'" % sys.argv[1], updated)
```
