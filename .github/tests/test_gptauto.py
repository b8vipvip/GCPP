import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from gptauto.engine import begin_verify,criterion,finish,gate,is_complete,plan_ready,start
from gptauto.model import CriterionStatus,Gate,GateStatus,Task
from gptauto.planner import GoalPlanner
class GPTAutoEmbeddedTests(unittest.TestCase):
 def test_dynamic_merge_goal(self):
  t=Task("t","完成修改并合并到 main","b8vipvip/GCPP",[]);start(t);GoalPlanner().apply(t);plan_ready(t);gs=[x.gate for x in t.plan];self.assertIn(Gate.MERGE,gs);self.assertNotIn(Gate.RELEASE,gs)
if __name__=="__main__":unittest.main()
