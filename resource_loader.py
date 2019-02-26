import topic_tree_manager as topic_tree

def load_tree(xml_file):
    return topic_tree.TreeManager(xml_file)

if __name__ == '__main__':
    load_tree('flight.xml')
