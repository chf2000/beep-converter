import sys
import os
import re

delay_scale = 1

if len(sys.argv) == 1:
    os.exit(-1)
for item in sys.argv[1:]:
    with open(item, "r") as f:
    # with open("die-gedanken-sind-frei.sh", "r") as f:
        content = f.read()
    result = ''
    content = re.sub(r"\\\n-n", "\nbeep", content)
    raw_unit = content.split('\n')
    unit = []
    for u in raw_unit:
        if u.startswith("beep"):
            unit.append(u.strip())
    for u in unit:
        duration = None
        pitch = None
        delay_each = None
        delay_once = None
        repeat_time = 1
        beep_argv = re.split('[\t \n]+',u)
        if len(beep_argv) == 1:
            continue
        for a in beep_argv[1:]:
            if a.startswith("-l"):
                duration = float(a[2:])
            elif a.startswith("-f"):
                pitch = float(a[2:])
            elif a.startswith("-D"):
                delay_each = float(a[2:])
            elif a.startswith("-d"):
                delay_once = float(a[2:])
            elif a.startswith("-r"):
                repeat_time = int(a[2:])
            else:
                print(f"Warning: cannot parse beep arg:{a}")
        for time in range(repeat_time):
            result += f"/usr/local/bin/beep -p {pitch} {duration/10}\n"
            if delay_each is not None and delay_each != 0:
                result += f"sleep {delay_each * delay_scale / 1000}\n"
        if delay_once is not None and delay_once != 0:
            result += f"sleep {delay_once * delay_scale / 1000}\n"

    print(result)
    os.system(result)
