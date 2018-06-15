A python-based client for propsd
--------

[Propsd](https://github.com/rapid7/propsd) does dynamic property management at scale, across thousands of servers and changes from hundreds of developers.

This python client allows applications to interact with the propsd service.

Installation
--------

To use propsd-client-python in your local python environment, run the following, replacing `<release>` with the [release](releases) you wish to use

```
pip install git+https://github.com/rapid7/propsd-client-python.git@<release>
```

If you wish to use this inside of an existing Python project, in requirements.txt ensure that a line like the following exists, again replacing `<release>` with the [relese](releases) you wish to use:

```
propsd==<release>
```

And then, in setup.py, ensure that a snippet like the following exists, again substituting `<release>` as appropriate:

```
...
    dependency_links=[
        'git+https://github.com/rapid7/propsd-client-python.git@<release>#egg=propsd-<release>'
    ]
...
```

Note that you'll need to use the `--process-dependency-links` option to `pip` to install.

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

Shut down the client when you're done:
```
client.shutdown()
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

# don't forget to shut down
client.shutdown()
```

`$ python test.py someproperty`

API documentation
-------
Read up on [propsd-client-python.readthedocs.io](http://propsd-client-python.readthedocs.io/en/latest/propsd.html#module-propsd).
