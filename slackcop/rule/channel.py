from slackcop.customrule import CustomRule


class Channel(CustomRule):
    def __init__(self, conf):
        self.rule_name = "channel"
        self.trigger = ["channel_created", "channel_rename"]
        self.conf = conf.get("required")

    def validate(self, slack_client, event_message):
        required_purpose = self.conf.get("purpose")
        required_topic = self.conf.get("topic")
        channel_id = event_message.get("channel").get("id")

        response = slack_client.api_call("channels.info", channel=channel_id)
        if not response.get("ok"):
            return True, ""

        channel_section = response.get("channel")
        topic = channel_section.get("topic").get("value")
        purpose = channel_section.get("purpose").get("value")

        if required_purpose:
            valid_purpose = len(purpose) > 0

        if required_topic:
            valid_topic = len(topic) > 0

        notify_target = channel_section.get("name")
        message = {"channel": notify_target, "text": "Please setting topic and purpose this channel: #" + notify_target}
        return bool(valid_purpose and valid_topic), message
