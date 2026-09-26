# CS 5330 Produce Photos

This repository contains photos of produce (fruits and vegetables) taken by
students in CS 5330 (Pattern Recognition & Computer Vision) at Northeastern
University during an in-class activity in Fall 2026. The photos were taken with
personal phones in everyday settings: kitchens, grocery stores, and outdoors.
They are later used as a real-world test set for a transfer learning exercise,
in which students compare a model's accuracy on these photos with its accuracy
on a clean public benchmark dataset, to see how well a model trained on curated
images generalizes to casual, uncontrolled photos.

## Folder structure

Each produce type has its own subfolder inside `CS 5330 Fall 2026 Class Dataset`.
Within each subfolder, images are numbered sequentially and named after the
class:

```
CS 5330 Fall 2026 Class Dataset/
├── apple/
│   ├── apple_001.jpg
│   ├── apple_002.jpg
│   └── ...
├── blackberry/
├── blueberry/
├── cranberry/
├── grape/
├── pear/
├── plum/
├── potato/
├── pumpkin/
└── squash/
```

The folder name is the class label, so the layout works directly with
folder-based loaders such as `torchvision.datasets.ImageFolder` or Keras
`image_dataset_from_directory`.

## Contents

| Produce type | Images |
|--------------|-------:|
| apple        | 20 |
| blackberry   | 20 |
| blueberry    | 10 |
| cranberry    | 10 |
| grape        | 10 |
| pear         | 20 |
| plum         | 30 |
| potato       | 10 |
| pumpkin      | 10 |
| squash       | 20 |
| **Total**    | **160** |

The classes are not balanced. Notes on specific classes:

- **cranberry:** the photos show dried cranberries, not fresh ones, and one
  shows them in their retail package.
- **squash:** the class includes butternut squash and chayote.

## Course context

- **Course:** CS 5330 — Pattern Recognition & Computer Vision
- **Institution:** Northeastern University
- **Term:** Fall 2026
- **Instructor:** Dr. Lino Coria

This is coursework material collected by students, not a curated research
dataset. Each contributor photographed their produce with their own device,
background, lighting, and framing, so image quality and conditions vary
naturally across the collection. Some images include a hand holding the item,
other objects, or pets. That variation is intentional: it is what makes the
set useful as a real-world test set.

## Usage

With 10–30 images per class, this dataset is too small to train an image
classifier from scratch. It is meant to be used with a pretrained model, either
as an evaluation set for a model fine-tuned on a larger dataset or as a small
fine-tuning set for transfer learning.

## License and privacy

This dataset is shared for educational and research reference. No formal
license is attached. The images show produce; no faces appear, although some
images include contributors' hands. All EXIF metadata (including any location
data) was removed and filenames were anonymized before upload.
