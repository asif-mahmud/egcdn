"""Worker process implementation."""
import logging

import kombu
import kombu.mixins as mixins


class BasicWorker(mixins.ConsumerProducerMixin):
    """Basic implementation of a worker."""

    def __init__(self, _id, url, data_exchange, data_queue, response_exchange):
        """Initialize a worker.

        :param url: Message Queue server's url.
        """
        self._id = _id
        self._url = url
        self._data_exchange = data_exchange
        self._data_queue = data_queue
        self._response_exchange = response_exchange
        self._logger = logging.getLogger(__name__)

    def get_consumers(self, Consumer, channel):
        """Get consumer for this worker."""
        return [
            Consumer(
                queues=[self._data_queue, ],
                callbacks=[self.rcv_data, ],
                prefetch_count=1,
            )
        ]

    def start(self):
        """Start the worker process."""
        with kombu.Connection(self._url) as conn:
            self._logger.info('Starting worker ID:{}'.format(self._id))
            self.connection = conn
            self.run()

    def rcv_data(self, data, message):
        """Recieve binary data and process it."""
        message.ack()
