import time
from environments import FindArkEnvironment

def GetActionFromModel():
    action = [(5, (6.0, 7.0))]
    return action

def main():
    env = FindArkEnvironment()
    env.reset()

    step_count = 0
    while True:
        
        step_count = step_count + 1
        
        action = GetActionFromModel()
        state = env.step(action)
        time.sleep(0.01)
        print(step_count, state)
 
if __name__ == "__main__":
    main()



