"""Worker process implementation."""
import logging

import kombu
import kombu.mixins as mixins
import magic

from . import responses
from . import processor


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
                on_message=self.on_message,
                prefetch_count=1,
            )
        ]

    def start(self):
        """Start the worker process."""
        with kombu.Connection(self._url) as conn:
            self._logger.debug('Starting worker ID:{}'.format(self._id))
            self.connection = conn
            self.run()

    def on_message(self, message):
        """Recieve binary data and process it."""
        self._logger.debug('[{}] Data recieved.'.format(self._id))
        response = self._process_data(message.payload)
        self._send_response(response, message.properties['correlation_id'])
        message.ack()

    def _process_data(self, data):
        """Process and make reports to send to the client."""
        mime = self._detect_mime(data)
        self._logger.info('[{}] {} mime detected.'.format(self._id, mime))
        if not mime:
            return responses.NoMimeErrResponse()
        proc = self._get_processor(mime)
        if not proc:
            return responses.NoProcessorDefined()
        if not isinstance(proc, processor.BaseProcessor):
            return responses.InvalidProcessorFound()
        url = proc.process(data)
        if not url:
            return responses.NoUrlGenerated()
        return responses.BaseResponse(filename=url)

    def _detect_mime(self, data):
        """Detect the mime type of `data`.

        :return Mime type as string or `None`
        """
        try:
            mime = magic.from_buffer(data, mime=True)
            return mime
        except Exception as err:
            self._logger.error('[{}] Could not parse mime type. {}'.format(
                self._id, err
            ))

    def _get_processor(self, mime):
        """Find a suitable processor from `egcdn.pluggables` package.

        :return The processor instance or `None`
        """
        proc = None
        return proc

    def _send_response(self, response, correlation_id):
        """Send the response to the client."""
        self.producer.publish(
            response,
            exchange=self._response_exchange,
            declare=[self._response_exchange, ],
            delivery_mode=2,
            routing_key=correlation_id,
            correlation_id=correlation_id,
            retry=True,
        )
