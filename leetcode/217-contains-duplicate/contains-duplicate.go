func containsDuplicate(nums []int) bool {
    var counter = make(map[int]int)
    for _, num := range nums {
        counter[num] +=1
        if counter[num] > 1 {
            return true
        }
    }
    return false
}