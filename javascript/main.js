function gotoClass( callback){
    setTimeout(() => {
        const bell = 'Bell Ringing'
        callback(bell)
    },2000 )
}
function wakeUp(bell){
    console.log('Go to class')
}
gotoClass(wakeUp)
console.log('prepare yourself for class')