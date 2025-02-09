from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx

from src import BinarySearchTree, BSTreeNode


def add_edges(node: Optional[BSTreeNode], G: nx.DiGraph) -> None:
    """
    Recursively add edges from the node to its children.
    """
    G.add_node(node.value)
    if node is None:
        return
    if node.left:
        G.add_edge(node.value, node.left.value)
        add_edges(node.left, G)
    if node.right:
        G.add_edge(node.value, node.right.value)
        add_edges(node.right, G)


def hierarchy_pos(G,
                  root,
                  width=1.0,
                  vert_gap=0.2,
                  vert_loc=0,
                  xcenter=0.5,
                  pos=None,
                  parent=None):
    """
    Compute a hierarchical layout for a tree graph G with root.
    This function is adapted from various online recipes.
    """
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if parent is not None:
        if parent in children:
            children.remove(parent)
    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = hierarchy_pos(G,
                                child,
                                width=dx,
                                vert_gap=vert_gap,
                                vert_loc=vert_loc - vert_gap,
                                xcenter=nextx,
                                pos=pos,
                                parent=root)
    return pos

def visualize_tree(snapshot: Optional[BSTreeNode]) -> None:
    """
    Visualize the tree snapshot using networkx and matplotlib.
    """
    plt.clf()  # Clear the current figure
    if snapshot is None:
        plt.text(0.5, 0.5, "Empty Tree", horizontalalignment='center',
                 verticalalignment='center', fontsize=12)
        plt.draw()
        return

    # Create a directed graph representing the tree.
    G = nx.DiGraph()
    add_edges(snapshot, G)
    pos = hierarchy_pos(G, snapshot.value)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue",
            arrows=True, font_size=10)
    plt.draw()


def visualization_worker(tree: BinarySearchTree,
                         refresh_interval: float = 1.0) -> None:
    """
    Worker that periodically fetches a snapshot of the tree and updates the visualization.
    """
    # Turn on interactive mode
    plt.ion()
    fig = plt.figure()
    while True:
        snapshot = tree.get_snapshot()
        visualize_tree(snapshot)
        plt.pause(refresh_interval)
