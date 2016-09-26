# coding: utf-8
from slackclient import SlackClient

from slackcop import log


class BotCore():
    def __init__(self, slack_token, rules):
        self.sc = SlackClient(slack_token)
        self.rules = rules

    def _notify(self, message):
        response = self.sc.api_call("chat.postMessage", **message)
        if not response.get("ok"):
            log_message = response.get("error") + "failed post message :" + str(message).strip()
            log.error(log_message)

    def start(self):
        self.sc.rtm_connect()

        while True:
            for rtm_message in self.sc.rtm_read():
                if "type" in rtm_message:
                    event_type = rtm_message.get("type")
                    for rule in self.rules:
                        if event_type not in rule.trigger:
                            continue

                        result, message = rule.validate(self.sc, rtm_message)
                        if result:
                            continue

                        log.info("'" + rule.__class__.__name__ +
                                 "' module capture '" +
                                 event_type + "' event and send message.")
                        self._notify(message)
