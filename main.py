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
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    output_dir = os.path.dirname(output_dir) or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
