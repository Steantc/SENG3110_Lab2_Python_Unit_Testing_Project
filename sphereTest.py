import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing test
    def test_volume1(self):
        assert(sphere.volume(30) == 113097.34)
    
    #failing tests
    def test_volume2(self):
        assert(sphere.volume(30) == 113097.33552923254)

    def test_volume3(self):
        assert(sphere.volume(30) == 0)


if __name__ == '__main__':
    unittest.main()