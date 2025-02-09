def get_node_style(node):
    """Return style attributes based on node type"""
    base_style = {
        'shape': 'circle',
        'style': 'filled',
        'fontname': 'Arial'
    }
    
    if node.__class__.__name__ == 'BSTreeNode':
        return {
            **base_style,
            'fillcolor': 'lightblue',
            'color': 'black'
        }
    elif node.__class__.__name__ == 'AVLNode':
        return {
            **base_style,
            'fillcolor': 'lightgreen',
            'color': 'black',
            'label': f'{node.value}\nh={node.height}'
        }
    elif node.__class__.__name__ == 'RBNode':
        return {
            **base_style,
            'fillcolor': 'red' if node.is_red else 'black',
            'fontcolor': 'white' if node.is_red else 'white'
        }
    return base_style
