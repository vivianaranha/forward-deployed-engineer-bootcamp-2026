"""Project 02: Technical Scope & Success Plan — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from fde_bootcamp.scoping import Requirement,rank_requirements,priority_score
def main():
    reqs=[Requirement("classify",10,3,2,True),Requirement("dashboard",4,5,3),Requirement("citations",9,4,2,True)]
    print([(r.name,priority_score(r)) for r in rank_requirements(reqs)])

if __name__=="__main__":
    main()
