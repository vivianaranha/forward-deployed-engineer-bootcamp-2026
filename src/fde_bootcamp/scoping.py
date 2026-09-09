from dataclasses import dataclass
@dataclass
class Requirement:
    name:str
    value:int
    effort:int
    risk:int
    must_have:bool=False
def priority_score(r):
    if min(r.value,r.effort,r.risk)<1: raise ValueError("scores must be >= 1")
    return round(r.value/(r.effort+r.risk)+(10 if r.must_have else 0),3)
def rank_requirements(items): return sorted(items,key=priority_score,reverse=True)
