"""Project 15: Strategic Customer Deployment — Capstone — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from fde_bootcamp.acceptance import Check,launch_ready
def main():
    checks=[Check("workflow",True,True),Check("security",True,True),Check("eval",True,True),Check("runbook",True),Check("training",False)]
    print({"launch_ready":launch_ready(checks)})

if __name__=="__main__":
    main()
