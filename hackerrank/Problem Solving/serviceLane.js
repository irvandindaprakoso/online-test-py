function serviceLane(n, width, cases) {
    let result = []

    for (const [start, end] of cases) {
        let min = Infinity
        for (let i= start; i <= end; i++) {
            const w = width[i]
            min = Math.min(min, w)
        }
        result.push(min)
    }

    return result
}


const n = 8;
const width = [
    2, 3, 1, 2, 3, 2, 3, 3
]
const cases = [
    [ 0, 3 ], [ 4, 6 ], [ 6, 7 ], [ 3, 5 ], [ 0, 7 ]
]

console.log(serviceLane(n, width, cases))