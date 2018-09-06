import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="redditmirror",
    version="1.0.0",
    author="Sam McCreery",
    author_email="4602020+mccreery@users.noreply.github.com",
    description="Takes posts from your Reddit saved tab and x-posts them to a subreddit of your choice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/mccreery/reddit-mirror",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires="praw>=6.0"
)
