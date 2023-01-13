// https://leetcode.com/problems/roman-to-integer/description/

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
// The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given a roman numeral, convert it to an integer.

 

// Example 1:

// Input: s = "III"
// Output: 3
// Explanation: III = 3.

// Example 2:

// Input: s = "LVIII"
// Output: 58
// Explanation: L = 50, V= 5, III = 3.

// Example 3:

// Input: s = "MCMXCIV"
// Output: 1994
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


s = "XXIV";
var romanToInt = function(s) {
    var num = [];
    for (var i = 0; i<s.length;i++){
        if ((s[i] == "I" && (s[i+1] == "V" ||s[i+1] =="X"))||(s[i] == "X" && (s[i+1] == "L" ||s[i+1] =="C"))||(s[i] == "C" && (s[i+1] == "D" ||s[i+1] =="M"))){
            var newitem = s[i]+s[i+1];
            i = i +1;
        }else{newitem = s[i]};
        num.push(newitem)  ;          
    }

    var numbers = 0
    for(i = 0;i<num.length;i++){
        var newnumber
        switch(num[i]){
            case "I":
                newnumber = 1;
                break;
            case "V":
                newnumber = 5;
                break;
            case "X":
                newnumber = 10;
                break;
            case "L":
                newnumber = 50;
                break;
            case "C":
                newnumber = 100;
                break;
            case "D":
                newnumber = 500;
                break;
            case "M":
                newnumber = 1000;
                break;
            case "IV":
                newnumber = 4;
                break;
            case "IX":
                newnumber = 9;
                break;
            case "XL":
                newnumber = 40;
                break;
            case "XC":
                newnumber = 90;
                break;
            case "CD":
                newnumber = 400;
                break; 
            case "CM":
                newnumber = 900;
                break;  
            default:
                newnumber = 0;
        }
        numbers = numbers + newnumber
        
    }
    
    return(numbers)
};
console.log(romanToInt(s))