func canAliceWin(nums []int) bool {
    single :=0
    double :=0
    for _, num := range nums{
        if num < 10{
            single +=num
        }else {
            double +=num
        }
    }
    return single != double
    
}