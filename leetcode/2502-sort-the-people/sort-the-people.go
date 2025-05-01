func sortPeople(names []string, heights []int) []string {
    n :=len(heights)
    for i:=0; i < n; i++{
        swapped :=false
        for j:=0; j < n-1-i; j++{
            if heights[j] < heights[j+1]{
                swapped = true
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]

            }
        }
        if !swapped{
            break
        }
    }
    return names
    
}