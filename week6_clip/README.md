# Week 6: "Can CLIP Read?"

Photos for the CS 5330 Week 6 in-class activity on **typographic attacks**
against CLIP. Each photo shows one fruit. Some photos also include a sticky
note with the name of a *different* fruit written on it, to test whether the
written word pulls CLIP's prediction away from what is actually in the image.

## Naming convention

| Pattern | Meaning |
|---|---|
| `<fruit>_plain.jpg` | The fruit alone, with no note |
| `<fruit>_note-<word>.jpg` | The fruit with a sticky note that says `<word>` |

`<fruit>` is the fruit actually in the photo, so it is the correct label.
`<word>` is the text on the note, which is the attack. Names are lower case,
single words, with no spaces.

## Contents

| Fruit | Plain | With note |
|---|---|---|
| apple | `apple_plain.jpg` | `apple_note-banana.jpg` |
| pear | `pear_plain.jpg` | `pear_note-banana.jpg` |
| tomato | `tomato_plain.jpg` | `tomato_note-banana.jpg` |

Every note says "banana", which is not the fruit in any of the photos.

## Processing

The photos were taken on an iPhone as HEIC files and converted with
[`scripts/convert_heic.py`](../scripts/convert_heic.py): orientation applied,
colors converted to sRGB, resized so the longest side is 1600 px, and saved as
JPEG (quality 90) with all metadata, including GPS location, removed.
