from dataclasses import dataclass
@dataclass
class Risk:
    name:str
    likelihood:int
    impact:int
    mitigation:str
    @property
    def score(self): return self.likelihood*self.impact
def top_risks(risks,n=5): return sorted(risks,key=lambda r:r.score,reverse=True)[:n]
