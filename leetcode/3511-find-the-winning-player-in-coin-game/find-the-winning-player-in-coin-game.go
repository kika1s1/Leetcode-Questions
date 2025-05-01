func losingPlayer(x int, y int) string {
    cnt := 0
    for x >= 1 && y >= 4 {
        cnt += 1
        x -= 1
        y -= 4
    }
    if cnt%2 == 0 {
        return "Bob"
    }
    return "Alice"
}
