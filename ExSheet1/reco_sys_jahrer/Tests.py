'''
Created on 10.03.2019

@author: bejahrer
'''

import unittest
from MovieLens import MovieLens
import os

class Tests(unittest.TestCase):
    
    def setUp(self):
        if os.name == 'nt':
            self.file = (r'.\ml-latest-small\test.csv')
            self.genre_file = (r'.\ml-latest-small\test_genre.csv')
        else:
            self.file = (r'./ml-latest-small/test.csv')
            self.genre_file = (r'./ml-latest-small/test_genre.csv')
        self.movieLens = MovieLens()
    
    def test_mean(self):
        result = self.movieLens.calcRatings(self.file)
        self.assertEqual(result[0], 3.7142857142857144)
        
    def test_median(self):
        result = self.movieLens.calcRatings(self.file)
        self.assertEqual(result[1], 4)
        
    def test_mode(self):
        result = self.movieLens.calcRatings(self.file)
        self.assertEqual(result[2], 5)
    
    def test_genres(self):
        result = self.movieLens.calcGenres(self.genre_file)
        correctSet = {'genre1', 'genre3', 'genre2'}
        self.assertEqual(result[0], correctSet)
        
    def test_occurence(self):
        result = self.movieLens.calcGenres(self.genre_file) 
        correctList = [('genre2', 3), ('genre3', 2), ('genre1', 1)]      
        self.assertEqual(result[1], correctList)


if __name__ == '__main__': 
    unittest.main()