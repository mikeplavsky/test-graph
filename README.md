Get Service Principle:
```
az ad sp create-for-rbac --skip-assignment true
```

Set up environment:
```
export AAD_TENANT=...
export CLIENT_ID=...
export CLIENT_SECRET=...
```

[users.py](./users.py): 
 * `nextLink` in `init_read` can be not empty multiple times w/o any data returned. 
 * when `while True: patch_all`, it can happen that `init_read` does not stop for a long time.
 * when `while True: patch_all`, it can happen that `delta_read` does not stop.
