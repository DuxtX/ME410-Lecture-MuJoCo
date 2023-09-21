# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:58:32 2022

@author: yuhao
"""

import xml.etree.ElementTree as ET
import numpy as np

def to_real5(f1,f2,f3,f4,f5):
    return '{:.6f} {:.6f} {:.6f} {:.6f} {:.6f}'.format(f1,f2,f3,f4,f5)

def to_real3(x,y,z):
    return '{:.6f} {:.6f} {:.6f}'.format(x,y,z)

def to_real2(x,y):
    return '{:.6f} {:.6f}'.format(x,y)

def to_real1(x):
    return '{:.6f}'.format(x)

def tostring(tree):
    return ET.tostring(tree.getroot())

def update_rotor_phi(tree, phi, WRITE):
    root = tree.getroot()
    for body in root.iter('body'):
        if body.attrib['name'] == 'rotor1' or body.attrib['name'] == 'rotor2':
            body.set('euler',to_real3(0,0,phi))
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_foot_weight(tree, foot_weight, WRITE):
    root = tree.getroot()
    for body in root.iter('body'):
        if body.attrib['name'] == 'foot1_contact' or body.attrib['name'] == 'foot2_contact' \
            or body.attrib['name'] == 'foot3_contact' or body.attrib['name'] == 'foot4_contact':
            for inertial in body.iter('inertial'):
                inertial.set('mass',to_real1(foot_weight))
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree
                
def update_rotor_weight(tree, rotor_weight, WRITE):
    root = tree.getroot()
    for body in root.iter('body'):
        if body.attrib['name'] == 'rotor1' or body.attrib['name'] == 'rotor2':
            for inertial in body.iter('inertial'):
                inertial.set('mass',to_real1(rotor_weight))          
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_body_weight(tree, body_weight, WRITE):
    root = tree.getroot()
    for body in root.iter('body'):
        if body.attrib['name'] == 'main_body':
            inertial = body.find('inertial')
            inertial.set('mass',to_real1(body_weight))          
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_beam_length(tree, len1, len2, len3, WRITE):
    root = tree.getroot()
    # Update link1
    for body in root.iter('body'):
        if body.attrib['name'] == 'link1':
            body.set('pos', to_real3(0,0,1e-6/2+len1/2))
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint0':
            joint.set('pos', to_real3(0,0,-len1/2)) 
        if joint.attrib['name'] == 'joint1':
            joint.set('pos', to_real3(0,0,-len2/2)) 
    for geom in root.iter('geom'):
        if geom.attrib['name'] == 'link1':
            geom.set('size', to_real2(.001, len1/2))
    # Update link2       
    for body in root.iter('body'):
        if body.attrib['name'] == 'link2':
            body.set('pos', to_real3(0,0,len1/2+len2/2))
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint2':
            joint.set('pos', to_real3(0,0,-len2/2))   
        if joint.attrib['name'] == 'joint3':
            joint.set('pos', to_real3(0,0,-len2/2)) 
    for geom in root.iter('geom'):
        if geom.attrib['name'] == 'link2':
            geom.set('size', to_real2(.001, len2/2))
    # Update link3   
    for body in root.iter('body'):
        if body.attrib['name'] == 'link3':
            body.set('pos', to_real3(0,0,len2/2+len3/2))
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint4':
            joint.set('pos', to_real3(0,0,-len3/2))   
        if joint.attrib['name'] == 'joint5':
            joint.set('pos', to_real3(0,0,-len3/2)) 
    for geom in root.iter('geom'):
        if geom.attrib['name'] == 'link3':
            geom.set('size', to_real2(.001, len3/2))
    # Update Markers 
    for body in root.iter('body'):
        if body.attrib['name'] == 'load':
            body.set('pos', to_real3(0, 0, len3/2+2e-3))
        if body.attrib['name'] == 'marker1':
            body.set('pos', to_real3(0, -20e-3, len3/2+2e-3))
        if body.attrib['name'] == 'marker2':
            body.set('pos', to_real3(20e-3, 0, len3/2+2e-3))
        if body.attrib['name'] == 'marker3':
            body.set('pos', to_real3(-20e-3, 20e-3, len3/2+2e-3))   

            
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_beam_length_2link(tree, len1, len2, WRITE):
    root = tree.getroot()
    # Update link1
    for body in root.iter('body'):
        if body.attrib['name'] == 'link1':
            body.set('pos', to_real3(0,0,1e-6/2+len1/2))
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint0':
            joint.set('pos', to_real3(0,0,-len1/2)) 
        if joint.attrib['name'] == 'joint1':
            joint.set('pos', to_real3(0,0,-len1/2))   
        if joint.attrib['name'] == 'joint2':
            joint.set('pos', to_real3(0,0,-len1/2)) 
    for geom in root.iter('geom'):
        if geom.attrib['name'] == 'link1':
            geom.set('size', to_real2(.001, len1/2))
    # Update link2       
    for body in root.iter('body'):
        if body.attrib['name'] == 'link2':
            body.set('pos', to_real3(0,0,len1/2+len2/2))
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint3':
            joint.set('pos', to_real3(0,0,-len2/2))   
        if joint.attrib['name'] == 'joint4':
            joint.set('pos', to_real3(0,0,-len2/2)) 
    for geom in root.iter('geom'):
        if geom.attrib['name'] == 'link2':
            geom.set('size', to_real2(.001, len2/2))
    # Update Markers 
    for body in root.iter('body'):
        if body.attrib['name'] == 'load':
            body.set('pos', to_real3(0, 0, len2/2+2e-3))
        if body.attrib['name'] == 'marker1':
            body.set('pos', to_real3(0, -20e-3, len2/2+2e-3))
        if body.attrib['name'] == 'marker2':
            body.set('pos', to_real3(20e-3, 0, len2/2+2e-3))
        if body.attrib['name'] == 'marker3':
            body.set('pos', to_real3(-20e-3, 20e-3, len2/2+2e-3))             
    # Update Foot
        if body.attrib['name'] == 'foot0':
            body.set('pos', to_real3(0, 32.25e-3, 0))
    # Update pos_marker
        if body.attrib['name'] == 'pos_marker':
            body.set('pos', to_real3(0, 0, len2/2+1e-3))
    # Update offset_load
        if body.attrib['name'] == 'offset_load':
            body.set('pos', to_real3(20e-3, 20e-3, 0))
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree
    
def update_stiff_damp(tree, stiffness, damping, WRITE): 
    root = tree.getroot()
    
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint0':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
        if joint.attrib['name'] == 'joint1':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
        if joint.attrib['name'] == 'joint2':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
        if joint.attrib['name'] == 'joint3':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
        if joint.attrib['name'] == 'joint4':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
        if joint.attrib['name'] == 'joint5':
            joint.set('stiffness', to_real1(stiffness))   
            joint.set('damping', to_real1(damping)) 
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_contact_fric(tree, f1, f2, f3, f4, f5, WRITE): 
    root = tree.getroot()
    
    for pair in root.iter('pair'):
        if pair.attrib['name'] == 'foot0_pair':
            pair.set('friction', to_real5(f1, f2, f3, f4, f5))   

    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree

def update_joint_ang(tree, ang0, ang2, ang4, WRITE): 
    root = tree.getroot()
    
    for joint in root.iter('joint'):
        if joint.attrib['name'] == 'joint0':
            joint.set('pos', to_real3(1, np.tan(ang0), 0))   
        if joint.attrib['name'] == 'joint1':
            joint.set('pos', to_real3(0, 0, 1))   
        if joint.attrib['name'] == 'joint2':
            joint.set('pos', to_real3(1, np.tan(ang2), 0))     
        if joint.attrib['name'] == 'joint3':
            joint.set('pos', to_real3(0, 0, 1))    
        if joint.attrib['name'] == 'joint4':
            joint.set('pos', to_real3(1, np.tan(ang4), 0))      
        if joint.attrib['name'] == 'joint5':
            joint.set('pos', to_real3(0, 0, 1))  
    ET.indent(tree)
    if WRITE: tree.write('./opt_xml_dual_rotor.xml')
    return ET.tostring(tree.getroot()), tree
# tree = ET.parse('simplified_model_one_leg.xml')
# update_beam_length(tree, 1e-3,1e-3,3e-3,True)
# update_stiff_damp(tree, 0.4,0.3,True)
