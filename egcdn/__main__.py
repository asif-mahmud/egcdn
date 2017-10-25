"""Main entry point for the package."""
import concurrent.futures as futures
import signal
import logging

import kombu

from .config import Configurator
from .server import BasicWorker


def spawn_worker(_id, url, data_exchange, data_queue, response_exchange):
    """Spawn a worker process."""
    try:
        worker = BasicWorker(_id, url, data_exchange,
                            data_queue, response_exchange)
        worker.start()
    except Exception as err:
        logging.getLogger(__name__).error(err)
        return


def main():
    """Entry point for main module."""
    configurator = Configurator()
    configurator.parse()

    client_data_exchange = kombu.Exchange(
        configurator.config.client_data_exchange,
        'topic',
    )
    server_response_exchange = kombu.Exchange(
        configurator.config.server_resp_exchange,
        'topic'
    )
    server_queue = kombu.Queue(
        configurator.config.queue,
        exchange=client_data_exchange,
        routing_key=configurator.config.route,
        auto_delete=True,
    )
    mq_url = '{}://{}:{}@{}:{}'.format(
        configurator.config.protocol,
        configurator.config.user,
        configurator.config.password,
        configurator.config.host,
        configurator.config.port,
    )

    # start up the servers
    logger = logging.getLogger(__name__)
    with futures.ProcessPoolExecutor(
        max_workers=configurator.config.workers
    ) as pool:
        for i in range(0, configurator.config.workers):
            pool.submit(
                spawn_worker,
                i + 1,
                mq_url,
                client_data_exchange,
                server_queue,
                server_response_exchange,
            )

        def signal_handler(signum, frame):
            """Stop the process pool."""
            logger.info('Asking workers to exit.')
            pool.shutdown(wait=False)
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


if __name__ == '__main__':
    main()
