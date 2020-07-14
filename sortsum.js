function sortasum(x, y){
    const sum = x + y
    if (sum >= 50 && sum <= 80){
        return 65
    }
    else{
        return 80
    }
}
console.log(sortasum(10, 10))