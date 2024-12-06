from typing import List, Tuple, Dict
class Solution():
    def lowest(self, distances: list) -> int:
        distances.sort()
        return distances.pop(0)
    
    def getSimilarity(self, l1: list, l2: list) -> List[int]:
        appearances = {k:l2.count(k) for k in l1}
        score = [k*v for k,v in appearances.items()]
        return score
    
    def getDistances(self, file: str) -> Tuple[List, List]:
        l1, l2 = [], []
        with open(file, 'r') as f:
             for line in f.readlines():
                line = line.strip('\n').split('   ')
                l1.append(int(line[0]))
                l2.append(int(line[1]))
        return l1,l2

    def distances(self, file: str) -> Tuple[int,int]:
        distancesInList = []
        list1, list2 = self.getDistances(file)
        similarityScore = sum(self.getSimilarity(list1, list2))
        for i in range(0,len(list1)):
            lowest1 = self.lowest(list1)
            lowest2 = self.lowest(list2)
            distancesInList.append(abs(lowest1 - lowest2))

        distances = sum(distancesInList)
        return distances, similarityScore

if __name__ == "__main__":
    test=Solution()
    print(test.distances('distances'))