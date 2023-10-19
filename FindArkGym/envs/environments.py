import os
import sys
import random
import numpy as np

import message
from client import FindArkClient


import win32event
import struct

import gymnasium as gym

LOADING_SEMAPHORE   = "Global\\FINDARK_LOADING_SEMAPHORE"
UE_SERVER_SEMAPHORE = "Global\\FINDARK_UESERVER_SEMAPHORE"
PY_CLIENT_SEMAPHORE = "Global\\FINDARK_PYCLIENT_SEMAPHORE"
SHAREDMEMORY_PATH   = "FINDARK_SHAREDMEMORY"



class FindArkEnvironment(gym.Env):
    def __init__(self, rendering_level=0):
        # TODO : fill setting variables
        self.__windows_start_process__()
        self.client = FindArkClient()
        self.agents = self.client.agents 
        self.state = dict()
        self._rendering_level = rendering_level
        
    def reset(self):
        # return initial state
        print("reset")
        self.client.release()
        state = self.__get_state__()
        self.client.acquire()
        print("reset end")
        return state
   
    def step(self, action):
        reward = None
        done = None
        info = None
        
        self.__act__(action)
        self.client.release()
        self.client.acquire()
        self.__get_state__()
        reward = self.__get_reward__()
        return self.state
        
        # if(len(self.agents) == 1):
        #     return (self.state[0], reward, done, info)


    def __windows_start_process__(self):
        loading_semaphore = win32event.CreateSemaphore(None, 0, 1, LOADING_SEMAPHORE)
        result = win32event.WaitForSingleObject(loading_semaphore, 100000)              # sem count +1
        
        if result == win32event.WAIT_TIMEOUT:
            raise("Time out waiting semaphore")
        

    def __act__(self, action):
        for agent in self.agents.values():
            action_byte = np.array(action, dtype=message.ActionDataType).tobytes()
            agent.act(action_byte)
        
    
    def __get_state__(self):
        for agent in self.agents.values():
            agent._state_buffer.seek(0)
            self.state[agent.name] = np.frombuffer(agent._state_buffer.read(32), dtype=message.StateDataType)
    
    def __get_reward__(self):
        return 0
    
    def __get_done__(self):
        return False
        
