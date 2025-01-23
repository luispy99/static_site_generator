from textnode import TextType
from delimiter import split_nodes_delimiter

# split TextNode objects with NORMAL text type into smaller nodes
def split_nodes_image(old_nodes: list):
    new_nodes = []
    delimiter = "!["

    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            new_nodes.extend(split_nodes_delimiter(node, delimiter, TextType.IMAGE))
        else:
            new_nodes.append(node)
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    delimiter = "["

    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            new_nodes.extend(split_nodes_delimiter(node, delimiter, TextType.LINK))
        else:
            new_nodes.append(node)
    
    return new_nodes
