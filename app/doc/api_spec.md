# Message Queue API

```text
GET /healthy
// Health check.
200 (empty body)
```

```text
GET /
// List all channels.
200 {"channels": ["whales", "dolphins"]}
```

```text
POST /channels/<channel>
// Append a string message; create the channel if it doesn't exist.
Body: {"message": "Hello!"}
200 {}
```

```text
GET /channels/<channel>?offset=0&limit=20
// Read messages oldest first; skip offset messages and return up to limit.
// Defaults: offset=0, limit=20. Unknown channel or empty page: {"messages": []}.
200 {"messages": ["Hello!"]}
```
