import UIKit

// variable declarations
var x : Int = 3
var y : Int = 4
var z : Int = x + y
var s : Float = 3.5
var myNmae : String = "George Marshall"
let pi = 3.14  // let is a constant 

y = 5
print(z)

// Strings

var goodText : String = " the text you care about"
var otherString : String = " the other string \(x) " // this has v
var combinedText : String = goodText + otherString
goodText += otherString

print()

var length : Int = myNmae.characters.count


for value in 1...100 {
    value + value
}

for idx in 0 ..< 10 {
    idx
}

var idx = 0
while idx < 10 {
    idx+=1
    print(idx)
}

repeat {
    idx+=idx
} while idx < 10

var number = 0

switch number {
case 0...4:
    print("hello world" )
case 5...8:
    print(" the number is 8")
default:
    print("the number is: blas")
}


//Functions

func sumTwoNumbers(x: Int, y: Int) -> Int {
    return x + y
}

sumTwoNumbers(x: 2, y: 3)


// Closure = global function
let sumOfTwoInt = {(x: Int, y: Int) in  // in declares and anonymous fucntion
    x+y
}



/* OPTIONALS = variable can have a value or not a value at all. */
let text = "Welcome"
// let number = Int(text)
var name: String?


// Structs = type or class
func printFulNameOfPerson(firstName: String, lastName: String){
    print("\(firstName) \(lastName)")
}
printFulNameOfPerson(firstName: "George", lastName: "Marshall")

// Done in Struct
struct Person {
    var firstName: String
    var lastName: String
    
    init(firstName: String, lastName: String) {
        self.firstName = firstName
        self.lastName = lastName
    }
}

let person1 = Person(firstName: "Victor", lastName: "Sigler"   ) // Usage of a struct

func printFulNameOfPerson(person : Person){
    print("\(person.firstName) \(person.lastName)")
}
printFulNameOfPerson(person: person1)


let label = "The width is "
let width = 94
let widthLabel = label + String(width)











