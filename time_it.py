import time
import random

def time_waste():

    print("Starting a time-waster.")

    random_time = random.randint(2, 20)
    time.sleep(random_time)

    print(f"Done. This took {random_time} seconds.")

time_waste()


