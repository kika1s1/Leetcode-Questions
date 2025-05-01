class SnapshotArray:

    def __init__(self, length: int):
        self.snap_shot = [{} for i in range(length)]        
        self.shot_count = 0
    def set(self, index: int, val: int) -> None:
        self.snap_shot[index][self.shot_count] = val
    def snap(self) -> int:
        self.shot_count +=1
        return self.shot_count -1
    def get(self, index: int, snap_id: int) -> int:
        while snap_id >=0:
            if snap_id in self.snap_shot[index]:
                return self.snap_shot[index][snap_id]
            snap_id -=1
        return 0


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)