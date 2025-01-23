from textnode import TextNode, TextType

# breaks a string into (max) 3 strings
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    parts = old_nodes.text.split(delimiter)

    for i, part in enumerate(parts):
        if i % 2 == 0:
            if part:
                node_list.append(TextNode(part, TextType.NORMAL))
        else:
            extracted_text = part.split(']', 1)
            if extracted_text[0]:
                node_list.append(TextNode(extracted_text[0], text_type))
            if len(extracted_text) > 1 and extracted_text[1]:
                node_list.append(TextNode(extracted_text[1], TextType.NORMAL))

    return node_list
