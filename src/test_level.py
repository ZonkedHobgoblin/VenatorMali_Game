from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[1]
level_path = BASE_DIR / "assets" / "levels" / "level1.json"

with open(level_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Map size:", data["width"], data["height"])
print("Tile size:", data["tilewidth"], data["tileheight"])

print("\nTilesets:")
for tileset in data["tilesets"]:
    print(tileset)

print("\nLayers:")
for layer in data["layers"]:
    print(layer["name"], layer["type"], "visible:", layer.get("visible"))
    if "data" in layer:
        print("first 20 tiles:", layer["data"][:20])