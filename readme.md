SlackCop
==========

SlackCop is bot to manage/monitor user and channel setting by unique team rule. SlackCop is written in python. 

SlackCop provide bot based team management architecture to user. Especially, It is for the user using the Slack under unique team rules.

For example, you should set...
* _"two factor authentication"_
* _"firstname and lastname"_
* _"channel purpose."_ etc...

Administrator and Owner is tired to monitor user/channel setting. 
SlackCop monitor user/channel setting on behalf of Administrator and Owner.


Setup
----------

*Please set up python 3.x environment in advance. Recommended using virtualenv.*

1. Execute following command.
    * $ git clone https://github.com/Subarunari/SlackCop.git
    * $ cd SlackCop
    * $ pip install -r requirements.txt
2. Setup configuration file.
    * Setting slack token in slackcop/conf/slack.yml
    * Setting Unique Team Rule in slackcop/conf/rule.yml
3. $ python slackcop.py &


Add Unique Team Rule Class
----------


ToDo
----------
- [ ] Create Setup.py
- [ ] Write UnitTest
- [ ] Complete Readme.md 
- [ ] Async Process


Environment
----------
* Python 3.4.2


Dependencies
----------

* [python-slackclient](https://pypi.python.org/pypi/slackclient)
* [logbook](https://github.com/getlogbook/logbook)
