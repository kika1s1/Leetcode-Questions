/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    let primeCount = 0;
    /*
    start from two and iterate until n
    initalise prime as a false boolean
    iterate until the half the index
    if there is a number that can divide that number until half the index change prime boolean to true and break from the innter loop
    otherwise just continue
    after the innerLoop is done, if prime is true increment the primecount
    otherwise just contiue
    */
    if (n === 0 || n === 1 || n === 2)
        return 0;
    for (let i = 2; i < n; i++){
        if (i === 2 || i === 3){
            primeCount += 1;
            continue;
        }
        if (i % 2 === 0)
            continue;
        let prime = true;
        for (let j = 3; j <= Math.floor(Math.sqrt(i)); j += 2){
            if (i % j === 0){
                prime = false;
                break;
            }
        }
        if (prime){
            primeCount += 1;
        }
    }
    return primeCount;
};