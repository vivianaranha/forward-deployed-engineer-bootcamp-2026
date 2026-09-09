from dataclasses import dataclass
@dataclass
class Check:
    name:str
    passed:bool
    critical:bool=False
def launch_ready(checks):
    if any(c.critical and not c.passed for c in checks): return False
    return sum(c.passed for c in checks)/max(len(checks),1)>=.8
