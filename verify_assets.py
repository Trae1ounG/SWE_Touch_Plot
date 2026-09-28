from pathlib import Path
import hashlib, json, struct
root = Path(__file__).resolve().parent
for name, expected in json.loads((root / "assets.sha256.json").read_text()).items():
    data = (root / name).read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", name
    assert hashlib.sha256(data).hexdigest() == expected, name
    width, height = struct.unpack(">II", data[16:24])
    print(f"OK {name}: {width} x {height}")
