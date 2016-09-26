from abc import ABCMeta, abstractmethod


class CustomRule(metaclass=ABCMeta):
    def __init__(self, conf):
        self.conf = conf

    @abstractmethod
    def validate(self, slack_client, event_message):
        '''
        Please define the custom validation rule.
        return "validation result", "post message"
        post message is defined based on slack api argument.
        https://api.slack.com/methods/chat.postMessage
        '''
        raise NotImplementedError()
