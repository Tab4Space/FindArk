from numpy import dtype
import ctypes

class ActionMessage(ctypes.Structure):
    _fields_ = [
        ("Id", ctypes.c_int32),
        ("Data", ctypes.c_double*3)
    ]
    
class StateMessage(ctypes.Structure):
    _fields_ = [
        ("Id", ctypes.c_int32),
        ("Data", ctypes.c_double*3)
    ]
    
class CameraMessage(ctypes.Structure):
    _fields_ = [
        ("Id", ctypes.c_int32),
        ("Data", ctypes.c_double*3)
    ]
    
ActionDataType = dtype(
    [
        ("MouseXY", ctypes.c_double, (2, )),
        ("SkillNumber", ctypes.c_int32, ),
        ("SkillTargetLoc", ctypes.c_double, (3, )),
        ("ItemNumber", ctypes.c_int32, ),
        ("ItemTargetLoc", ctypes.c_double, (3, ))
    ],
    align = True
)

StateDataType = dtype(
    [
        ("Id", ctypes.c_int32, ),
        ("Location", ctypes.c_double, (3, ))
    ],
    align = True
)