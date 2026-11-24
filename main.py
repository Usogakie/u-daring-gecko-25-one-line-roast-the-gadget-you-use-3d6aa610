import os

LINE = "My phone sends me a screen-time report every Sunday like a disappointed parent, then hands me an 'Ignore limit' button that never says no \u2014 a bouncer who always lets me in."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
