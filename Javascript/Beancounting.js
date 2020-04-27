function countBs(string) {
    let result = 0;
    //loop over the string
    for(let i = 0; i < string.length; i++) {
        //if current character is "B"
        if(string[i] === "B") {

        //increment our result by 1
            result = result + 1;
        }
    }
    return result;
}

function countChar(string, character) {
    let result = 0;
    
    for(let i = 0; i < string.length; i++) {
        //if current character matches input character
        if(string[i] === character) {
            //increment our result by 1
            result = result + 1;
        }

    }

    //return result
    return result;
} 

    
    
    
    
    }
    
    }
    
    console.log(countBs("BcBBk"));
    console.log(countChar("kakkerkayukkk", "k"))