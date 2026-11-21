import threading
import time

def download_file():
    print("Downloading file...")
    time.sleep(2)
    print("Download complete")

def process_data():
    print("Processing data...")
    time.sleep(1)
    print("Processing complete")

def save_results():
    print("Saving results...")
    time.sleep(1)
    print("Results saved")

# Create one thread for each task
threads = [
    threading.Thread(target=download_file),
    threading.Thread(target=process_data),
    threading.Thread(target=save_results)
]

# Start all tasks
for thread in threads:
    thread.start()

# Wait for all tasks to finish
for thread in threads:
    thread.join()

print("All tasks are complete")