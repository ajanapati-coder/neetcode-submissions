class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedTime = [()] * len(position)

        for i in range(len(position)):
            positionSpeedTime[i] = (position[i], speed[i], (target - position[i]) / speed[i])
        
        positionSpeedTime.sort(reverse=True)

        numFleets = 1
        leadTime = positionSpeedTime[0][2]
        for i in range(1, len(positionSpeedTime)):
            if positionSpeedTime[i][2] > leadTime:
                numFleets += 1
                leadTime = positionSpeedTime[i][2]
        
        return numFleets

            

