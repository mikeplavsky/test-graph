`users.py`: 
 * `nextLink` in `init_read` can be not empty multiple times w/o any data returned. 
 * when `patch_all` called in `while True`, it can happen that `init_read` does not stop for a long time.
