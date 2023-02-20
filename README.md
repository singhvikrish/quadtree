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


To use the visualizer, simply click on the window where you want to insert a point. The children of the quadtree are automatically created once the number of points exceeds the maximum capacity.


Example of the visualizer:

![Visualizer](https://raw.githubusercontent.com/rishabhsinghvi/QuadTree/master/samples/VisualizerSample.PNG)



3) To run the visualizer with random points:

```
python QuadTree.py -rv
```

or alternatively,

```
python QuadTree.py --random
```

Example of the visualizer:

![Visualizer](https://raw.githubusercontent.com/rishabhsinghvi/QuadTree/master/samples/RandomVisualize.gif)


The visualizer inserts a point every 60 frames, which should translate to 1 second on most systems.


4) To plot speedup between linear and quadtree search, simply run the script with the argument -p or --plot

Example, with 4000 points and the search point in the middle of the linear array.


![Plot](https://raw.githubusercontent.com/rishabhsinghvi/QuadTree/master/samples/SpeedUpPlot.PNG)



