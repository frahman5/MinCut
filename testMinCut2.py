import MinCut2
import unittest

class TestMinCut(unittest.TestCase):

    def setUp(self):
        self.location_SG = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/SampleGraph.txt'
        self.location_one = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/one.txt'
        self.location_two = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/two.txt'
        self.location_three = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/three.txt'
        self.location_four = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/four.txt'

    def test_getEdges(self):
        G = MinCut2.getVertices(self.location_SG)
        answer = [set((1,2)),set((1,7)),set((1,8)),set((2,8)),set((2,7)),
                  set((2,3)),set((3,6)),set((3,5)),set((3,4)),set((4,6)),
                  set((4,5)),set((5,6)),set((6,7)),set((7,8))]
        self.assertEqual(answer,MinCut2.getEdges(G))

    def test_minCut_SG(self):
        answer = 2
        self.assertEqual(answer,MinCut2.main(self.location_SG))

    def test_minCut_1(self):
        answer = 2
        self.assertEqual(answer,MinCut2.main(self.location_one))

    def test_minCut_2(self):
        answer = 2
        self.assertEqual(answer,MinCut2.main(self.location_two))

    def test_minCut_3(self):
        answer = 1
        self.assertEqual(answer,MinCut2.main(self.location_three))

    def test_minCut_4(self):
        answer = 1
        self.assertEqual(answer,MinCut2.main(self.location_four))

suite = unittest.TestLoader().loadTestsFromTestCase(TestMinCut)
unittest.TextTestRunner(verbosity=2).run(suite)
