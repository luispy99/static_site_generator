import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from textnode import TextNode, TextType
from htmlnode import LeafNode

#def main():
#    test = TextNode("esto es el texto", "italic", "https:el_internet.com")
#    print(test)

# converts string to nodes
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, None, {"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", None, None, {"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception("unvalid text type")

#main()
