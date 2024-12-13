from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes.text:
        raise Exception("empty node")

    if text_type not in TextType:
        raise Exception("invalid Markdown syntax")

    node_list = old_nodes.text.split(delimiter, 2)

    if len(node_list) == 1:
        return [old_nodes]
    
    node_list[0] = TextNode(node_list[0], TextType.NORMAL)
    node_list[2] = TextNode(node_list[2], TextType.NORMAL)

    node_list[1] = TextNode(node_list[1], text_type)

    return node_list
