from slackcop.customrule import CustomRule


class UserProfile(CustomRule):
    def __init__(self, conf):
        self.rule_name = "userprofile"
        self.trigger = ["team_join", "user_change", "presence_change"]
        self.conf = conf.get("required")

    def validate(self, slack_client, event_message):
        event_type = event_message.get("type")
        has2fa = self.conf.get("2fa")

        if event_type in ["team_join", "user_changes"]:
            result = event_message.get("user").get("has_2fa") is has2fa
            target_user = event_message.get("user").get("id")
        elif event_type in ["presence_change"]:
            if event_message.get("presence") == "active":
                target_user = event_message.get("user")
                response = slack_client.api_call("users.info", user=target_user)
                result = response.get("user").get("has_2fa") is has2fa
            else:
                return True, ""
        else:
            return True, ""

        message = {"channel": target_user, "attachments": '[{"pretext": "Please set two factor authentication.", "text":"<https://get.slack.help/hc/en-us/articles/204509068-Set-up-two-factor-authentication|two factor setting help document>"}]', }
        return result, message
