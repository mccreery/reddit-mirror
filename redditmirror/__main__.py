#!/usr/bin/env python3

import praw, datetime, argparse, sys

def yn(message):
    while True:
        answer = input(message + " (y/n): ").lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False

def format_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

def get_subreddit(reddit, subreddit):
    try:
        return reddit.subreddits.search_by_name(subreddit, exact=True)[0]
    except:
        return None

def choose_subreddit(reddit, args):
    subreddit = None

    while not subreddit:
        name = None
        if "subreddit" in args:
            name = args.subreddit
        elif not args.auto:
            name = input("Subreddit (leave blank to mimic username): ")

        if not name:
            name = reddit.user.me()

        subreddit = get_subreddit(reddit, name)

        if not subreddit:
            print("Could not find subreddit r/{}".format(name), file=sys.stderr)

            if "no_create" in args:
                if args.auto:
                    sys.exit(1)
                elif "subreddit" in args:
                    del args.subreddit
            elif args.auto or yn("Create private subreddit r/{} (warning: subreddits cannot be deleted)".format(name)):
                subreddit = reddit.subreddit.create(name, subreddit_type="private")
                print("Created private subreddit r/{}".format(name))

    return subreddit

if __name__ == "__main__":
    reddit = praw.Reddit(user_agent="save-to-subreddit")

    parser = argparse.ArgumentParser(description="Mirror posts from \"saved\" to a subreddit using crossposts")
    parser.add_argument("-a", "--auto", action="store_true", help="do not prompt the user")

    parser.add_argument("-s", "--subreddit", "--sub", help="post to the given subreddit; r/username if omitted", default=argparse.SUPPRESS)
    parser.add_argument("-n", "--no-create", action="store_true", help="do not create a new subreddit; crash in auto mode", default=argparse.SUPPRESS)
    parser.add_argument("-k", "--keep", action="store_true", help="do not unsave posts in auto mode", default=argparse.SUPPRESS)

    args = parser.parse_args()
    subreddit = choose_subreddit(reddit, args)

    if args.auto:
        delete_saved = "keep" not in args
    else:
        delete_saved = yn("Unsave mirrored posts")
    print("Finding saved posts...")

    posts = reddit.user.me().saved(limit=None)
    posts = filter(lambda post: isinstance(post, praw.models.Submission), posts)
    posts = sorted(posts, key=lambda post: post.created)

    if posts:
        print("Found {} saved posts between {} and {}".format(
            len(posts),
            format_timestamp(posts[0].created),
            format_timestamp(posts[-1].created)))

        print("Mirroring saved posts to r/{}...".format(subreddit))

        for post in posts:
            post.crosspost(subreddit)
            if delete_saved: post.unsave()
    else:
        print("No saved posts found")
