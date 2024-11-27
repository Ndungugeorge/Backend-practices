/*function getMarks(){
    return new Promise(function(resolve, reject){
        const marks = 9;
        if(marks >= 90){
            resolve(marks)
        }
        else reject(marks)

    })
}
getMarks().then(function(data){
    console.log("Cogratulations you passed your examinations!!")
},
function(data){
    console.log("Sorry, you need to redo the test")
}
)*/
// using callback

function walkTheDog(callback){
    setTimeout(() => {
        console.log("You walked the dog 🐕‍🦺");
        callback();
    },1500)}
    //promise
function walkTheDog(){
    return new Promise((resolve,reject) => {
        if (dogWalked = true){
            resolve("You walked the dog");
        }
        else reject("Please make sure you walk the dog tommorow");

    })
    setTimeout(() => {
        console.log("You walked the dog 🐕‍🦺");
        callback();
    },1500)


}
function cleanTheKitchen(callback){
    setTimeout(() => {
        console.log("Wow! the kitchen looks sparckling clean");
        callback();
    },2000)
}
function takeOutTrash(callback){
    setTimeout(() => {
        console.log("You take out the trash");
        callback();
    },2500)
}

walkTheDog(() =>{
    cleanTheKitchen(() =>{
        takeOutTrash(() =>{
            console.log("Job well done!")
        })
    })
})

//function walk(callback){
  //  return new Promise(function(resolve, reject)
//{
  //  resolve(console.log("walk the dog"))

//})
//}
