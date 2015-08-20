import praw

r = praw.Reddit(user_agent = "save-to-subreddit")
username = raw_input(">>Username:")
password = raw_input(">>Password:")
subreddit = raw_input(">>Subreddit (without /r/)")

r.login(username,password)

for post in r.user.get_saved():

    post_name = str(post)

    try:
        semi = post_name.index(':')
        post_name = post_name[semi+2:]
    except Exception, CannotFind:
        pass

    sub = str(post.subreddit.display_name)
    package = '[' + sub + ']' + ' ' + post_name
    link = post.permalink
    print package
    r.submit(subreddit, package, url = link)
    post.unsave()

