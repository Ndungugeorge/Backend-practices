/*function getFullResponseFromAPI(success){
    return new Promise((resolve, reject) =>{
        if(success){
            resolve({status:200,body:'success'});
        }else reject(new Error("The fake API is not working successfully"));

    })
}

console.log(getFullResponseFromAPI(true))
console.log(getFullResponseFromAPI(false))
*/

//Handling promises
function handleResponseFromAPI(promise){
    return promise
        .then(() => ({status: 200, body:'success'}))
        .catch(new Error(''))
        .finally(() => {console.log("Got a response from an API");

        });

}
const promise = Promise.resolve()
handleResponseFromAPI(promise)
    promise.resolve((value) => {
        console.log(value);
    })
