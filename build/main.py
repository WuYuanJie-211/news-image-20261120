#!/usr/bin/env python3
"""THE WORLD IN ONE DAY -- Friday 20 November 2026.

Entrypoint for the news-image entry. The front page is rendered once,
by hand, from build/front.html into build/entry.png (1024x1024, under
1 MiB). This program does the only thing the competition run needs:
copy that pre-rendered image to /output/entry.png, after checking it
is a real PNG of the right size and dimensions.

No network, no randomness, no timestamps: running it twice writes
byte-identical output.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1024 * 1024  # competition cap: image <= 1 MiB
WANT_W, WANT_H = 1024, 1024


def png_size(path):
    """Return (width, height) read from the PNG IHDR chunk."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file: %s" % path)
    if head[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk: %s" % path)
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.exists(SRC):
        print("missing source image: %s" % SRC, file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print("entry.png too large: %d bytes > %d" % (size, MAX_BYTES),
              file=sys.stderr)
        return 1
    width, height = png_size(SRC)
    if (width, height) != (WANT_W, WANT_H):
        print("wrong dimensions: %dx%d, want %dx%d"
              % (width, height, WANT_W, WANT_H), file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Post-copy check: the output must be byte-identical to the source.
    # A silent short write or a stale /output would otherwise pass.
    if sha256(DST) != sha256(SRC):
        print("output mismatch after copy: %s != %s" % (DST, SRC),
              file=sys.stderr)
        return 1
    print("entry.png: %d bytes, %dx%d, sha256 %s"
          % (size, width, height, sha256(DST)))
    print("wrote %s" % DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
