class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        final_string = ""
        for key, value in self.props.items():
            final_string += f"{key}=\"{value} "
        final_string = final_string[:-1]
        return final_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError
        
        if not self.tag:
            return f"{self.value}"
        
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
