import unittest
import cone

class coneTest(unittest.TestCase):

    #passing test
    def test_volume1(self):
        assert(cone.volume(12,25) == 3769.91)
    
    #failing tests
    def test_volume2(self):
        assert(cone.volume(12,25) == 3769.911184307752)

    def test_volume3(self):
        assert(cone.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()