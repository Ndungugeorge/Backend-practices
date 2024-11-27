/*const first = [1, 2, 3];
const secnd = [4, 5, 6];

const combine = [...first, 'b', ...secnd,'c']
console.log(combine)


//we can combine objects using spread and clone an array or an object.
//Example

const person = {
    name: "George"
}
const specialization = {
    job : "software engineer"
}

const combined = {...person, ...specialization, Age: 26}
console.log(combined)*/


/*function getFullResponseFromAPI(success){
    return new Promise(function(resolve, reject){
        if (success) {
            resolve(console.log({
            status: 200,
            body: 'sucess'  
            }))
            
        }
        else reject(
             console.log('The fake API is not working currently')
        )
           
        } 
    )
}
console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));



import ClassRoom from './0-classroom'

function (initializeRoom){
    return 
}
*/

function getListStudents(){
    return [
        {
        id: 1, firstName: "Gillaume", location: "San Francisco" },
    {
        id: 2, firstName: "James", location: "Columbia"
    },
    {
        id: 5, firstName: "Serena", location: "San Francisco"
    }]
}
//console.log(getListStudents());

//function getListStudentId(array){
//    if (!Array.isArray(array)){ //we don't use typeof in non //primitive data structure
//        return [];
//    }
//    else
//    {
//        return array.map((arr) => arr.id);
//
//    }
//}
//console.log(getListStudentId('hello'));
//console.log(getListStudentId(getListStudents));
//['Alice', 'George', 'Catherine'].map((a) => a + "Ndungu");

//function getStudentLocation(array,city){
   // return array.filter((loc) => loc.location===city)
//}
//let std = getListStudents();
//console.log(getStudentLocation(std, "San Francisco"))
//console.log("hello")

function getStudentIdSum(arry){
    if (!Array.isArray(arry)){
        console.log("arry is not an Array. kindly provide an array")
    }
    return arry.reduce((prev, curr) => prev + curr.id,0);
}
//const ids = getListStudents();
//console.log(getStudentIdSum(ids));

function UpdateStudentGradeByCity(arr,city,newGrades){
    return arr.filter((loc) => loc.location === city)
    .map((loc) =>{
        for (let id of newGrades){
            if (id.studentId === loc.id){
                loc.grade = id.grade;

            }else{
                loc.grade = 'N/A'
            }
        }
        return loc;
    })
}
console.log(UpdateStudentGradeByCity(getListStudents(),"San Francisco", [{studentId: 5, grade: 97},{ studentId: 1, grade: 86}]));