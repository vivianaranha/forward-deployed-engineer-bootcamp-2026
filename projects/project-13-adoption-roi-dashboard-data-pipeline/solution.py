"""Project 13: Adoption & ROI Dashboard Data Pipeline — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from fde_bootcamp.value import WorkflowBaseline,monthly_savings,annualized_value
def main():
    b=WorkflowBaseline(5000,12,45)
    s=monthly_savings(b,8)
    print({"monthly_savings":s,"annualized_value":annualized_value(s)})

if __name__=="__main__":
    main()
