class TimeMap:

    def __init__(self):
        self.timeMap = {}
        self.timeStamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key][timestamp] = value
        else:
            self.timeMap[key] = {}
            self.timeMap[key][timestamp] = value



        if key not in self.timeStamps:
            self.timeStamps[key] = [timestamp]
        else:
            self.timeStamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        elif timestamp in self.timeMap[key]:
            return self.timeMap[key][timestamp]
        else:
            relevantTimeStamps = [value for value in self.timeStamps[key] if value <= timestamp]
            if relevantTimeStamps != []:
                return self.timeMap[key][max(relevantTimeStamps)]
            else:
                return ""

            
        
