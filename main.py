"""Write one absurd terms-of-service clause to the entry file.

Pure Python standard library only.
"""

import os

ENTRY = (
    "Upon termination, the user's soul shall be returned in substantially "
    "its original condition, less reasonable wear and tear, within thirty "
    "(30) business days of notice, postage prepaid by the user."
)


def main() -> None:
    # MAKEFUN_OUTPUT_DIR names the writable output DIRECTORY; older
    # callers may pass a full ".../entry.txt" file path instead, so
    # normalize both shapes to a directory before joining the filename.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out.endswith(".txt"):
        out = os.path.dirname(out) or "."
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
