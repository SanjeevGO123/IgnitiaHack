# IgnitiaHack

## Backend
Flask server for the backend of the Ignitia Hackathon
to run the server, run the following commands:
```cd backend
conda env create -f conda-cpu.yml
conda activate yolov4-cpu1
python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4 
python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/car2.jpg --plate

```

