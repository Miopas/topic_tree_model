import xml.etree.ElementTree as ET
import logging
import re
import pdb

logging.basicConfig()
logger = logging.getLogger('TreeManager')

class TreeManager(object):
    def __init__(self, xml_file):
        self.topic_tree = ET.parse(xml_file)
        self.focus = ''

    def process(self, session, nlu_result): 
        logger.debug('run fill_tree')
        self.fill_tree(session, nlu_result)

        logger.debug('run find_next_focus')
        next_focus_node, action = self.find_next_focus()

        if next_focus_node != None:
            session['system_actions'].append({'node':self.get_name(next_focus_node), 'action':action})
            return False, self.get_reply(next_focus_node, action) 
        else:
            return True, 'END'

    def fill_tree(self, session, nlu_result): 
        '''Fill empty nodes using nlu_result
        nlu_result: a structured semantic representation in JSON format, such as: 
                    {'domain':'flight', 'intent':'book', 'slots':{'customer_name':'Jack', 'start_city':'Shanghai'} } 
        session: 
            {'system_actions':[{'node':'customer_name', 'action':'ack'}] }
        '''
        if session == None or nlu_result == None:
            return

        for (slot_name, slot_value) in nlu_result['slots'].items():
            #if slot_name == 'ack':
            #    for history_action in session['system_actions']:
            #        if history_action['action'] == 'ack':
            #            node = self.tree.findall('.//domain/intent/*[@name=\'%s\']' % (history_action['node']))
            #            if len(node) == 1 and node[0] != None:
            #                node[0].set('is_ack', 'True')

            slot_node = self.topic_tree.findall('.//domain/intent/*[@name=\'%s\']' % (slot_name))
            if len(slot_node) == 1 and slot_node[0] != None:
                #print(list(slot_node[0].iter()))
                slot_node[0].set('value', slot_value)         


    def find_next_focus(self):
        #pdb.set_trace()
        #for slot_node in self.topic_tree.findall('.//domain/intent/slot'):
        #    if self.is_filled(slot_node) and not self.is_ack(slot_node):
        #        return slot_node, 'ack'
        #     
        for slot_node in self.topic_tree.findall('.//domain/intent/slot'):
            if not self.is_filled(slot_node) and not self.is_optional(slot_node):
                return slot_node, 'request'

        return None, ''

    def is_filled(self, node):
        if node.get('value') != '' and node.get('value') != None:
            return True
        return False

    def is_optional(self, node):
        if node.get('optional') != '' and node.get('optional') != None \
                and node.get('optional') == 'True':
            return True
        return False

    def is_ack(self, node):
        if node.find('is_ack') != None:
            return True
        return False

    def get_reply(self, node, action):
        if node == None:
            logger.error('node empty')
            return None

        reply = node.find('./%s/text' % action).text
        reply = re.sub('%alias%', self.get_alias(node), reply)
        
        #reply = re.sub('%value%', self.get_value(node), reply)

        return reply

    def get_name(self, node):
        if node == None:
            logger.error('node empty')
            return None
        return node.get('name')

    def get_alias(self, node):
        if node == None:
            logger.error('node empty')
            return None
        return node.find('alias').text

    def get_value(self, node):
        if node == None:
            logger.error('node empty')
            return None
        #print(list(node.iter()))
        return node.get('value')

if __name__ == '__main__':
    tree = TreeManager('flight.xml')
    print(list(tree.topic_tree.iter()))
