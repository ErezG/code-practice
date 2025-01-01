function createPhoneNumber(numbers){
    part1 = numbers.slice(0,3).join('')
    part2 = numbers.slice(3,6).join('')
    part3 = numbers.slice(6,10).join('')
    return `(${part1}) ${part2}-${part3}`
}

createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])