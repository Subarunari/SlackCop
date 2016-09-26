import sys

from slackcop import log
from slackcop.botcore import BotCore
from slackcop.confparser import ConfigYamlParser
from slackcop.ruleloader import RuleLoader


def main():
    config_parser = ConfigYamlParser()
    slack_token = config_parser.get_slack_token()
    rule_conf = config_parser.get_rule()

    rule_loader = RuleLoader(rule_conf)
    rule_instance_list = rule_loader.load_module()

    bot = BotCore(slack_token, rule_instance_list)

    try:
        log.info("Starting Slackcop.")
        bot.start()
    except KeyboardInterrupt:
        log.info("Terminating Slackcop.")
        sys.exit()


if __name__ == '__main__':
    log.setup()
    main()
