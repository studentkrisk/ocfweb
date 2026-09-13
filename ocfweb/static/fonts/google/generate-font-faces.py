import sys, os

# argument syntax: python3 generate-font-faces.py FOLDER1 FOLDER2 FOLDER3
# you may have to remove the variable syntax ttfs

with open("font-faces.css", "w") as css:
    for direc in sys.argv[1:]:
        for file in os.listdir("./" + direc):
            if file.split(".")[-1] != "ttf":
                continue

