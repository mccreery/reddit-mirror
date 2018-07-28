#!/usr/bin/env python3

import praw, datetime
reddit = praw.Reddit(user_agent="save-to-subreddit")

def yn(message):
    while True:
        answer = input(message + " (y/n): ")
        if answer.lower() in ("y", "yes"):
            return True
        elif answer.lower() in ("n", "no"):
            return False

def format_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

def sub_exists(sub):
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except:
        return False
    return True

def get_subreddit():
    subreddit = None

    while not subreddit:
        subreddit = input("Subreddit (leave blank to mimic username): ")

        if not subreddit:
            username = reddit.user.me()

            if sub_exists(username):
                print("Found username mimic sub r/{}".format(username))
                subreddit = username
            elif yn("Create private subreddit r/{} (warning: subreddits cannot be deleted)".format(username)):
                subreddit = reddit.subreddit.create(username, subreddit_type="private")
        elif not sub_exists(subreddit):
            print("Could not find subreddit r/{}".format(subreddit))
            subreddit = None

    return subreddit

if __name__ == "__main__":
    subreddit = get_subreddit()
    delete_saved = yn("Unsave mirrored posts")
    print("Finding saved posts...")

    posts = sorted(reddit.user.me().saved(limit=None), key=lambda post: post.created)

    if posts:
        print("Found {} saved posts between {} and {}".format(
            len(posts),
            format_timestamp(posts[0].created),
            format_timestamp(posts[-1].created)))

        if yn("Mirror posts"):
            print("Mirroring saved posts to r/{}...".format(subreddit))

            for post in posts:
                post.crosspost(subreddit)
                if delete_saved: post.unsave()
    else:
        print("No saved posts found")
