from typing import List, Tuple, Dict
import copy
class Solution():
    safe_reports = []
    last_seen = 0
    triedOnce = 0
    tryOneMap = dict()
    tryOneMapFull = []
    
    def convertReport(self, report: str) -> List[int]:
        return [int(n) for n in report.split(" ")]

    def check_report(self, report_list: List[int]) -> bool:
        sorted_report_list = [i for i in sorted(report_list)]
        reversed_report_list = [i for i in reversed(report_list)]
        if sorted_report_list == report_list:
            pass
        elif sorted_report_list == reversed_report_list:
            pass
        else:
            if not self.triedOnce:
                self.tryOneMapFull.append(report_list)
            return False
        for i,n in enumerate(report_list):
            if i == 0:
                self.last_seen = int(n)
                continue
            difference = abs(int(n) - self.last_seen)
            self.last_seen = int(n)
            if difference >= 4:
                if not self.triedOnce:
                    self.tryOneMapFull.append(report_list)
                return False
            if difference <= 0:
                if not self.triedOnce:
                    self.tryOneMapFull.append(report_list)
                return False
        self.safe_reports.append(report_list)
        return True

    def removeOneCheck(self, level: List[int], index: int) -> List[int]:
        new_level = copy.deepcopy(level)
        new_level.pop(index)
        return new_level

    
    def appendToFile(self, file: str, level: str, appendString: str) -> None:
        with open(file+"_processed", "a+") as f:
            level=level.strip("\n")
            newLine = f'{level} {appendString}\n'
            f.write(newLine)

    def getReports(self, file: str) -> list:
        with open(file, 'r') as f:
             reports=[l.strip("\n") for l in f.readlines()]
        return reports

    def safeReports(self, file: str) -> Tuple[int,int]:
        reports = self.getReports(file)
        for report in reports:
            refined_report = self.convertReport(report)
            self.check_report(refined_report)
        self.triedOnce = True
        part1 = len(self.safe_reports)
        for report in self.tryOneMapFull:
            for i, level in enumerate(report):
                removed_report = self.removeOneCheck(report, i)
                if self.check_report(removed_report):
                    break
        part2 = len(self.safe_reports)



        return part1, part2

if __name__ == "__main__":
    test=Solution()
    print(test.safeReports('reports'))