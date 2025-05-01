func isPalindrome(x int) bool {
    var reversed int
    var original int = x
    if x < 0{
        return false
    }
    for x > 0{
        reversed = reversed * 10 + x%10
        x = x/10
    }
    if reversed == original{
        return true
    }else{
        return false
    }
    
}