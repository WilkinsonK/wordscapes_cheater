import itertools, os, sys
from concurrent.futures import ThreadPoolExecutor

import httpx

MAX_THREAD_COUNT    = 64
URL_DICTIONARY_ROOT = "https://api.dictionaryapi.dev/api/v2/entries/en"


def usage():
    print(f"{os.path.basename(__file__)} <CHARS> <N>",
          "Finds all words of N length associated with the given characters.",
          sep="\n")


def word_exists(word: str) -> bool:
    resp = httpx.get(f"{URL_DICTIONARY_ROOT}/{word.lower()}")

    status = resp.status_code
    if status in range(400,500) and status != 404:
        print(f"Request failed with status: {status}")
        quit(-1)

    return status == 200


def print_if_word_exists(word: str):
    if not word_exists(word):
        return
    print(word)


def main():
    if len(sys.argv) < 3:
        usage()
        return -1

    perms = itertools.permutations(sys.argv[1], int(sys.argv[2]))
    perms = set(["".join(i) for i in perms])

    with ThreadPoolExecutor(MAX_THREAD_COUNT) as pool:
        pool.map(print_if_word_exists, perms)

    return 0


if __name__ == "__main__":
    exit(main())
