 #🖼️ Image Metadata Analyzer

A simple Python-based tool that analyzes an image and generates a detailed **metadata report**. It extracts basic file information such as file size, format, dimensions, resolution, color mode, and available EXIF metadata.

## ✨ Features

* 📁 Accepts an image file path as input
* 📊 Displays image dimensions and file size
* 🖼️ Detects image format
* 🎨 Displays color mode
* 📐 Extracts resolution/DPI information when available
* 📷 Extracts EXIF metadata when available
* 📅 Displays camera and date-taken information when available
* 🔄 Supports multiple image formats

## 📂 Supported Formats

### Required

* JPG / JPEG
* PNG

### Bonus

* TIFF
* WEBP
* BMP

## 🛠️ Technologies Used

* **Python**
* **Pillow (PIL)**
* **Pathlib**
* **ExifTags**

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/image-analyzer.git
```

### 2. Navigate to the project directory

```bash
cd image-analyzer
```

### 3. Install the required dependency

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the program by providing the image path:

```bash
python image_analyzer.py photo.jpg
```

You can also provide the path to an image located somewhere else on your computer:

```bash
python image_analyzer.py "C:\Users\YourName\Pictures\image.jpg"
```

## 📊 Sample Output

```text

========================================
IMAGE METADATA REPORT
========================================
File Name       : photo.jpg
File Size       : 35.98 KB
File Format     : JPEG
Width           : 640 px
Height          : 762 px
Resolution      : 150.00 x 150.00 DPI
Color Mode      : RGB

EXIF Metadata
----------------------------------------
No EXIF metadata found.
========================================
