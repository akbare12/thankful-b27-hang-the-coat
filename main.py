import os

# Deterministic, stdlib-only: writes the entry text to entry.txt.
TEXT = "Thank you. Your coat has carried the weight of every verdict you weighed today, heavy on your shoulders all day. I take it from you now, shake the dust from its shoulders, and hang it on the peg by the door. Stand a little taller without it. Tonight it rests there, empty sleeves still, waiting to keep you warm again tomorrow."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
