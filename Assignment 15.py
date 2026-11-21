import gc
import time
import tracemalloc

class Node:
    def __init__(self):
        self.other = None

def experiment(collection_enabled):
    gc.enable() if collection_enabled else gc.disable()
    gc.collect()  # Start each experiment with a clean slate
    tracemalloc.start()

    start = time.time()

    for _ in range(100_000):
        a = Node()
        b = Node()
        a.other = b
        b.other = a
        del a, b

    if not collection_enabled:
        before_manual = tracemalloc.get_traced_memory()[0]
        gc.collect()  # Manually collect the unused objects
        after_manual = tracemalloc.get_traced_memory()[0]
    else:
        before_manual = after_manual = 0

    elapsed = time.time() - start
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return elapsed, current_memory, peak_memory, before_manual, after_manual

for enabled in (True, False):
    elapsed, current, peak, before, after = experiment(enabled)
    print(f"\nGC {'enabled' if enabled else 'disabled'}")
    print(f"Time: {elapsed:.3f} seconds")
    print(f"Current traced memory: {current / 1024:.1f} KB")
    print(f"Peak traced memory: {peak / 1024:.1f} KB")
    if not enabled:
        print(f"Memory before manual collection: {before / 1024:.1f} KB")
        print(f"Memory after manual collection: {after / 1024:.1f} KB")

gc.enable()  # Leave garbage collection enabled