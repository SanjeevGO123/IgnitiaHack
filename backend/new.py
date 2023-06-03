import os
command = "python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/"+"car2.jpg"+" --plate"
output = os.popen(command).read()
# Extract the necessary information from the output
plate_number = output[18:]