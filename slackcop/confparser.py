# coding: utf-8

import os
import yaml

from slackcop import log


class ConfigYamlParser():
    def __init__(self):
        dirpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "conf")
        self.slack_conf_file = os.path.join(dirpath, "slack.yml")
        self.rule_conf_file = os.path.join(dirpath, "rule.yml")

    def get_slack_token(self):
        self._check_conf_file_exists(self.slack_conf_file)
        with open(self.slack_conf_file) as fp:
            slack_conf = yaml.load(fp)
            token = slack_conf.get("bot").get("token")
            if token is None:
                log.critical("please setting slack token in " + self.slack_conf_file)

            return token

    def get_rule(self):
        self._check_conf_file_exists(self.rule_conf_file)
        with open(self.rule_conf_file) as fp:
            rule_conf = yaml.load(fp)
            return rule_conf

    def _check_conf_file_exists(self, file_path):
        if not os.path.exists(file_path):
            log.critical("Not found setting file. " + os.linesep + "please setting " + file_path)
