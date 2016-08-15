A python-based client for propsd
--------

[Propsd](https://github.com/rapid7/propsd) does dynamic property management at scale, across thousands of servers and changes from hundreds of developers.

This python client allows applications to interact with the propsd service.

Installation
--------

`pip install git+https://github.com/rapid7/propsd-client-python.git@0.1.1`

Usage
--------

Create a client:
```
import propsd
import sys

client = propsd.Client()
```

Print a property (returns `None` if the property is unset or if there is an error):
```
print(client.get('someproperty'))
```

Print the entire property set (returns `None` if there is an error):
```
print(client.properties())
```

Subscribe to property changes (the search parameter is [objectpath](http://objectpath.org/reference.html) syntax):
```
def updated(search, properties, search_result):
  print("new value is %s" % search_result)

client.subscribe("$.'%s'" % 'someproperty', updated)
```

Dump the status of the propsd service:
```
print(client.status())
```

Dump the health of the propsd service:
```
print(client.health())
```

Example usage
-------

(test.py):
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
input()
```

`$ python test.py someproperty`
