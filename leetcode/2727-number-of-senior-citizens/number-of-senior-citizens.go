func countSeniors(details []string) int {
    cnt := 0
	for _, detail := range details {
		ageStr := detail[len(detail)-4 : len(detail)-2]
		age, _ := strconv.Atoi(ageStr)
		if age > 60 {
			cnt++
		}
	}
	return cnt
    
}