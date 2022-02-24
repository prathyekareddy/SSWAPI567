import unittest

from PA_HW4_SSW_567 import fetchRepos, number_of_commits

class TestFetchGithubRepos(unittest.TestCase):
    def test_getHub_repo(self):
        self.assertEqual(number_of_commits("prathyekareddy", "Triangle567"), 22)
        self.assertEqual(number_of_commits("prathyekareddy", "SSW-567"), 4)
        
if __name__ == '__main__':
    unittest.main()