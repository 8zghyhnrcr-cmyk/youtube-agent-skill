"""Prepare a provider-neutral 10-second scene manifest and prompt, without API charges."""
import json
from pathlib import Path
from characters import load_characters
ROOT=Path(__file__).resolve().parent
def build_scene():
    data, images=load_characters(require_images=True)
    scene=json.loads((ROOT/"episodes"/"pilot_001_scene_01.json").read_text(encoding="utf-8"))
    for name in scene["characters"]:
        if name not in data["characters"]: raise ValueError("Unknown character: "+name)
    return {
        "scene":scene,
        "references":{name:str(images[name]) for name in scene["characters"]},
        "characters":{name:data["characters"][name] for name in scene["characters"]},
        "rules":data["rules"]
    }
if __name__=="__main__":
    result=build_scene()
    print(json.dumps(result,ensure_ascii=False,indent=2))
