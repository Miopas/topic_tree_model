#!/usr/bin/env python3
#coding=utf8

import resource_loader as loader
import json
import re

def get_nlu_result(query):
    query = re.sub('\'', '\"', query)
    return json.loads(query)


if __name__ == '__main__':
    
    # load xml 
    topic_tree = loader.load_tree('flight.xml')

    session = {'system_actions':[] }
    nlu_result = None
    is_dialog_end = False

    print('system output > Hello')
    while (not is_dialog_end):
        query = input('Enter your input > ')
        nlu_result = get_nlu_result(query)
        is_dialog_end, reply = topic_tree.process(session, nlu_result)
        print('system output > %s' % reply)
