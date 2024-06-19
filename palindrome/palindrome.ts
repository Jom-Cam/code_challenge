const input = 1111

function isPalindrome(x:number){
    if (x < 0){
        console.log("Negative Number, not a Palandrome")
        return false
    }
    let arrayX = String(x).split("")

    while (arrayX.length > 0) {
        let currentFirstLetter = arrayX[0];
        let currentLastLetter = arrayX[arrayX.length-1];
        arrayX = arrayX.slice(1, arrayX.length-1)

        if (currentFirstLetter != currentLastLetter) {
            return false
        }
        // console.log(arrayX)
        // console.log(currentFirstLetter)
        // console.log(currentLastLetter)
    }
    return true
}

const answer:string =  isPalindrome(input) ? "This is a Palandrome" : "This is not a Palandrome"
