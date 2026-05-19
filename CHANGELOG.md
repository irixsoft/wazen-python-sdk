# Changelog

## 0.4.0

- API now returns `sender_lid`, `from_phone_number`, `from_display_name` on inbound messages — these surface automatically in the returned dict (no SDK code change required to read them)
- `from_phone_number` is the actual sender phone number resolved from the Baileys v7 LID identifier (`*@lid`) seen in `from_jid`
- For group messages, `sender_lid` and `from_phone_number` identify the individual participant (`from_jid` remains the group JID)

## 0.3.0

- API now returns `mime_type`, `file_size`, `file_name` on inbound media messages — these surface automatically in the returned dict (no SDK code change required to read them)
- Add `messages.get_media(session_id, message_id)` and async equivalent, returning raw media bytes

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
