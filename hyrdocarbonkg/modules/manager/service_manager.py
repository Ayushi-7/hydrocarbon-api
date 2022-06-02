import importlib
import logging as logger
from hydrocarbonkg.utils.logs import config as logconfig

from hydrocarbonkg.modules.worker.api.get_all_disease import GetAllEquipment
from hydrocarbonkg.modules.worker.api.get_all_symptom import GetAllFluids

def worker_factory(api_name):
    '''
    Factory Methods for Knowledge Graph Service Workers
    '''
    workers = {
        "GetAllEquipment": GetAllEquipmentWorker,
        "GetAllFluids": GetAllFluidsWorker
    }
    
    return workers[api_name]()

def execute(request, api_name):
    logger.debug(logconfig.EXECUTE)
    knowledge_service_response = None
    worker = worker_factory(api_name)

    knowledge_service_request, status = worker.transform_request(request)

    if status['is_ok'] == False:
        logger.error(status)
        knowledge_service_response = None
        return worker.transform_response(
            knowledge_service_response,
            status
        )

    knowledge_service_response, status = worker.do(knowledge_service_request, status)

    if status['is_ok'] == False:
        logger.error(status)
        knowledge_service_response = None
        return worker.transform_response(
            knowledge_service_response,
            status
        )

    logger.debug(logconfig.EXECUTED)

    return worker.transform_response(
        knowledge_service_response,
        status
    )
