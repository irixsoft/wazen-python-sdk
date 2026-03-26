# Changelog

## 0.2.0

- All features now available on all plans (removed Pro+ tier restrictions)
- Groups, Channels, and bulk contact validation no longer require Pro+ subscription
- Updated documentation to reflect universal feature access

## 0.1.0 (2026-03-26)

Initial release of the Wazen Python SDK.

### Features

- **Wazen** sync client and **AsyncWazen** async client
- **Sessions** - create, list, get, delete, restart, get_qr, factory_reset (7 methods)
- **Messages** - send, list, get (3 methods)
- **Contacts** - check, bulk_check (2 methods)
- **Groups** - list, create, get, update, leave, manage_participants, update_settings, send_message, get_invite, revoke_invite, get_requests, manage_requests, get_invite_info, join (14 methods)
- **Channels** - create, lookup, get, update, delete, send_message, list_messages, react, follow, unfollow, mute, unmute (12 methods)
- **Warming** - start, get_status, pause, resume, cancel (5 methods)
- **Webhooks** - create, list, update, delete, test, get_logs (6 methods)
- **Account** - get, get_usage (2 methods)
- **API Keys** - create, list, revoke (3 methods)
- **Error handling** with WazenApiError, WazenTimeoutError, WazenNetworkError
- Context manager support for both sync and async clients
- Python 3.10+ with full type annotations
- Single dependency: httpx
