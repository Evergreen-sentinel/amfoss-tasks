function is_prime(num){
    if (num < 2){
        return false;
    }
    for(let i=2;i<= Math.sqrt(num);i++){
        if(num%i==0){
            return false;
        }
    }
    return true;
}

function main(){
    const readline=require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Enter the limit n: ", function(limit){
        const n=parseInt(limit);
        console.log();

        for(let i=0;i<n;i++){
            if(is_prime(i)){
                process.stdout.write(i+" ");
            }
        }

        console.log();
        readline.close();
    });


}

main();
