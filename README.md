# save-to-subreddit
Python script that takes links from you "saved" and posts them to a subreddit of your choice. Preferably a personal one.

## Dependencies
The script requires `python3` and [`praw`](https://praw.readthedocs.io/en/latest/getting_started/installation.html):

```
pip install praw
```

For the script to know your authentication details you need to create a `praw.ini` file, see [here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

## Running
There are a few command line arguments which can be used to skip the prompts and even run in non-interactive mode. You can use `-h` or `--help` to get help.

### Examples:
```bash
./RedditSaved.py -a          # run in automatic mode; tries to create a private subreddit
                             # called r/username if it does not exist
```
```bash
./RedditSaved.py -as example # use subreddit r/example instead of r/username
```
```bash
./RedditSaved.py -kn         # 'k'eep saved posts, reprompt instead of creating new subreddit
```
```bash
./RedditSaved.py -an         # crash and burn if r/username does not exist
```
