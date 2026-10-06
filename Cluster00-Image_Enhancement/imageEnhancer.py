from PIL import Image, ImageEnhance, ImageStat, ImageFilter
import os

# Ask for the image path
image_path = input(
    "Enter image path (press Enter to use input.jpg): "
).strip()

# Use input.jpg if no path is given
if image_path == "":
    image_path = "input.jpg"

# Check if the image exists
if not os.path.exists(image_path):
    print("Image not found!")
    exit()

# Open the image
image = Image.open(image_path)

print("\nChecking image...")

# --------------------------------------------------
# 1. Check brightness
# --------------------------------------------------

gray_image = image.convert("L")
brightness = ImageStat.Stat(gray_image).mean[0]

print(f"Brightness: {brightness:.2f}")

if brightness < 80:
    print("Image is dark. Increasing brightness slightly.")
    image = ImageEnhance.Brightness(image).enhance(1.12)

elif brightness > 190:
    print("Image is bright. Reducing brightness slightly.")
    image = ImageEnhance.Brightness(image).enhance(0.95)

else:
    print("Brightness looks good.")


# --------------------------------------------------
# 2. Check color saturation
# --------------------------------------------------

hsv_image = image.convert("HSV")
saturation = ImageStat.Stat(hsv_image).mean[1]

print(f"Saturation: {saturation:.2f}")

if saturation < 70:
    print("Image looks dull. Increasing color slightly.")
    image = ImageEnhance.Color(image).enhance(1.10)

elif saturation > 150:
    print("Image already has strong colors. Reducing saturation slightly.")
    image = ImageEnhance.Color(image).enhance(0.95)

else:
    print("Saturation looks good.")


# --------------------------------------------------
# 3. Check contrast
# --------------------------------------------------

contrast_value = ImageStat.Stat(gray_image).stddev[0]

print(f"Contrast: {contrast_value:.2f}")

if contrast_value < 35:
    print("Contrast is low. Increasing contrast slightly.")
    image = ImageEnhance.Contrast(image).enhance(1.08)

else:
    print("Contrast looks good.")


# --------------------------------------------------
# 4. Check sharpness
# --------------------------------------------------

# Convert to grayscale and detect edges
gray_for_sharpness = image.convert("L")

edge_image = gray_for_sharpness.filter(
    ImageFilter.FIND_EDGES
)

edge_strength = ImageStat.Stat(edge_image).mean[0]

print(f"Edge detail: {edge_strength:.2f}")

if edge_strength < 8:
    print("Image has low detail. Increasing sharpness slightly.")
    image = ImageEnhance.Sharpness(image).enhance(1.10)

else:
    print("Sharpness looks good.")


# --------------------------------------------------
# 5. Save the enhanced image
# --------------------------------------------------

output_path = "enhanced.jpg"

# JPEG does not support some image modes such as RGBA.
# Convert to RGB before saving.
if image.mode != "RGB":
    image = image.convert("RGB")

image.save(output_path, quality=95)

print("\nImage enhancement completed!")
print("Saved as:", output_path)

