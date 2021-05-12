import sys

'''
Example

## Table of contents
* [Introduction](#introduction)
* [Some paragraph](#some-paragraph)
    * [Sub paragraph](#sub-paragraph)
* [Another paragraph](#another-paragraph)
'''

MARKDOWN_FILE_PATH = sys.argv[1]
HASHTAG_START_NUM = "##"


with open(MARKDOWN_FILE_PATH, 'r') as file:
    markdown_file = file.readlines()


def parse_file(data):
    for line in data:
        # Gets titles that are not the first (one hashtag only)
        if line.startswith(HASHTAG_START_NUM):
            hashtag_count = line.count('#')
            title_start = hashtag_count + 1     # Hashtags + blank space
            title = line[title_start:].strip()  # Strip removes line break
            format_line(hashtag_count, title)


def format_line(hashtag_count, title):
    title_ref = title.replace(' ', '-').lower()
    indent = "    "
    print(indent * (hashtag_count - len(HASHTAG_START_NUM)) +
          f"* [{title}](#{title_ref})")


def main():
    parse_file(markdown_file)


main()
