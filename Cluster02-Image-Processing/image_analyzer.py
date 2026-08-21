from PIL import Image, ExifTags
import os
import sys


def format_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    else:
        return f"{size / (1024 * 1024 * 1024):.2f} GB"


def analyze_image(image_path):

    print("Starting image analysis...")

    if not os.path.exists(image_path):
        print(f"ERROR: Image not found: {image_path}")
        return

    try:
        file_size = os.path.getsize(image_path)

        with Image.open(image_path) as image:

            print()
            print("=" * 40)
            print("IMAGE METADATA REPORT")
            print("=" * 40)

            print(f"File Name       : {os.path.basename(image_path)}")
            print(f"File Size       : {format_size(file_size)}")
            print(f"File Format     : {image.format}")
            print(f"Width           : {image.width} px")
            print(f"Height          : {image.height} px")

            dpi = image.info.get("dpi")

            if dpi:
                print(f"Resolution      : {dpi[0]:.2f} x {dpi[1]:.2f} DPI")
            else:
                print("Resolution      : Not available")

            print(f"Color Mode      : {image.mode}")

            print()
            print("EXIF Metadata")
            print("-" * 40)

            exif = image.getexif()

            if not exif:
                print("No EXIF metadata found.")
            else:
                for tag_id, value in exif.items():

                    tag_name = ExifTags.TAGS.get(tag_id, tag_id)

                    if isinstance(value, bytes):
                        value = value.decode(errors="replace")

                    print(f"{tag_name:<20}: {value}")

            print("=" * 40)

    except Exception as error:
        print("ERROR: Could not analyze image.")
        print("Reason:", error)


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python image_analyzer.py <image_path>")
        print()
        print("Example:")
        print("python image_analyzer.py photo.jpg")
        return

    image_path = sys.argv[1]

    analyze_image(image_path)


if __name__ == "__main__":
    main()