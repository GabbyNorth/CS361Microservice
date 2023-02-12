# Gabby Narmontaite
# CS361 Assignment 8
# February 11, 2023

import string
import random
import time

print("\ngenerator running...")

while True:

    time.sleep(1)
    edt = open('generator-service.txt', 'r')

    if edt.read().isdigit():
        edt.seek(0)
        local_val = int(edt.read())

        counter = 0
        key = ''
        spaces = random.randint(0, 45)
        chars = string.ascii_letters + " " * spaces

        while counter < local_val:
            char = random.choice(chars)
            key += char
            counter += 1

        edt = open('generator-service.txt', 'w')
        edt.write("*" + key + "*")
        edt.flush()

        # console output
        print(f'\nWriting key of length {local_val}: \'{key}\'')
        print(f'\n\'{chars}\'')
        print(spaces)

        time.sleep(2)
        edt.truncate(0)

        edt.close()
