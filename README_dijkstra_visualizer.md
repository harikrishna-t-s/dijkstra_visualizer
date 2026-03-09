# Dijkstra Graph Visualizer (Python)

A minimal interactive application that demonstrates how **Dijkstra's
Algorithm** works using a graphical interface.

This project allows users to create their own weighted graph, visualize
it, and observe how the algorithm computes the shortest path from a
selected starting node to all other nodes in real time.

The goal of this project is to make a fundamental concept from **Graph
Theory** easier to understand through visual simulation and interaction.

------------------------------------------------------------------------

# Abstract

Shortest path algorithms play an important role in computer science,
transportation systems, networking, and logistics optimization.

This project implements Dijkstra's Algorithm in Python and integrates it
with a simple graphical interface. Users can manually construct a graph
by adding nodes and weighted edges. Once the graph is defined, the
algorithm can be executed to determine the shortest path distances from
a chosen starting node.

The visualization dynamically highlights nodes as they are visited by
the algorithm, allowing users to observe how the algorithm progresses
step‑by‑step. This approach transforms an otherwise abstract concept
into an intuitive and interactive learning experience.

The system is implemented using Python libraries such as:

-   tkinter for the graphical interface
-   networkx for graph representation
-   matplotlib for visualization

The application emphasizes clarity, simplicity, and educational value
while maintaining a minimal black‑and‑white design aesthetic.

------------------------------------------------------------------------

# Project Motivation

Understanding graph algorithms can be challenging because most
explanations are theoretical or text‑based.

This project attempts to solve that problem by:

-   Allowing users to build graphs interactively
-   Showing the algorithm execution visually
-   Providing a simple interface suitable for beginners

It is particularly useful for:

-   Students learning algorithms
-   Demonstrations in classrooms or labs
-   Anyone curious about how shortest path algorithms work

------------------------------------------------------------------------

# Features

## Interactive Graph Creation

Users can define a graph by entering: - Node 1 - Node 2 - Edge weight

Edges are added dynamically and the graph is immediately visualized.

## Real‑Time Graph Visualization

The graph structure is displayed in the interface using a layout
algorithm that automatically positions nodes.

## Algorithm Execution

Once a graph is created, users can select a starting node and run the
shortest path computation using Dijkstra's Algorithm.

## Step‑by‑Step Visualization

During execution: - Nodes visited by the algorithm are highlighted - The
algorithm's progress can be observed in real time

## Result Summary

After completion, the application displays the shortest distance from
the starting node to all other nodes.

------------------------------------------------------------------------

# Technologies Used

  Technology   Purpose
  ------------ -----------------------------------------
  Python       Core programming language
  tkinter      Graphical User Interface
  networkx     Graph data structure and operations
  matplotlib   Graph visualization
  heapq        Efficient priority queue implementation

------------------------------------------------------------------------

# System Architecture

The project is structured around three major components.

## 1. User Interface Layer

Built using tkinter.

Responsibilities: - Collect graph inputs - Trigger algorithm execution -
Display results

## 2. Graph Representation Layer

Implemented using networkx.

Responsibilities: - Store nodes and edges - Maintain edge weights -
Provide neighbor relationships for the algorithm

## 3. Algorithm Engine

A custom Python implementation of Dijkstra's Algorithm.

Responsibilities: - Compute shortest paths - Maintain priority queue -
Update visited nodes - Send updates to the visualization layer

------------------------------------------------------------------------

# How the Algorithm Works (Simple Explanation)

Imagine a map of cities connected by roads. Each road has a distance.

The goal is to find the shortest distance from one city to every other
city.

Dijkstra's Algorithm works as follows:

1.  Start at the chosen node
2.  Assign distance **0 to the start node** and **infinity to others**
3.  Visit the closest unvisited node
4.  Update distances of its neighbors if a shorter path is found
5.  Repeat until all nodes are visited

The algorithm guarantees the shortest path when all edge weights are
non‑negative.

------------------------------------------------------------------------

# Installation

## Clone the repository

git clone https://github.com/yourusername/dijkstra-visualizer.git\
cd dijkstra-visualizer

## Install dependencies

pip install networkx matplotlib

Note: tkinter usually comes preinstalled with Python.

------------------------------------------------------------------------

# Running the Application

python dijkstra_visualizer.py

A window will open containing the graph interface.

------------------------------------------------------------------------

# How to Use the Program

## Step 1: Add Graph Edges

Enter:

Node 1\
Node 2\
Weight

Then click **Add Edge**.

Example:

A B 4\
A C 2\
B D 5

The graph will appear in the visualization panel.

------------------------------------------------------------------------

## Step 2: Choose Start Node

Example:

Start Node: A

------------------------------------------------------------------------

## Step 3: Execute the Algorithm

Click **Execute Dijkstra**.

During execution:

-   Visited nodes change color
-   The algorithm progresses step‑by‑step

------------------------------------------------------------------------

## Step 4: View Results

After completion, a popup displays the shortest distances.

Example output:

A : 0\
B : 4\
C : 2\
D : 5

------------------------------------------------------------------------

# Code Structure

project/ │\
├── .graph(virtual-environment)
├── dijkstra_visualizer.py\
├── LICENCE
└── README.md

------------------------------------------------------------------------

# Limitations

-   Supports undirected graphs only
-   Negative edge weights are not supported
-   Graph layout is automatic

These constraints align with the standard assumptions of Dijkstra's
Algorithm.

------------------------------------------------------------------------

# Future Improvements

Possible enhancements include:

-   Drag‑and‑drop graph creation
-   Directed graph support
-   Step‑by‑step algorithm controls
-   Highlighting the final shortest path
-   Improved dark‑mode interface
-   Exporting graphs

------------------------------------------------------------------------

# Educational Value

This project demonstrates:

-   Graph data structures
-   Shortest path algorithms
-   Visualization of algorithm behavior
-   Integration of algorithms with user interfaces

It can serve as a learning tool, lab experiment, or introductory
algorithm demonstration.

------------------------------------------------------------------------

# License

This project is released under the MIT License.
