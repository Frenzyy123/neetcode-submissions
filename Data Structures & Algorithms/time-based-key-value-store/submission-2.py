class TimeMap:
    def __init__(self):
        self.values = {}
        self.timestamps = {}
        self.leftTimes = {}
        self.rightTimes = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append(timestamp)
        self.timestamps[timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        else:
            lp = 0
            rp = len(self.values[key]) - 1
            save = ""
            while lp <= rp:
                mid = (lp + rp) // 2
                if self.values[key][mid] <= timestamp:
                    save = self.timestamps[self.values[key][mid]]
                    lp = mid + 1
                else:
                    rp = mid - 1
            
            return save

        