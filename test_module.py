import unittest
from module import transition
class LifecycleTests(unittest.TestCase):
    def test_completion(self): self.assertEqual(transition("RESERVED","complete"),"CONSUMED")
    def test_cancellation_and_expiry(self):
        for event in ("cancel","expire"): self.assertEqual(transition("RESERVED",event),"RESTORED")
    def test_duplicates(self):
        for state,event in (("CONSUMED","complete"),("RESTORED","cancel"),("RESTORED","expire")):
            self.assertEqual(transition(state,event),state)
    def test_conflicts(self):
        for state,event in (("CONSUMED","cancel"),("CONSUMED","expire"),("RESTORED","complete")):
            with self.subTest(state=state,event=event), self.assertRaises(ValueError): transition(state,event)
    def test_unknowns(self):
        for state,event in (("UNKNOWN","complete"),("RESERVED","refund")):
            with self.assertRaises(ValueError): transition(state,event)
if __name__ == "__main__": unittest.main()
