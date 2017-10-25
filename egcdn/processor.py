"""Abstract processor implementation."""
import abc


class BaseProcessor(abc.ABC):
    """Abstract processor

    Every processor implementation must inherit this
    class to be usable. Child must implement a method
    called `process` which takes in raw data as argument
    and returns a file name/url or `None`. This file name/url
    will be sent to the client as response.
    """

    @abc.abstractmethod
    def process(self, data):
        """Process data and return a file name/url."""
        pass
