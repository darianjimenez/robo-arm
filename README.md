# Weclome to our CompRobo Final Project Website!
Team Members: Rohan, Ahan, Ishan, Darian

## Milestone 1 Update: 
So far, work for our MVP is on track, and we’re beginning research on our stretch goals.

### Status of computational set-up / hardware set-up:
* So far we have been able to connect to the HiWonders arm and use the controller to pick objects up using the instructions provided by the FunRobo repo. We have also been able to set coordinates for the robot arm to go to using the provided code. 

### Major components of the project and their status:
**Color identification:** 
* This file can detect cube shaped objects in front of it (provided a clear working area), identify the color of each cube, and output a set of coordinates the robot arm can use to pick up the cube.
* Current Status: We have a working script which can detect red, green, and blue squares, draw a border around them, and give the center point of each block (we can then use those coordinates with the robot arm so it knows where to go). It currently works with our laptops webcams and requires a blank background.
* Python Libraries: opencv, numpy

**Speech to Text and NLP:**
* The plan for this is to have a file which takes in speech live, infers which color cube the user wants to move with natural language processing, and communicates which block to move.
* Current Status: We have a working script which is able to take live user speech and output the correct block color the user has requested to be picked up. 
* Python Libraries: whisper, sounddevice

**Arm Movement:**
* For this aspect of the project, we want to be able to give the arm coordinates to move to based on where each of the blocks are.
* Current Status: Currently we are able to move the arm to a given set of coordinates, but we have not yet been able to use it to pick anything up. Movement is limited to what we have described in the hardware setup section.

**Testing and Integration:**
* Current Status: So far we have not been able to integrate these components on the robot itself due to time limitations and many team members getting sick/traveling.
* Next Steps: We plan to have an integrated system by the next check-in, which is able to at least go to a cube of a given color based on the users speech. We are also currently conducting research on better pipelines for STT and potentially using more colors than just RGB.
  
### Potential risks to reaching the MVP:
* So far the main risks are interfacing with the hardware. We’ve run into some issues where one day the robot is working completely fine but the next day it’s not
* We were correct in our assumption that the robot would take some time to get set up 
* The best way we see to combat this is to keep our environment clean and report to each other when any change has been made on the robot
* We’ve also run into issues with the natural language processing often being incorrect (or detecting another language) if we don’t speak to it very clearly
* For the Computer Vision aspect of the project, we haven’t run into many issues, however, we don’t anticipate too many for our MVP given we are only using red, green, and blue blocks

### Goals for Milestone 2:
* For Milestone 2 we are on track for what we initially hoped to have done for our MVP. We plan to take these individual parts and incorporate them together. We want to have our robot be able to detect where the blocks are and go to certain blocks given a voice command. 