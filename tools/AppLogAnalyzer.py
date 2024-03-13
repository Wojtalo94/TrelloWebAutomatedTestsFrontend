import time
import json
import logging


class AppLogAnalyzer():
    def __init__(self, driver):
        self._logger = logging.getLogger("AppLogAnalyzer")
        self.driver = driver

    def clear_first_logs(self):
        # Sleep needed to get last log entry.
        time.sleep(0.3)
        self.driver.get_log('performance')

    def _get_app_logs(self):
        # Sleep needed to get last log entry.
        time.sleep(0.3)
        logs = self.driver.get_log('performance')      
        with open('logs/app_tests_logs.log', 'a') as f:
            for entry in logs:
                f.write(str(entry) + '\n')
        return logs

    def _filter_logs(self, request_will_be_sent: bool = False, response_received: bool = False):
        logs = self._get_app_logs()
        filtered_logs = []
        for entry in logs:
            log_entry = json.loads(entry['message'])
            if 'message' in log_entry:
                message = log_entry['message']
                if 'method' in message:
                    method = message['method']
                    if request_will_be_sent:
                        if method == "Network.requestWillBeSent":
                            filtered_logs.append(log_entry)
                    if response_received:
                        if method == "Network.responseReceived":
                            filtered_logs.append(log_entry)
        return filtered_logs
    
    def check_request_will_be_sent(self):
        filtered_logs = self._filter_logs(request_will_be_sent=True)
        for log_entry in filtered_logs:
            message = log_entry['message']
            method = message['method']
            assert method == "Network.requestWillBeSent", f"Logs from app: '{method}'"

    def check_request_will_not_be_sent(self):
        filtered_logs = self._filter_logs(request_will_be_sent=True)
        if not filtered_logs:
            self._logger.info("No logs to check")
        for log_entry in filtered_logs:
            message = log_entry['message']
            method = message['method']
            assert method != "Network.requestWillBeSent", f"Logs from app: '{method}'"

