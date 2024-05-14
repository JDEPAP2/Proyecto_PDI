const video = document.getElementById('cam');
const labl = document.getElementById('label');


// const getCamera = async () =>{
    // try {
    //     stream = await navigator.mediaDevices.getUserMedia({video: true});
    //     cam.srcObject = stream; 
    // } catch (error) {
        
    // }
// }

// const getLabel = async () => {
//     console.log(Flask.url_for('/classifier'))
//     const res = await fetch('http://127.0.0.1:5000/classifier');
//     const js = await res.json()
//     console.log(js)
//     labl.innerText = js.label;
// }


const getVideo = async () =>{
        console.log("pasooo")
        const res = await fetch('http://127.0.0.1:5000/video');
        console.log(res)
        const js = await res.json()
        console.log(js)
    }

document.addEventListener("DOMContentLoaded",()=>getVideo());