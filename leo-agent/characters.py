"""Leo AI Agent character-reference loader (no paid API calls)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "characters.json"

def load_characters(require_images=True):
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    images = {name: ROOT / rel for name, rel in data["reference_images"].items()}
    missing = [str(path) for path in images.values() if not path.is_file()]
    if require_images and missing:
        raise FileNotFoundError("Missing reference images: " + ", ".join(missing))
    return data, images

def scene_character_prompt(name):
    data, images = load_characters()
    char = data["characters"][name]
    return {"character": name, "appearance": char["appearance"],
            "reference_image": str(images[name]),
            "rules": data["rules"]}

if __name__ == "__main__":
    data, images = load_characters(require_images=False)
    for name, path in images.items():
        print(f"{name}: {'READY' if path.is_file() else 'MISSING'} - {path}")
