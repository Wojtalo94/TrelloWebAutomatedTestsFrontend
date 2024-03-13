import logging
import json
from .Request import Request


class RestController():
    def __init__(self):
        self._logger = logging.getLogger("AppController")
        self._request = Request()
    
    def check_member_type(self):
        self._logger.info("Check member type")
        response, _ = self._request.get_all_boards_members()
        member_type = response[0]['memberType']
        return member_type

    def check_member_deactivation(self):
        self._logger.info("Check member status")
        response, _ = self._request.get_all_boards_members()
        deactivated_status = response[0]['deactivated']
        return deactivated_status