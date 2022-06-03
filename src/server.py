import os
import grpc
from concurrent import futures
from dotenv import load_dotenv
from utils.logs.logger import get_logger
from modules.manager.service_manager import execute
//import jio.brain.proto.knowledge.hydrocarbon.api.hydrocarbon_kg_service_pb2_grpc as hydrocarbon_knowledge_service

logger = get_logger("root", "server")

'''
	i/p: API specific request
	o/p: API specific response
'''
class HydrocarbonApiService(hydrocarbon_service.HydrocarbonApiServiceServicer):
	'''
	i/p: None
	o/p: List of Disease ID and Name
	'''
	def GetAllEquipment(self, request, context):
		logger.debug("GetAllEquipment request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ALL_EQUIPMENT'),
			request = request
		)
	
	def GetAllFluid(self, request, context):
		logger.debug("GetAllFluid request received in servicer")
		return execute(
			api_name = os.getenv('API.GET_ALL_FLUID'),
			request = request
		)
  
if __name__ == "__main__":
	'''
	Start Method starts the Hydrocarbon API Server
	'''
	load_dotenv()
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(os.getenv('MAX_WORKERS'))))
	hydrocarbon_service.add_HydrocarbonApiServiceServicer_to_server(HydrocarbonApiService(), server)
	server.add_insecure_port('[::]:' + str(os.getenv('SERVER_PORT')))
	server.start()
	print('Starting server. Listening on port %s.'%str(os.getenv('SERVER_PORT')))
	server.wait_for_termination()
