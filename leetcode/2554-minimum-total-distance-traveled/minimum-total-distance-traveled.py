class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort(key=lambda x: x[0])

        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]

        for i in range(robot_count):
            dp[i][factory_count] = 1e12 
        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]

                skip = dp[i][j + 1]

                dp[i][j] = min(assign, skip)  

        return dp[0][0]  