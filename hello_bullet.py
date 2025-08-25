import pybullet as p
import time
import pybullet_data
import os

p.connect(p.GUI)
pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(),'franka_panda/panda.urdf'), useFixedBase=True)

while True:
    p.stepSimulation()