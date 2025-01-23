class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    # converts the prop to a single string
    def props_to_html(self):
        final_string = ""
        for key, value in self.props.items():
            final_string += f"{key}=\"{value}\" "
        final_string = final_string[:-1]
        return final_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        super().__init__(tag, value, None, props)

    # converts node to string
    def to_html(self):
        if not self.value:
            raise ValueError("must have a value")
        
        if not self.tag:
            return f"{self.value}"
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        super().__init__(tag, None, children, props)
    
    # put all children in a string
    def to_html(self):
        if not self.tag:
            raise ValueError("must have a tag")
        
        if not self.children:
            raise ValueError("must have children")
        
        html_string = ""
        for kid in self.children:
            html_string += kid.to_html()
        
        return f"<{self.tag}>{html_string}</{self.tag}>"
