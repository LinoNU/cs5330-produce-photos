"""Convert iPhone HEIC photos to metadata-free JPEGs for the public dataset repo.

For each ``.heic`` / ``.heif`` file in the input folder, this script:

1. opens it with pillow-heif,
2. bakes the camera orientation into the pixels (``ImageOps.exif_transpose``),
3. converts colors from the embedded profile (e.g. iPhone Display P3) to sRGB,
4. shrinks it so the longest side is at most ``--max-side`` pixels (default 1600),
5. saves it as an RGB JPEG (quality 90) with no EXIF, GPS, XMP, ICC or comments.

The image is rebuilt from raw pixels before saving, so no metadata from the
original file can carry over.

Usage:
    python scripts/convert_heic.py INPUT_DIR OUTPUT_DIR [--max-side 1600] [--quality 90]

Requires: pip install pillow pillow-heif
"""

from __future__ import annotations

import argparse
import io
from pathlib import Path

from PIL import Image, ImageCms, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()

HEIC_SUFFIXES = {".heic", ".heif"}
SRGB_PROFILE = ImageCms.createProfile("sRGB")


def to_srgb(image: Image.Image) -> Image.Image:
    """Return an RGB copy of ``image`` with colors converted to sRGB.

    Once the ICC profile is stripped, viewers assume sRGB, so converting first
    keeps colors (especially iPhone Display P3 reds) looking right.
    """
    icc = image.info.get("icc_profile")
    image = image.convert("RGB")
    if icc:
        source = ImageCms.ImageCmsProfile(io.BytesIO(icc))
        image = ImageCms.profileToProfile(image, source, SRGB_PROFILE, outputMode="RGB")
    return image


def strip_metadata(image: Image.Image) -> Image.Image:
    """Return a new image with the same pixels and an empty ``info`` dict."""
    clean = Image.new(image.mode, image.size)
    clean.paste(image)
    return clean


def convert_file(src: Path, dst: Path, max_side: int, quality: int) -> tuple[int, int]:
    """Convert one HEIC file to a metadata-free JPEG and return its final size."""
    with Image.open(src) as original:
        image = ImageOps.exif_transpose(original)
        image = to_srgb(image)
    image.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
    image = strip_metadata(image)
    dst.parent.mkdir(parents=True, exist_ok=True)
    image.save(dst, "JPEG", quality=quality, optimize=True)
    return image.size


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input_dir", type=Path, help="Folder containing .heic files")
    parser.add_argument("output_dir", type=Path, help="Folder to write .jpg files to")
    parser.add_argument("--max-side", type=int, default=1600, help="Longest side in pixels (default: 1600)")
    parser.add_argument("--quality", type=int, default=90, help="JPEG quality (default: 90)")
    args = parser.parse_args()

    sources = sorted(p for p in args.input_dir.iterdir() if p.suffix.lower() in HEIC_SUFFIXES)
    if not sources:
        raise SystemExit(f"No HEIC files found in {args.input_dir}")

    for src in sources:
        dst = args.output_dir / f"{src.stem}.jpg"
        width, height = convert_file(src, dst, args.max_side, args.quality)
        print(f"{src.name} -> {dst} ({width}x{height})")


if __name__ == "__main__":
    main()
