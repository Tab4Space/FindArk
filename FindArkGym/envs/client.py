import json
import win32event

from shm import SharedMemory
from agents import FindArkAgent



UE_SERVER_SEMAPHORE = "Global\\FINDARK_UESERVER_SEMAPHORE"
PY_CLIENT_SEMAPHORE = "Global\\FINDARK_PYCLIENT_SEMAPHORE"

"""
* 통신 담당

"""

class FindArkClient:
    def __init__(self):
        self._ue_semaphore = None
        self._py_semaphore = None
        self._setting = None
        self._shared_memory = dict()
        self.agents = dict()
        self._time_out = 10

        self.__windows_init__()
        self.__add_agent__()
    
    def __windows_init__(self):
        self._ue_semaphore = win32event.OpenSemaphore(win32event.EVENT_ALL_ACCESS, False, UE_SERVER_SEMAPHORE)
        self._py_semaphore = win32event.OpenSemaphore(win32event.EVENT_ALL_ACCESS, False, PY_CLIENT_SEMAPHORE)
        
    
    def __add_agent__(self):
        with open("C:/Users/park/Documents/FindArkSetting.json", "r") as f:
            self.setting = json.load(f)
            
        for charcter in self.setting["Characters"]:
            self.agents[charcter["CharacterName"]] = FindArkAgent(self, charcter["CharacterName"])
        
    
    def acquire(self):
        print("acquire")
        result = win32event.WaitForSingleObject(self._py_semaphore, win32event.INFINITE)
        # if result == win32event.WAIT_OBJECT_0:
        #     # agent['name']._action_buffer = ~~~
        #     for name in self.agents.keys():
        #         self.agents[name].state_buffer.seek(0)
        #         self.agents[name].state_buffer.read(self.agents[name].state_buf_size)
        #         self.agents[name].action_buffer.write()
                
            
    
    def release(self):
        print("release")
        win32event.ReleaseSemaphore(self._ue_semaphore, 1)
        
    
    def malloc(self, key, buffer_size):
        # Create pointer to accecc shared memory
        self._shared_memory[key] = SharedMemory(key, buffer_size).memory_pointer
        return self._shared_memory[key]
    