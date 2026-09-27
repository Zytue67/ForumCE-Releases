#!/usr/bin/env python3
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("version", help="Release version, e.g. 1.0.1")
    ap.add_argument("--calculator-bin", required=True, help="Path to ForumCE-Calculator/bin")
    ap.add_argument("--dmg", help="Optional ForumCE Connect DMG path")
    ap.add_argument("--notes", default="ForumCE update")
    args = ap.parse_args()

    release = ROOT / "release" / "latest"
    if release.exists():
        shutil.rmtree(release)
    release.mkdir(parents=True)

    calc_bin = Path(args.calculator_bin)
    names = ["FORUMCE.8xp", "FORUMCE.8xp.0.8xv", "FORUMCE.8xp.1.8xv"]
    assets = []
    for name in names:
        src = calc_bin / name
        if not src.exists():
            raise SystemExit(f"Missing calculator file: {src}")
        dst = release / name
        shutil.copy2(src, dst)
        assets.append({"name": name, "sha256": sha256(dst), "size": dst.stat().st_size})

    manifest = {
        "schema": 1,
        "product": "ForumCE",
        "calculator_version": args.version,
        "connect_version": args.version,
        "minimum_connect_version": "1.0.0",
        "notes": args.notes,
        "calculator_files": assets,
    }

    if args.dmg:
        src = Path(args.dmg)
        if not src.exists():
            raise SystemExit(f"Missing DMG: {src}")
        dst = release / src.name
        shutil.copy2(src, dst)
        manifest["connect_dmg"] = {
            "name": dst.name,
            "sha256": sha256(dst),
            "size": dst.stat().st_size,
        }

    (release / "forumce-release.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Prepared ForumCE {args.version} in {release}")
    for p in sorted(release.iterdir()):
        print(" -", p.name)


if __name__ == "__main__":
    main()
