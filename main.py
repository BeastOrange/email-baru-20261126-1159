import os
from pathlib import Path

SENTENCE: str = (
    "I insisted on an open-concept floor plan, and now my shower makes "
    "unbroken eye contact with the mail carrier."
)


def main() -> None:
    raw_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_path = Path(raw_path)

    if (
        output_path.is_dir()
        or raw_path.endswith(("/", "\\"))
        or (not output_path.suffix and output_path.name != "entry.txt")
    ):
        output_path = output_path / "entry.txt"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = SENTENCE if SENTENCE.endswith("\n") else f"{SENTENCE}\n"
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
