#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes one single-line joke pickup line to /output/entry.txt and prints it.
"""

LINE = "Are you gradient descent? Because every step I take pulls me closer to you."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
