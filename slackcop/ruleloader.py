# coding: utf-8

import os
import glob
import importlib
import inspect

from slackcop import log
from slackcop.customrule import CustomRule


class RuleLoader():
    def __init__(self, rule_conf):
        dirpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rule")
        module_file_name_rule = os.path.join(dirpath, "*.py")
        init_file_path = os.path.join(dirpath, "__init__.py")

        self.rule_conf = rule_conf
        self.rule_list = glob.glob(module_file_name_rule)
        self.rule_list.remove(init_file_path)

    def load_module(self):
        rule_instance_list = list()

        for rule in self.rule_list:
            module = os.path.splitext(rule.split(os.sep)[-1])[0]
            if self.rule_conf.get(module) is None:
                log.error("No setting '" + module + "' in rule.yml")
                continue

            customrule = importlib.import_module("slackcop.rule." + module)
            rule_classes = inspect.getmembers(
                    customrule,
                    predicate=(lambda x: inspect.isclass(x)
                               and issubclass(x, CustomRule)
                               and not (x.__name__ == CustomRule.__name__))
                    )

            for rule_class in list(set(rule_classes)):
                rule_instance_list.append(rule_class[1](self.rule_conf[module]))
                log.info("Success loading '" + module + "' module.")

        return rule_instance_list
