# Wazen Python SDK

Official Python SDK for the [Wazen WhatsApp API](https://wazen.dev).

[![PyPI](https://img.shields.io/pypi/v/wazen)](https://pypi.org/project/wazen)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=fff)](https://python.org)

## Installation

```bash
pip install wazen
```

## Quick Start

```python
from wazen import Wazen

wazen = Wazen("wz_your_api_key")

# Send a message
message = wazen.messages.send("session-id", to="+1234567890", type="text", content="Hello from Wazen!")

# List sessions
sessions = wazen.sessions.list()

# Check if a number is on WhatsApp
result = wazen.contacts.check("session-id", phone="+1234567890")
```

### Async Usage

```python
from wazen import AsyncWazen

wazen = AsyncWazen("wz_your_api_key")

message = await wazen.messages.send("session-id", to="+1234567890", type="text", content="Hello!")
```

## Resources

All resources are accessible as properties on the client instance.

### Sessions

```python
wazen.sessions.create()
wazen.sessions.list()
wazen.sessions.get("session-id")
wazen.sessions.delete("session-id")
wazen.sessions.restart("session-id")
wazen.sessions.get_qr("session-id")
wazen.sessions.factory_reset("session-id")
```

### Messages

```python
# Send text
wazen.messages.send("session-id", to="+1234567890", type="text", content="Hello!")

# Send image
wazen.messages.send("session-id", to="+1234567890", type="image", media_url="https://example.com/photo.jpg")

# Get message history
wazen.messages.list("session-id", direction="outgoing", limit=10)

# Get single message
wazen.messages.get("session-id", "message-id")
```

### Groups

```python
wazen.groups.list("session-id")
wazen.groups.create("session-id", subject="Team Chat", participants=["+1234567890"])
wazen.groups.get("session-id", "group-id")
wazen.groups.update("session-id", "group-id", subject="New Name")
wazen.groups.leave("session-id", "group-id")
wazen.groups.manage_participants("session-id", "group-id", action="add", participants=["+0987654321"])
wazen.groups.send_message("session-id", "group-id", type="text", content="Hello group!")
```

### Channels

```python
wazen.channels.create("session-id", name="Product Updates", description="Latest news")
wazen.channels.send_message("session-id", "channel-id", type="text", content="New release!")
```

### Contacts

```python
# Check single number
wazen.contacts.check("session-id", phone="+1234567890")

# Bulk check
wazen.contacts.bulk_check("session-id", phones=["+1234567890", "+0987654321"])
```

### Warming

```python
wazen.warming.start("session-id", contacts=[
    {"phone": "+1234567890", "name": "Alice"},
    {"phone": "+0987654321"},
])
wazen.warming.get_status("session-id")
wazen.warming.pause("session-id")
wazen.warming.resume("session-id")
wazen.warming.cancel("session-id")
```

### Webhooks

```python
wazen.webhooks.create(
    url="https://your-app.com/webhooks/wazen",
    events=["message.received", "message.delivered"],
)
wazen.webhooks.list()
wazen.webhooks.update("webhook-id", enabled=False)
wazen.webhooks.delete("webhook-id")
wazen.webhooks.test("webhook-id")
wazen.webhooks.get_logs("webhook-id")
```

### Account

```python
account = wazen.account.get()
usage = wazen.account.get_usage()
```

### API Keys

```python
key = wazen.api_keys.create(name="new-key")
wazen.api_keys.list()
wazen.api_keys.revoke("key-id")
```

## Configuration

```python
wazen = Wazen(
    "wz_your_api_key",
    base_url="https://wazen.dev/api/v1",  # default
    timeout=30,                            # default, in seconds
)
```

## Error Handling

```python
from wazen import Wazen, WazenApiError

try:
    wazen.messages.send("session-id", to="+1234567890", type="text", content="Hi")
except WazenApiError as e:
    print(e.status_code)  # HTTP status code
    print(e.error_code)   # API error code
    print(e.message)      # Error message
```

## Requirements

- Python 3.10 or later
- A Wazen account with an active subscription
- An API key from your [Dashboard](https://wazen.dev/dashboard/developers)

## Links

- [API Documentation](https://wazen.dev/docs)
- [Dashboard](https://wazen.dev/dashboard)
- [TypeScript SDK](https://www.npmjs.com/package/@wazen/sdk)
- [.NET SDK](https://www.nuget.org/packages/Wazen)

## License

MIT
