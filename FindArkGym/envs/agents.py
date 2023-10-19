import ctypes
from message import *


class FindArkAgent:
    def __init__(self, client, agent_name):
        self._client = client
        self.name = agent_name
        
        self._action_buffer_size = ctypes.sizeof(ActionMessage)
        self._state_buffer_size = ctypes.sizeof(StateMessage)
        
        self._action_buffer = self._client.malloc(self.name+"_action", self._action_buffer_size)
        self._state_buffer = self._client.malloc(self.name+"_state", self._state_buffer_size)
        
    def act(self, action):
        self.__act__(action)
        
    def __act__(self, action_byte):
        self._action_buffer.seek(0)
        self._action_buffer.write(action_byte)
        
        
    @property
    def action_buf_size(self):
        return self._action_buffer_size
    
    @property
    def state_buf_size(self):
        return self._state_buffer_size
