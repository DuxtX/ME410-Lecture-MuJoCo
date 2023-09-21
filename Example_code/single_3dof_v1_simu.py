#
# Created on Thu Aug 24 2023
#
# Copyright (c) Yuhao
#

import mujoco
import mujoco_viewer
import time
import os
import numpy as np
import sys
import csv
import matplotlib.pyplot as plt

ws=os.path.abspath(os.curdir)
xml_name = "single_3dof_v1_3modules.xml"
xml_path = os.path.join(ws,xml_name)
data_path = r'C:\Users\yuhjiang\OneDrive - epfl.ch\Research\3dof_mujoco'
if os.path.isdir(data_path):
    print('Data directory found.')
else:
    print('Data directory not found.')
    os.mkdir(data_path)
    print('Successfully created data directory')

def mycontroller(model, data):
    # rotor control
    vel_goal = 2*np.pi*f
    data.ctrl[0] = vel_goal
    data.ctrl[1] = -vel_goal
    data.ctrl[2] = -vel_goal
    return

if __name__ == "__main__":
    
    model = mujoco.MjModel.from_xml_path(xml_path)
    # linear_actuator = model.actuator('linear_actuator')
    # balance_servo = model.actuator('balance_servo')
    # linear_actuator.gainprm[0] = 2000
    # balance_servo.gainprm[0] = 1
    Visual = True
    
    for f in np.arange(40,91,1):
        A_oscillator = 20*1e-4 # m
        # f = 30
        ang_vel = np.pi
        data = mujoco.MjData(model)
        mujoco.set_mjcb_control(mycontroller)
        tic = time.time()
        sim_data = np.empty((0,20), int)
        sim_time = []
        
        if Visual:
            # Visualization
            viewer = mujoco_viewer.MujocoViewer(model, data, title='demo', height=1080, width=1920, hide_menus=False)
            # viewer = mujoco_viewer.MujocoViewer(model, data, 'offscreen') # offscreen render for video recording
            cam = viewer.cam
            cam.azimuth = 0.5
            cam.elevation = 0.5
            cam.distance = 0.5
            cam.lookat = np.array([0, 0, 0])
        
        while data.time < 5: 
            mujoco.mj_step(model, data)
            
            if Visual:
                viewer.render() # Initial Render
                
            step_time = data.time
            sim_time.append(step_time)
            main_body_pos = data.body("main_body").xpos # Body position data (1 x 3)
            main_body_quat = data.body("main_body").xquat # Cartesian orientation of body frame (1 x 4)
            main_body_cvel = data.body("main_body").cvel # Body computed velocity [3D rot; 3D tran] (1 x 6)
            main_body_cacc = data.body("main_body").cacc # Body computed acceleration [3D rot; 3D tran] (1 x 6)
            step_data = np.concatenate(([step_time],main_body_quat,main_body_pos,main_body_cvel,main_body_cacc),axis=None)
            # step_data = np.concatenate(([step_time],main_body_pos),axis=None)
            sim_data = np.vstack([sim_data, step_data])
            # print(data.body("main_body").xpos)
        toc = time.time() - tic
        print("Time elipsed: {}".format(toc))
        # sim_data = np.column_stack((sim_time,body_pos))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        Name = '4leg_walking_f={}_A={}'.format(f,A_oscillator)
        Name += '.csv'
        csv.write('{}\{}'.format(data_path,Name), sim_data)
        plt.figure()
        plt.plot(sim_data[:,1], sim_data[:,2])
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.title('Trajectory at f={}Hz, A={}e-4m'.format(f, A_oscillator))
        print('Current simulation finished at f={}, A={}'.format(f, A_oscillator))
        
    plt.show()
    os.system("pause")