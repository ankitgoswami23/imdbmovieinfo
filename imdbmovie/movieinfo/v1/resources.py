from flask import request
from flask_restful import Resource


# class SoftwareManagement(Resource):
#     """
#     Class created to handle the request coming to Process Controller from different Channel Adapters
#     """
#
#     def __init__(self):
#         pass
#
#     def post(self):
#         """
#         Handle POST requests.
#         :return:
#         """
#         return_resp = None
#         try:
#             data, response = request.get_json(force=True), 'processing'
#             logger.log_incoming_request(request=request)
#             logger.log_info(msg=f"PROCESS CONTROLLER REQUEST : {data}")
#
#             return ProcessControllerRequest().validate_parameter(data)
#         except Exception as e:
#             logger.log_exception(msg=str(e), exc_info=True)
#             return return_resp, 503

class TestAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        return "Succdsadasdsess"