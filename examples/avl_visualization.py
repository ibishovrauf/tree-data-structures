import random
import threading
import time

from src import AVLTree, visualization_worker


def insertion_worker(tree: AVLTree,
                     interval: float = 0.5) -> None:
    i = 0
    while True:
        value = random.randint(0, 500)
        tree.insert(value)
        time.sleep(interval)
        i += 1
        if i == 100:
            break

if __name__ == "__main__":
    bst = AVLTree()

    # Start the insertion worker thread.
    ins_thread = threading.Thread(target=insertion_worker,
                                  args=(bst, 1.5),
                                  daemon=True)
    ins_thread.start()

    visualization_worker(bst)
    ins_thread.join()
