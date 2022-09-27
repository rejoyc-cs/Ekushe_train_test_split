#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 07:18:40 2022

@author: rejoy
"""

import os
import shutil
import random

def split(ts,rate):
    
    folder = os.listdir(ts)

    ### Creating Test and Train Folders ####
    for i in range(len(folder)):
        path = os.path.join(str(ts+folder[i]),"test")
        os.mkdir(path)
        path = os.path.join(str(ts+folder[i]),"train")
        os.mkdir(path)
    print("Train Test Folder created\n")
      
    ### Randomly picking Training Data ####    
    for i in range(len(folder)):
        j=0
        limit = int(len(os.listdir(ts+folder[i]))*rate)
        while(j<limit):
            image = random.choice(os.listdir(ts+folder[i]))
            if image.endswith(".jpg"):
                src = ts+folder[i] +'/'+ image
                tar = ts+folder[i] + '/train/' + image
                shutil.move(src,tar)
                j+=1
        print("Train Folder ",i," Done!!\n")
        
    ### Remaining Test Data ###
    for i in range(len(folder)):
        for image in os.listdir(ts+folder[i]):
            if image.endswith(".jpg"):
                src = ts+folder[i] +'/'+ image
                tar = ts+folder[i] + '/test/' + image
                shutil.move(src,tar)
        print("Test folder ",i," Done!!\n")

def merge(ms,fs,ts):
    male = []
    female = []
    target = []
    
    #### Creating Target Directories
    for i in range(len(os.listdir(fs))):
        path = os.path.join(str(ts), str(i))
        os.mkdir(path)
    
    
    ### Listing Male Source and Target Directories
    for path in os.listdir(ms):
        male.append(ms+path+'/')
        target.append(ts+'/'+path+'/')
    ### Listing Female Source Directories
    for path in os.listdir(fs):
        female.append(fs+path+'/')
        #target.append(ts+'/'+path+'/')
        
        
    #Merging all male and female files in one directory
    for i in range(len(male)):
        listImages = os.listdir(male[i])
        for file in listImages:
            src = male[i] + file
            tar = target[i] + file
            shutil.move(src,tar)

    
    for i in range(len(female)):
        listImages = os.listdir(female[i])
        for file in listImages:
            src = female[i] + file
            tar = target[i] + file
            shutil.move(src,tar)
            
    print("Merging complete\n")

def main():
    male_src = "/home/rejoy/Desktop/male/"   ##Mention the path of MALE folder
    female_src = "/home/rejoy/Desktop/female/"   ##Mention the path of FEMALE folder
    target_src = "/home/rejoy/Desktop/target/"   ##Mention an existed target folder where to store
    merge(male_src,female_src,target_src)
    rate=0.7
    split(target_src,rate)
    
if __name__ == '__main__':
    main()
    