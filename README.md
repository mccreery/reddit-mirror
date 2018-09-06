# Reddit Mirror
Python module that takes links from your "saved" and x-posts them to a subreddit of your choice.

The best way to install is using `pip`:
```
pip install redditmirror
```

For the script to know your authentication details you need to create a `praw.ini` file, see [here](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

## Running
There are a few command line arguments which can be used to skip the prompts and even run in non-interactive mode. You can use `-h` or `--help` to get help.

### Examples:
```bash
python -m redditmirror -a          # run in automatic mode; tries to create a private subreddit
                                   # called r/username if it does not exist
```
```bash
python -m redditmirror -as example # use subreddit r/example instead of r/username
```
```bash
python -m redditmirror -kn         # 'k'eep saved posts, reprompt instead of creating new subreddit
```
```bash
python -m redditmirror -an         # crash and burn if r/username does not exist
```
