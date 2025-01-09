class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        result = []
        for key, value in self.props.items():
            formatted_props = f' {key}="{value}"'
            result.append(formatted_props)

        return "".join(result)
    
    def to_html(self):
        raise NotImplementedError