import grpc
//from jio.brain.proto.knowledge.api.data.get_all_children_pb2 import GetAllChildrenRequest
//from jio.brain.proto.knowledge.api.data.get_all_children_pb2_grpc import GetAllChildrenServiceStub

class KGDispatcher:
    '''
    TODO
    '''
    def __init__(self):
        self.host = "localhost"

    def get_all_children(self,request):
        channel = grpc.insecure_channel(f"{self.host}:31038")
        stub = GetAllChildrenServiceStub(channel)
        try:
            request = GetAllChildrenRequest(
                predicate_name = request["predicate_name"],
                from_node = request["from_node"]
            )
            response = stub.serve(request)
            return response
        except Exception as e:
            return str(e)
