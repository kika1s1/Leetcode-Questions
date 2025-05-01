func kthDistinct(arr []string, k int) string {
	count := map[string]int{}
	for _, num := range arr {
		count[num] += 1
	}
	cnt := 0
	for _, num := range arr {
		if count[num] == 1 {
			cnt += 1
			if cnt == k {
				return num
			}
		}

	}
	return ""
}