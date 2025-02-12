"""
A simple greeting module
"""


def hello(name: str = "World"):
    """
    >>> hello()
    Hello World!
    >>> hello('buddy')
    Hello buddy!
    """
    print(f"Hello {name}!")
