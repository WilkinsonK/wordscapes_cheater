# Wordscapes Cheater #

Cheating is no fun, but sometimes a game with no hints can get
irritating, increasingly, over time. When all hope, sanity or
patience is lost this ugly script gets the job done.

Given an array of characters from stdin and a word length, this
cheater will brute-force try all permutations of said characters
against a Web API that serves as a RESTful english dictionary.

# Usage #

Execution of this script is bare-minimum effort. You can view the
usage example by running the script as-is with no arguments:

```bash
$ python3 -m main
main.py <CHARS> <N>
Finds all words of N length associated with the given characters.
```
