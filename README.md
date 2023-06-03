# IgnitiaHack

## Backend 
### Installation
1. Install [Python 3.8](https://www.python.org/downloads/release/python-380/)
2. pip install -r requirements.txt
3. activate the environment

### Running the server
```bash
python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4 
python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/car2.jpg --plate
```