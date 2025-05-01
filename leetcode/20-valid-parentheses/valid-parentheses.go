func isValid(s string) bool {
    stack := []string{}
    pair := map[string]string{
        "(": ")",
        "{": "}",
        "[": "]",
    }

    for _, par := range s {
        char := string(par)
        if closing, exists := pair[char]; exists {
            stack = append(stack, closing)
        } else {
            if len(stack) == 0 || stack[len(stack)-1] != char {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}