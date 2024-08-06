# Write a program that uses multiprocessing to apply a grayscale filter to multiple images concurrently. Save the processed images to a specified directory.

import multiprocessing
from PIL import Image
import os


def apply_grayscale(image_path, output_dir):
    img = Image.open(image_path).convert("L")
    img.save(os.path.join(output_dir, os.path.basename(image_path)))


if __name__ == "__main__":
    image_paths = [
        "source_images/image1.jpg",
        "source_images/image2.jpg",
        "source_images/image3.jpg",
    ]
    output_dir = "processed_images"
    os.makedirs(output_dir, exist_ok=True)

    processes = [
        multiprocessing.Process(target=apply_grayscale, args=(path, output_dir))
        for path in image_paths
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
