import argparse
import threading
import time

from src import AVLTree, visualization_worker, read_values_from_file


def insertion_worker(tree: AVLTree,
                     values: list,
                     interval: float = 0.5) -> None:
    """
    Inserts each value from the provided list into the AVL tree
    with a delay specified by interval.
    """
    for value in values:
        tree.insert(value)
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AVL Tree Insertion and Visualization")
    parser.add_argument("-f", "--file", required=True,
                        help="File name containing integer values")
    parser.add_argument("-i", "--interval", type=float, default=1.5,
                        help="Interval between insertions in seconds (default: 1.5)")
    args = parser.parse_args()

    values = read_values_from_file(args.file)
    bst = AVLTree()

    # Start the insertion worker thread.
    ins_thread = threading.Thread(target=insertion_worker,
                                  args=(bst, values, 1.5),
                                  daemon=True)
    ins_thread.start()

    visualization_worker(bst)
    ins_thread.join()
