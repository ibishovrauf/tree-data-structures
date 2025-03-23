import random
import threading
import time

from src import BinarySearchTree, visualization_worker


def insertion_worker(tree: BinarySearchTree,
                     interval: float = 0.5) -> None:
    while True:
        value = random.randint(0, 10)
        tree.insert(value)
        print(f"Inserted {value}")
        time.sleep(interval)


if __name__ == "__main__":
    bst = BinarySearchTree()

    # Start the insertion worker thread.
    ins_thread = threading.Thread(target=insertion_worker,
                                  args=(bst, 1.5),
                                  daemon=True)
    ins_thread.start()

    visualization_worker(bst)
    ins_thread.join()
