import os
import sys
import random
import numpy as np
import ctypes
import mmap
import time

import win32event

SHAREDMEMORY_PATH = "FINDARK_SHAREDMEMORY"

class SharedMemory:
    _numpy_to_ctype = {
            np.bool_:   ctypes.c_bool,
            np.byte:    ctypes.c_byte,
            np.float32: ctypes.c_float,
            np.uint8:   ctypes.c_uint8,
            np.int32:   ctypes.c_int32,
            np.int64:   ctypes.c_int64
        }
    
    def __init__(self, name, buffer_size):
        self.memory_size = buffer_size
        self.memory_path = SHAREDMEMORY_PATH + "_" + name
        print(self.memory_path)
        self.memory_pointer = mmap.mmap(-1, self.memory_size, self.memory_path)
        
        
        
    def writeToMemory(self):
        pass
    
    def readFromMemory(self):
        pass

