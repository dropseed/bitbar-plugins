#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
import subprocess

try:
    docker_output = subprocess.check_output(["/usr/local/bin/docker", "ps"], stderr=subprocess.STDOUT).decode("utf-8")
except subprocess.CalledProcessError:
    print("0* up")
    exit(0)

containers = []

# TODO group by common prefixes...

for line in docker_output.splitlines()[1:]:
    parts = line.split()
    container_name = parts[-1]
    container_id = parts[0]
    containers.append({"name": container_name, "id": container_id})

print(f"{len(containers)} up")

if containers:
    print("---")
    for container in containers:
        print(container["name"])
        print(f"-- Kill | color=red bash=/usr/local/bin/docker param1=kill param2={container['id']} refresh=true terminal=false")

    print("---")
    ids = " ".join([x["id"] for x in containers])
    print(
        f'Stop all | color=red bash=/bin/bash param1="-c" param2="/usr/local/bin/docker kill {ids}" refresh=true terminal=false'
    )
    print("Refresh | refresh=true")
else:
    print("---")
    print("Refresh | refresh=true")
