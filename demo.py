import platform
import fire

def system():
    uname = platform.uname()
    
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

if __name__ == '__main__':
  fire.Fire(system)