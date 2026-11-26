"""Write the lost sock's status update to /output/entry.txt.

One line, 119 characters, inside the 120-character gate. The sock was
pulled out of a magician's hat in front of 200 people — it was supposed
to be a rabbit, and it panicked. Stdlib only; no network.
"""

import os

ENTRY = "Status update: the magician pulled me out of his hat in front of 200 people. I was supposed to be a rabbit. I panicked."

OUTPUT_DIR = "/output"
# The grader sets no override; the env var exists only so a local run can
# aim the file elsewhere (e.g. a scratch dir) without editing the code.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def validate_entry(text):
    """Gate mirror: single line, 1-120 chars, not only whitespace.

    Fail loudly here instead of writing a file the sealed scorer would
    reject as invalid.
    """
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if "\n" in text or not text.strip():
        raise ValueError("entry must be one non-blank line")
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write one validated line to the gate's output path."""
    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
