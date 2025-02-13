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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be missing!")
        
        if self.children is None:
            raise ValueError("children cannot be missing!")
        
        children_html = ""
        
        for child in self.children:
            if not hasattr(child, 'to_html'):
                raise ValueError("All children must have a 'to_html' method!")

        children_html = ""
        for child in self.children:
            # Call the child's to_html method
            children_html += child.to_html()
        
        html = f"<{self.tag}>{children_html}</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"