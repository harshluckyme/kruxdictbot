import subprocess
import time

while True:
    subprocess.run(["bash", "dictbot"], text=True, input="2 3")
    time.sleep(10)
