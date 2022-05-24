# DeepQLearning-Snake-Game
This is our first approach to reinforced learning algorithms. it's a simple pygame snake-like game, able to train and play at a decent learning rate.

 This project was made using 
 * Pygame to make the main stages and the snake game itself.
 * Pytorch to make the main learing model.
 * Pandas and numpy to make the main aritmetic operations.
 * Anaconda to make a virtual enviroment suitable for this project


# How to install

First you need to install Anaconda virutal enviroment and initialize it by using 
```
conda create -n "Enviroment name" python="version"
```
Activate virtual enviroment by using.
```
conda activate "Enviroment name"
```
Install pygame and pythorch using
```
pip install pygame
pip install torch torchvision
```
Install mplotlib and ipython
```
pip install matplotlib ipython
```
Finally navigate to root directory and run
```
python .\agent.py
```
*Omit "" when entering enviroment name and python version*
# Stages

This project counts with 2 differentes stages. Both are practically the same with a single main difference. Its size.

The first stage its a canvas of 640 by 480 pixels.

The second stage its a canvas of 840 by 680 pixels.

Both stages count with the same agents. We have the main agent, the sanke or player, and food for the snake to grow.

The user is able to change form stage to stage by changing only 1 single line of code. Located at line 30 of game.py file.

```
  def __init__(self, w=640, h=480):
```
Just change the with and height to the desired value.

*Be advised that we only tested canvas sizes of 640x480 and 840x680 pixels*

