import pybullet as p
import time
import pybullet_data
import os

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(),'franka_panda/panda.urdf'), useFixedBase=True)
pandaUid = p.loadURDF(os.path.join('models','testing1_macro.urdf'), useFixedBase=True)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()