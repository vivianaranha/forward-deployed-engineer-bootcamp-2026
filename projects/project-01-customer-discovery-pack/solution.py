"""Project 01: Customer Discovery Pack — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from fde_bootcamp.discovery import completeness
def main():
    notes={"business_outcome":"reduce resolution time","users":["agent"],"workflow":"receive-research-respond","systems":["ticketing"],"data":["tickets"],"constraints":["4-week POC"],"risks":["access"],"success_metrics":["resolution time"]}
    print({"completeness":completeness(notes)})

if __name__=="__main__":
    main()
