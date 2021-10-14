Migrating your code from v1 to v2
=======================================

Changes to base API convenience methods
---------------------------------------

stabila.toDecimal()
~~~~~~~~~~~~~~~~~

In v4 ``stabila.toDecimal()`` is renamed: :meth:`~stabila.toInt` for improved clarity. It does not return a :class:`decimal.Decimal`, it returns an :class:`int`.


Removed Methods
~~~~~~~~~~~~~~~~~~

- ``stabila.toUtf8`` was removed for :meth:`~stabila.toText`.
- ``stabila.fromUtf8`` was removed for :meth:`~stabila.toHex`.
- ``stabila.toAscii`` was removed for :meth:`~stabila.toBytes`.
- ``stabila.fromAscii`` was removed for :meth:`~stabila.toHex`.
- ``stabila.fromDecimal`` was removed for :meth:`~stabila.toHex`.

Provider Access
~~~~~~~~~~~~~~~~~

In v2, ``stabila.currentProvider`` was removed, in favor of ``stabila.providers``.

Disambiguating String Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of places where an arbitrary string input might be either
a byte-string that has been hex-encoded, or unicode characters in text.
These are named ``hexstr`` and ``text`` in stabilaAPI.
You specify which kind of :class:`str` you have by using the appropriate
keyword argument. See examples in :ref:`overview_type_conversions`.

In v1, some methods accepted a :class:`str` as the first positional argument.
In v2, you must pass strings as one of ``hexstr`` or ``text`` keyword arguments.

Notable methods that no longer accept ambiguous strings:

- :meth:`~stabila.sha3`
- :meth:`~stabila.toBytes`