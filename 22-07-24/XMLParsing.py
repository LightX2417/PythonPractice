# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # Initialize the attribute count
    attr_count = 0
    # Use a queue for breadth-first traversal
    nodes = [node]

    while nodes:
        current_node = nodes.pop(0)
        # Add the number of attributes of the current node to the count
        attr_count += len(current_node.attrib)
        # Add all child elements of the current node to the queue
        nodes.extend(list(current_node))

    return attr_count


if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
