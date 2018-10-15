#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
from subprocess import check_output
import requests


EMAIL_ADDRESS, API_TOKEN = (
    check_output(
        ["security", "find-generic-password", "-s", "bitbar_zendesk_credentials", "-w"]
    )
    .decode("utf-8")
    .strip()
    .split(":")
)
DOMAIN = EMAIL_ADDRESS.split("@")[1].split(".")[0]
ZENDESK_URL = f"https://{DOMAIN}.zendesk.com"

response = requests.get(
    f"{ZENDESK_URL}/api/v2/search.json",
    params={"query": "status<solved "},
    auth=(f"{EMAIL_ADDRESS}/token", API_TOKEN),
)
response.raise_for_status()
results = response.json()["results"]

by_status = {}
for ticket in results:
    status = ticket["status"]
    if status in by_status:
        by_status[status].append(ticket)
    else:
        by_status[status] = [ticket]

print(f"{len(results)} | templateImage=iVBORw0KGgoAAAANSUhEUgAAADAAAABICAYAAACwc3YrAAAACXBIWXMAABYlAAAWJQFJUiTwAAACF0lEQVRoge2ai23CQAyG7S7QbFA2KCOwQdmgdIKyQekG6QRNN6AbZAS6QboBTODqpIt0QB5nO8iN5F86CYn47C/n8/kQSEQwZ93NOnoH+AdyAGs5gLUcwFoOYC0HsJYDWMsBrOUA1nIAa80eAMLPKl0DAFbha8Wo23nDZ8U8DQAUfXEOrcBR+W609kEnAFgTUe9cvQBEdACAX4XzWmHbahPj6NXYHqiEjk8K21bvRLQffaovt2LuFjEVuHm7u5iHuweqobjO5h59AGDJhLhyzgQ4DG1aNkAC0WQ4L9PVEwAcOcFnAySBbDqCaWK+L5LnFgCwZwKE4JeceNgAmZBFTAPuObCR+LvFSRxW45FpEyqOqGpNCoCIJQA8Mc2+iGgn9TkZACKG/fHKNPsBgK3G7yQAiBiq1CfTbLRNyJEaABEXwrZhRUSN1r8KABFDxQnH/T3T9GWsx8mVdgVKQcX5kFacLokBEDFUjmem2TcRqTbtpUQAseK8Mc1+4kk+qdgAseKUTLNjejEJGx8RK0RsEJGSUceXky9Bm5DbmaatRNrYlZnXyKy+SNLj5LbFdcccFcM+q7njAHCcXwGES47gYjR4oc8GEDo/SyGBfTt2KoCw+YSOU4CtAqARt9Ox4kxx6KwVtg8xjk71AijahFuo6I2T/A9PtnIAazmAtRzAWg5gLQewlgNYywGs5QDWcgBrOYC15g0AAH8NzSh9eF9GagAAAABJRU5ErkJggg==")
print("---")

for status, tickets in by_status.items():
    print(f"{status.capitalize()} ({len(tickets)})")
    for ticket in tickets:
        subject = ticket["subject"]
        address = ticket["via"]["source"].get("from", {}).get("address", "No email")
        url = f"{ZENDESK_URL}/agent/tickets/{ticket['id']}"
        print(f"{subject} - {address} | length=30 href={url}")

    print("---")

print(f"Open ZenDesk | href={ZENDESK_URL}/agent/")
print("Refresh tickets | refresh=true")
