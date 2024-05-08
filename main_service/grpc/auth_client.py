import grpc
import main_service.protos.gen.proto.Auth_pb2_grpc as auth


async def Client():
    chanel = grpc.insecure_channel("localhost:8002")
    return auth.AuthServerStub(chanel)

