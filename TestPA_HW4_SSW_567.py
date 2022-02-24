import unittest

from fetchGithubReposInfo import fetchRepos, number_of_commits

class TestFetchGithubRepos(unittest.TestCase):
    """ Test cases to check the results from API results"""
    def test_getHub_repo(self):
        with self.assertRaises(ValueError):
            fetchRepos("Restaurant-Ratings-Project")
        self.assertEqual(number_of_commits("anshulkapoor018", "Restaurant-Ratings-Project"), 30)


if __name__ == '__main__':
    main()