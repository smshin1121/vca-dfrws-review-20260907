"""Reassemble the complete review ZIP from the two byte-preserving ZIP parts."""

from __future__ import annotations

import hashlib
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Part:
    """Expected bytes, independently checked before assembly."""

    filename: str
    archive_sha256: str
    member: str
    payload_bytes: int
    payload_sha256: str


PARTS = (
    Part(
        "VCA_review_v5_part1.zip",
        "09c1bb67a27531661acb40f09cc4a160ef8b609127ad1bf04d26917ef63f3585",
        "archive_part_01.bin",
        83886080,
        "c01cead0fefb407437f976978b54dcd2b2f8822a18b4813a8171dc7bdf578af6",
    ),
    Part(
        "VCA_review_v5_part2.zip",
        "2d30ec5dbd7c4d63ce51705c31252be852080753daea048096f62a002aaaf7e0",
        "archive_part_02.bin",
        62447490,
        "f9c9a111032eedc003844677ffa15862f76359f2274b7ad5ab2dd111b29252c6",
    ),
)
OUTPUT = "VCA_anonymous_review_v5_20260908.zip"
OUTPUT_BYTES = 146333570
OUTPUT_SHA256 = "1a474cf43851d37bd8740671af7c2755d41190ff476ffc5437b11910afc2c1dc"


def main() -> None:
    """Validate all parts, then write a new complete ZIP without extracting it."""
    root = Path(__file__).resolve().parent
    target = root / OUTPUT
    if target.exists():
        raise FileExistsError("Use a new directory; the output ZIP already exists.")
    for part in PARTS:
        path = root / part.filename
        with path.open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
        if actual != part.archive_sha256:
            raise ValueError("Part archive checksum mismatch: " + part.filename)
        with zipfile.ZipFile(path) as archive:
            if archive.namelist() != [part.member]:
                raise ValueError("Unexpected part members: " + part.filename)
            payload = archive.read(part.member)
        if len(payload) != part.payload_bytes:
            raise ValueError("Part payload length mismatch: " + part.filename)
        if hashlib.sha256(payload).hexdigest() != part.payload_sha256:
            raise ValueError("Part payload checksum mismatch: " + part.filename)
    digest = hashlib.sha256()
    total = 0
    with target.open("xb") as destination:
        for part in PARTS:
            with (
                zipfile.ZipFile(root / part.filename) as archive,
                archive.open(part.member) as stream,
            ):
                while block := stream.read(1024 * 1024):
                    destination.write(block)
                    digest.update(block)
                    total += len(block)
    if total != OUTPUT_BYTES or digest.hexdigest() != OUTPUT_SHA256:
        raise ValueError("Combined ZIP checksum mismatch; preserve the failed output.")
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError("Combined ZIP member integrity check failed.")
    print("PASS: " + OUTPUT)
    print("SHA-256: " + OUTPUT_SHA256)
    print("Extract this complete ZIP to a new directory and follow its README.")


if __name__ == "__main__":
    main()
