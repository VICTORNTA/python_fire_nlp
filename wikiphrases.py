#!/usr/bin/env  python
import fire
from nlplogic.corenlp import get_phrase_blob

if __name__ == "__main__":
    fire.Fire(get_phrase_blob)
