# QuadTree

A QuadTree implementation using Python, with a visualizer written using PyGame.

The QuadTree uses a maximum capacity of 5 points per quad, although it can be changed.

To run the code:

1) Install packages using pip:

```
pip install -r requirements.txt
```

2) To run the visualizer:

```
python QuadTree.py -v
```

or alternatively, 

```
python QuadTree.py --visualize
```

3) To plot speedup between linear and quadtree search, simply run the script without -v


To use the visualizer, simply click on the window where you want to insert a point. The children of the quadtree are automatically created once the number of points exceeds the maximum capacity.

Example of the visualizer:


![Visualizer](https://raw.githubusercontent.com/rishabhsinghvi/QuadTree/master/samples/VisualizerSample.PNG)

