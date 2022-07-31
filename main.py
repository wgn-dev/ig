import os
key = "IG_USERNAME"
value = os.getenv(key)
while True:
    os.system(f"python3 qlizz.py {value}")

