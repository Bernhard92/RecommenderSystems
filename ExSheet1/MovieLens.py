import csv
import operator


class MovieLens(object):
    
    
    def __init__(self):
        mean, median, mode = self.calcRatings(r'.\ml-latest-small\ratings.csv')
        print mean
        print median
        print mode
        
        genres, sorted_occ = self.calcGenres(r'.\ml-latest-small\movies.csv')
        print genres
        print sorted_occ
        
        
    def calcRatings(self, file_name):
        ratingList = [] 
        
        try:
            ratings = open(file_name, 'rb') 
        except IOError:
            print 'File not found'
            return
        
        reader = csv.reader(ratings)
        next(reader)
        
        for row in reader:
            ratingList.append(float(row[2])) 
            
        ratings.close()
            
        sumRatings = 0
        for rating in ratingList:
            sumRatings += rating;
            
        meanRating = sumRatings/len(ratingList)
        medianRating = ratingList[(len(ratingList)+1)/2 if  (len(ratingList)%2==0) else (len(ratingList))/2]
        modeRating = max(set(ratingList), key=ratingList.count)
        
        return meanRating, medianRating, modeRating        
    
    
    def calcGenres(self, file_name):
        movieGenres = set()
        genreOcc = {}
        
        try:
            movies = open(file_name, 'rb') 
        except IOError:
            print 'File not found'
            return
        
        reader = csv.reader(movies)
        next(reader)
        
        for row in reader:
            genres = row[2].split('|')
            for genre in genres:
                movieGenres.add(genre) 
                genreOcc[genre] = 0
                
        movies.seek(0)
        next(reader)        
        for row in reader:
            genres = row[2].split('|')
            for genre in genres:
                genreOcc[genre] += 1    
                     
        
        movies.close()
        sorted_occ = sorted(genreOcc.items(),  key=operator.itemgetter(1), reverse = True)    
        return movieGenres, sorted_occ
        
        
  
    
if __name__ == '__main__':
    mr = MovieLens()