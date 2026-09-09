import sys
from pathlib import Path
import unittest
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from fde_bootcamp.value import WorkflowBaseline,monthly_labor_cost,monthly_savings,annualized_value
from fde_bootcamp.scoping import Requirement,priority_score,rank_requirements
from fde_bootcamp.risks import Risk,top_risks
from fde_bootcamp.acceptance import Check,launch_ready
from fde_bootcamp.discovery import completeness

class FDETests(unittest.TestCase):
    def test_cost(self): self.assertEqual(monthly_labor_cost(WorkflowBaseline(100,60,50)),5000)
    def test_savings(self): self.assertEqual(monthly_savings(WorkflowBaseline(100,60,50),30),2500)
    def test_annual(self): self.assertEqual(annualized_value(1000),12000)
    def test_priority(self): self.assertGreater(priority_score(Requirement("a",5,2,2,True)),priority_score(Requirement("b",10,1,1)))
    def test_rank(self): self.assertEqual(rank_requirements([Requirement("a",3,3,3),Requirement("b",9,2,2)])[0].name,"b")
    def test_risk(self): self.assertEqual(top_risks([Risk("a",1,1,"x"),Risk("b",3,3,"x")],1)[0].name,"b")
    def test_critical(self): self.assertFalse(launch_ready([Check("security",False,True),Check("other",True)]))
    def test_threshold(self): self.assertTrue(launch_ready([Check(str(i),i<8) for i in range(10)]))
    def test_discovery(self):
        n={"business_outcome":"x","users":["u"],"workflow":"w","systems":["s"],"data":["d"],"constraints":["c"],"risks":["r"],"success_metrics":["m"]}
        self.assertEqual(completeness(n),1.0)
if __name__=="__main__": unittest.main()
