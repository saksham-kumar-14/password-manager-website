let suggested_password = "";
const ascii_chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
const length = Math.floor(Math.random() * 25) + 20; 
for(let i=0;i<length;i++){
    const index = Math.floor(Math.random()*(ascii_chars.length))
    suggested_password += ascii_chars[index]
}

document.getElementById("suggested-password-btn").onclick=()=>{
    document.getElementById("suggested-password").innerHTML = suggested_password; 
}