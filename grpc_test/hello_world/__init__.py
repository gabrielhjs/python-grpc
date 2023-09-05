import grpc
from .protos import hello_world_pb2, hello_world_pb2_grpc
import asyncio


class Greeter(hello_world_pb2_grpc.GreeterServicer):
    async def SayHello(
        self, request: hello_world_pb2.HelloRequest, context: grpc.aio.ServicerContext
    ):
        for _ in range(0, 5):
            yield hello_world_pb2.HelloResponse(response=f"Hello, {request.name}")
            await asyncio.sleep(5)
