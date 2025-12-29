#!/usr/bin/env python3
"""
Move images referenced as /images/... in posts into their respective post folders
and update references to use a colocated relative path (./filename).

Usage:
  ./scripts/move_images_to_posts.py --dry-run
  ./scripts/move_images_to_posts.py --apply

By default the script performs a dry-run and prints planned moves.
Set --apply to actually move files and update content.
"""
import argparse
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_IMAGES = ROOT / "public" / "images"
POSTS_DIR = ROOT / "src" / "content" / "post"

IMG_PATTERN = re.compile(r"/images/[\w\-./%]+\.(?:png|jpe?g|gif|webp|avif|svg)", re.IGNORECASE)


def find_post_files():
    for p in POSTS_DIR.rglob("index.*"):
        if p.suffix.lower() in {".md", ".mdx"}:
            yield p


def extract_images(text):
    return set(m.group(0) for m in IMG_PATTERN.finditer(text))


def find_public_file(img_path):
    # img_path starts with /images/...
    rel = img_path.lstrip("/")  # images/...
    candidate = ROOT / rel
    if candidate.exists():
        return candidate
    # try inside public/images with subdirs
    candidate2 = PUBLIC_IMAGES / Path(rel).relative_to("images")
    if candidate2.exists():
        return candidate2
    # fallback: search by basename under public/images
    name = Path(rel).name
    for p in PUBLIC_IMAGES.rglob(name):
        return p
    return None


def safe_move(src: Path, dest_dir: Path, apply: bool):
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if dest.exists():
        # avoid overwrite by appending a suffix
        base = src.stem
        ext = src.suffix
        i = 1
        while True:
            candidate = dest_dir / f"{base}-{i}{ext}"
            if not candidate.exists():
                dest = candidate
                break
            i += 1
    if apply:
        shutil.move(str(src), str(dest))
    return dest


def process_file(path: Path, apply: bool):
    text = path.read_text(encoding="utf-8")
    images = extract_images(text)
    if not images:
        return []
    moves = []
    post_dir = path.parent
    for img in sorted(images):
        pub = find_public_file(img)
        if not pub:
            moves.append((img, None, None))
            continue
        dest = safe_move(pub, post_dir, apply)
        newref = f"./{dest.name}"
        if apply:
            text = text.replace(img, newref)
        moves.append((img, pub, dest))
    if apply and text:
        path.write_text(text, encoding="utf-8")
    return moves


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Actually move files and update content")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of posts to process (0 = all)")
    args = ap.parse_args()

    apply = args.apply
    planned = []
    for i, post in enumerate(find_post_files(), start=1):
        if args.limit and i > args.limit:
            break
        moves = process_file(post, apply=False)
        if moves:
            planned.append((post, moves))

    if not planned:
        print("No /images/... references found in posts.")
        return

    print("Planned moves (dry-run):")
    for post, moves in planned:
        print(f"\nPost: {post}")
        for img, pub, dest in moves:
            if pub is None:
                print(f"  MISSING: {img} (no file found under public/images)")
            else:
                print(f"  {pub} -> {post.parent}/(will be {pub.name})")

    if not apply:
        print("\nRun with --apply to perform these moves and update content.")
        return

    # Apply moves for real
    print("\nApplying moves...")
    for post, _ in planned:
        moves = process_file(post, apply=True)
        print(f"Updated: {post} ({len(moves)} image(s) processed)")

    print("Done.")


if __name__ == '__main__':
    main()
