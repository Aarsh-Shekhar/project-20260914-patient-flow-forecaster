import unittest

from patient_flow_forecaster.models import Record
from patient_flow_forecaster.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="encounter-002", exposure=78791, signal=0.316, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
