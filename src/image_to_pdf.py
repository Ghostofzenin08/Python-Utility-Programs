import sys
import image_to_pdf
import os


filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open("output.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.lower().endswith((".jpeg", ".jpg", ".png")):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(image_to_pdf.convert(imgs)) 

elif os.path.isfile(filepath):
    if filepath.lower().endswith((".jpeg", ".jpg", ".png")):
        with open("output.pdf", "wb") as f:
            f.write(image_to_pdf.convert(filepath))

else:
    print("please input file or directory path")
