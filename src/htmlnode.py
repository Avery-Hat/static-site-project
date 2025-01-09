class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    
    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method.")

    def props_to_html(self):
        if self.props is None:
            return ""
        
        result = []
        for key, value in self.props.items():
            formatted_props = f' {key}="{value}"'
            result.append(formatted_props)

        return "".join(result)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value is None: #raising error if value is none
            raise ValueError("All LeafNodes must have a value!")
        if self.tag is None: #returning raw value if tag is none
            return self.value

        props_string = self.props_to_html() #constructing HTML string
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
