from slackcop.customrule import CustomRule


class UserProfile(CustomRule):
    def __init__(self, conf):
        self.rule_name = "userprofile"
        self.trigger = ["team_join", "user_change"]
        self.conf = conf.get("required")

    def validate(self, slack_client, event_message):
        has2fa = self.conf.get("2fa")
        result = event_message.get("user").get("has_2fa") is has2fa
        target_user = event_message.get("user").get("id")

        message = {"channel": target_user, "attachments": '[{"text": "Please set 2 factor authentication."}]'}
        return result, message
