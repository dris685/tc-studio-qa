import sys
sys.path.append('/Users/silviaho/Documents/tc-studio-qa/')
# import os
# sys.path.append(os.environ['WORKSPACE'])
import configparser

config = configparser.RawConfigParser()
config.read('./Configuration/config.ini')


class ReadConfig:
    @staticmethod
    def getBase_URL():
        base_URL = config.get('common info', 'base_URL')
        return base_URL
