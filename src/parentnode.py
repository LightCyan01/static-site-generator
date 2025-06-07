from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        
        if self.tag is None:
            raise ValueError("Parentnode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        attributes = self.props_to_html()
        
        html = f"<{self.tag}{attributes}>"
        
        for child in self.children:
            html += child.to_html()
            
        html += f"</{self.tag}>"
        return html
    