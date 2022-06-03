import logging as logger
import hydrocarbonkg.utils.logs.config as logconfig
from google.protobuf import json_format
from hydrocarbonkg.modules.worker.utils.config import status 
from hydrocarbonkg.modules.worker.utils.validate_kg_response import validate_kg_response
from google.protobuf.json_format import MessageToDict
from hydrocarbonkg.modules.dispatcher.kg_dispatcher import KGDispatcher
//from jio.brain.proto.knowledge.healthcare.req_res.get_all_disease_pb2 import GetAllEquipmentResponse......
import copy

class GetAllEquipmentWorker:

    def __init__(self):
        '''
        __init__ is the constructor for a class. 
        The self parameter refers to the instance of the object 
        '''
        pass 

    def transform_request(self, request):
        
        logger.debug(logconfig.PREPROCESSING)
        knowledge_request = {"predicate_name": "is_a", "from_node": "hydrocarbon_equipment"}
        logger.debug(logconfig.PREPROCESSING_COMPLETED)
        return knowledge_request, status

    def do(self, request, status):

        dispatcher = KGDispatcher()
        response = dispatcher.get_all_children(request)
        response, dispatcher_status = validate_kg_response(response)
        if not response:
            return None, dispatcher_status
        return response, dispatcher_status

    def transform_response(self, response, status):
                                                   
        logger.debug(logconfig.POSTPROCESSING)

        if not response:
            response = GetAllDiseaseResponse(status = status)        
        else:
            response_obj = []
            to_node_list = response.to_node

            for node in to_node_list:
                response_obj.append({"id": node.id, 
                                    "entity_type": node.entity_type,
                                    "name": node.name,
                                    "display_name": node.display_name})
            
            response = GetAllDiseaseResponse(disease = response_obj, status = status)
            
        logger.debug(logconfig.POSTPROCESSING_COMPLETED)
        return response
