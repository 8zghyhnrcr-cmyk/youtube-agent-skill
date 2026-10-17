# Leo AI Agent — Character References

This development branch adds the four fixed character definitions and a Python loader.

## Add reference PNGs
Place the four images at:
- `assets/characters/leo.png`
- `assets/characters/mia.png`
- `assets/characters/pofuduk.png`
- `assets/characters/mavis.png`

These binary images are **not yet committed**; the source reference sheet was provided in ChatGPT. Upload the approved crops before rendering. The loader fails safely when files are absent.

## Run
```bash
cd leo-agent
python3 characters.py
```

`load_characters()` validates that all four images exist. `scene_character_prompt("leo")` returns the appearance, reference image path and preservation rules for a provider adapter.

No paid API is invoked. Every paid generation must be approved separately.
