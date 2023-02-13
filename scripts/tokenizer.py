#!/usr/bin/env python3
"""Tokenize Ukrainian text using Stanza.

Usage:
    tokenizer.py < input.txt > output.tok

Example:
    $ echo 'Привіт, світе!' | ./tokenizer.py
    Привіт , світе !
"""

import fileinput
import stanza


def tokenize(text: str) -> [str]:
    if not hasattr(tokenize, "nlp"):
        tokenize.nlp = stanza.Pipeline(
            lang="uk",
            processors="tokenize",
            download_method=stanza.DownloadMethod.REUSE_RESOURCES,
        )
    nlp = tokenize.nlp

    tokenized = " ".join([t.text for t in nlp(text).iter_tokens()])
    return tokenized


def main():
    for line in fileinput.input():
        line = line.strip("\n")
        print(tokenize(line))


if __name__ == "__main__":
    main()
