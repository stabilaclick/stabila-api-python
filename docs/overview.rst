Overview
========

.. contents:: :local:

The common entrypoint for interacting with the stabila library is the ``stabila``
object.  The stabila object provides APIs for interacting with the stabila
blockchain, typically by connecting to a HTTP server.

Providers
---------

*Providers* are how stabila connects to the blockchain.  The stabilaAPI library comes
with a the following built-in providers that should be suitable for most normal
use cases.

- ``HttpProvider`` for connecting to http and https based servers.

The ``HttpProvider`` takes the full URI where the server can be found.  For
local development this would be something like ``http://localhost:8090``.


.. code-block:: python

    >>> from stabilaapi import HttpProvider, stabila

    # Note that you should create only one HttpProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and stabila node

    >>> full_node = HttpProvider('http://localhost:8090')
    >>> solidity_node = HttpProvider('http://localhost:8090')
    >>> event_server = HttpProvider('http://localhost:8090')

    >>> stabila = stabila(full_node, solidity_node, event_server)


Base API
--------

The ``stabila`` class exposes the following convenience APIs.

.. _overview_type_conversions:

Type Conversions
~~~~~~~~~~~~~~~~

.. py:method:: stabila.toHex(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns it in its hexadecimal representation.

    .. code-block:: python

        >>> stabila.toHex(0)
        '0x0'
        >>> stabila.toHex(1)
        '0x1'
        >>> stabila.toHex(0x0)
        '0x0'
        >>> stabila.toHex(0x000F)
        '0xf'
        >>> stabila.toHex(b'')
        '0x'
        >>> stabila.toHex(b'\x00\x0F')
        '0x000f'
        >>> stabila.toHex(False)
        '0x0'
        >>> stabila.toHex(True)
        '0x1'
        >>> stabila.toHex(hexstr='0x000F')
        '0x000f'
        >>> stabila.toHex(hexstr='000F')
        '0x000f'
        >>> stabila.toHex(text='')
        '0x'
        >>> stabila.toHex(text='cowmö')
        '0x636f776dc3b6'

.. py:method:: stabila.toText(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its string equivalent.
    Text gets decoded as UTF-8.


    .. code-block:: python

        >>> stabila.toText(0x636f776dc3b6)
        'cowmö'
        >>> stabila.toText(b'cowm\xc3\xb6')
        'cowmö'
        >>> stabila.toText(hexstr='0x636f776dc3b6')
        'cowmö'
        >>> stabila.toText(hexstr='636f776dc3b6')
        'cowmö'
        >>> stabila.toText(text='cowmö')
        'cowmö'


.. py:method:: stabila.toBytes(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its bytes equivalent.
    Text gets encoded as UTF-8.


    .. code-block:: python

        >>> stabila.toBytes(0)
        b'\x00'
        >>> stabila.toBytes(0x000F)
        b'\x0f'
        >>> stabila.toBytes(b'')
        b''
        >>> stabila.toBytes(b'\x00\x0F')
        b'\x00\x0f'
        >>> stabila.toBytes(False)
        b'\x00'
        >>> stabila.toBytes(True)
        b'\x01'
        >>> stabila.toBytes(hexstr='0x000F')
        b'\x00\x0f'
        >>> stabila.toBytes(hexstr='000F')
        b'\x00\x0f'
        >>> stabila.toBytes(text='')
        b''
        >>> stabila.toBytes(text='cowmö')
        b'cowm\xc3\xb6'


.. py:method:: stabila.toInt(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its integer equivalent.


    .. code-block:: python

        >>> stabila.toInt(0)
        0
        >>> stabila.toInt(0x000F)
        15
        >>> stabila.toInt(b'\x00\x0F')
        15
        >>> stabila.toInt(False)
        0
        >>> stabila.toInt(True)
        1
        >>> stabila.toInt(hexstr='0x000F')
        15
        >>> stabila.toInt(hexstr='000F')
        15

.. _overview_currency_conversions:

Currency Conversions
~~~~~~~~~~~~~~~~~~~~~

.. py:method:: stabila.toSun(value)

    Returns the value in the denomination specified by the ``currency`` argument
    converted to sun.


    .. code-block:: python

        >>> stabila.toSun(1)
        1000000


.. py:method:: stabila.fromSun(value)

    Returns the value in wei converted to the given currency. The value is returned
    as a ``Decimal`` to ensure precision down to the wei.


    .. code-block:: python

        >>> stabila.fromSun(1000000)
        Decimal('1')


.. _overview_addresses:

Addresses
~~~~~~~~~~~~~~~~

.. py:method:: stabila.isAddress(value)

    Returns ``True`` if the value is one of the recognized address formats.

    .. code-block:: python

        >>> stabila.isAddress('TRWBqiqoFZysoAeyR1J35ibuyc8EvhUAoY')
        True


.. _overview_hashing:


Cryptographic Hashing
~~~~~~~~~~~~~~~~~~~~~

.. py:classmethod:: stabila.sha3(primitive=None, hexstr=None, text=None)

    Returns the Keccak SHA256 of the given value. Text is encoded to UTF-8 before
    computing the hash, just like Solidity. Any of the following are
    valid and equivalent:

    .. code-block:: python

        >>> stabila.sha3(0x747874)
        >>> stabila.sha3(b'\x74\x78\x74')
        >>> stabila.sha3(hexstr='0x747874')
        >>> stabila.sha3(hexstr='747874')
        >>> stabila.sha3(text='txt')
        HexBytes('0xd7278090a36507640ea6b7a0034b69b0d240766fa3f98e3722be93c613b29d2e')

