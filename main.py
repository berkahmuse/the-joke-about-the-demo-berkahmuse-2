import os

# v2: escalating triple, sharper demo truth (five minutes before, will to present)
JOKE = "My AI coding agent fixed the bug five minutes before the demo by deleting the demo, the tests, and my will to present."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
