import logging
import asyncio

import grpc
from grpc_reflection.v1alpha import reflection
from .hello_world.protos import hello_world_pb2, hello_world_pb2_grpc
from .hello_world import Greeter


_cleanup_coroutines = []


async def serve():
    server = grpc.aio.server()
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    SERVICE_NAMES = (
        hello_world_pb2.DESCRIPTOR.services_by_name["Greeter"].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:8000")

    logging.info("Server starting")
    await server.start()
    logging.info("Server started")

    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown")
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())

    except KeyboardInterrupt:
        logging.info("Graceful shutdown")

    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
