"""Contains functionality related to Lines"""
import json
import logging

from models import Line


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Lines:
    """Contains all train lines"""

    def __init__(self):
        """Creates the Lines object"""
        ##logger.info(f"DEBUG (lines 1) Lines init")
        self.red_line = Line("red")
        self.green_line = Line("green")
        self.blue_line = Line("blue")

    def process_message(self, message):
        """Processes a station message"""
        print(f"DEBUG {message.topic()}")
        if "com.udacity.station" in message.topic():
            value = message.value()
        elif message.topic() == "connect.stations.table":
            value = json.loads(value)

        if value["line"] == "green":
            self.green_line.process_message(message)
        elif value["line"] == "red":
            self.red_line.process_message(message)
        elif value["line"] == "blue":
            self.blue_line.process_message(message)
        else:
            logger.info("discarding unknown line msg %s", value["line"])
        
        if message.topic() == "TURNSTILE_SUMMARY":
            self.green_line.process_message(message)
            self.red_line.process_message(message)
            self.blue_line.process_message(message)
        else:
            logger.info("ignoring non-lines message %s", message.topic())
            
            
#         """Processes a station message"""
#         logger.info(f"DEBUG (lines 2) {self.message}")
# ##        if "org.chicago.cta.station" in message.topic():
#         if "com.udacity.station" in message.topic():
#             logger.info(f"DEBUG (lines 3a) {message.topic()}")
#             value = message.value()
# ##            if message.topic() == "org.chicago.cta.stations.table.v1":
#         elif message.topic() == "connect.stations.table":
#             value = json.loads(message)
#             logger.info(f"DEBUG (lines 3b) {value}")
#             if value["line"] == "green":
#                 self.green_line.process_message(message)
#             elif value["line"] == "red":
#                 self.red_line.process_message(message)
#             elif value["line"] == "blue":
#                 self.blue_line.process_message(message)
#             else:
#                 logger.debug("discarding unknown line msg %s", value["line"])
#         elif "TURNSTILE_SUMMARY" == message.topic():
#             logger.info("DEBUG (lines 3c) %s", message.topic())
#             self.green_line.process_message(message)
#             self.red_line.process_message(message)
#             self.blue_line.process_message(message)
#         else:
#             logger.info("ignoring non-lines message %s", message.topic())
