import numpy as np
from open3d import *

def main():
    pcd= read_point_cloud("PC_1943.pcd")
    draw_geometries([pcd])

if __main__ == "__main__":
  main()
