var CryptoJS = require('crypto-js');
var axios = require('axios');

var jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

var $ = jQuery = require('jquery')(window);

/************************ LOADING KEYS **************************************/
if (localStorage['iitb-spc-dec-keys']!=null){
    document.getElementById('dec-key-cache').innerHTML 
	= "Keys are present in browser cache. Choose the new file, only if "
	+ "you want to update the decryption keys. Note that this will "
	+ "overwrite the existing keys present in browser cache.";
    
} else {
    document.getElementById('dec-key-cache').innerHTML
	= "Please select the file containing decryption keys.";
}

document.getElementById('load-key').addEventListener("click", function(){
    var file = document.getElementById('dec-key').files[0];
    var reader = new FileReader();
    reader.readAsText(file, "UTF-8");
    reader.onload = function(e) {
	// document.getElementById('hello').innerHTML = reader.result;
	console.log('file read');
	console.log(reader.result);
	e = document.getElementById('algo');
	if (e.options[e.selectedIndex].value == 'rsa'){
	    // if the value is rsa read it this way
	    localStorage['iitb-spc-dec-keys'] = reader.result.split('\n')
		.slice(1,26).join()
	}else{
	    // note that localStorage stores the values as a string
	    localStorage['iitb-spc-dec-keys'] = reader.result.split('\n');
	    // in this case, the two-element array is converted to a common
	    // -separated string!
	    // Use the split(',') function to split it.
	}
    };
});

/************************ LOADING FILE FOR DEBUG ****************************/

file_data = '' // [encrypted] file contents

document.getElementById('load-enc-file').addEventListener("click", function(){
    var file = document.getElementById('enc-file').files[0];
    var reader = new FileReader();
    // reader.readAsDataURL(file); // for non text files
    reader.readAsText(file, "UTF-8");
    reader.onload = function(e) {
	console.log('encrypted file loaded');
	// console.log(reader.result);
	console.log(typeof(reader.result));
	file_data = reader.result;
	console.log(file_data.length);
	console.log('file reloaded');
	decryptFile();
	// document.getElementById('pdf').src = file_data;
    }
});

message = ''

/*************************** LOADING FILE FROM SERVER ***********************/

function listRootFolder(){
    host='http://127.0.0.1:8000/'
    axios.get(host+'download_file/').then(function(response){
	// console.log(response.data);
	var item_list = JSON.parse(response.data);
	for(var item in item_list){
	    if ([item_list] == 'dir')
		console.log($('#directory-contents'));
	}
    });
}


/*************************** DECRYPTING FILES ********************************/

function decrypt_core_AES_CBC(key, iv, ciphertext) {
    // console.log(key);
    // console.log(iv);
    message = CryptoJS.AES.decrypt({
	ciphertext: ciphertext
    }, key, {
	iv: iv,
	padding: CryptoJS.pad.NoPadding, 
	mode: CryptoJS.mode.CBC
    }); 
    //console.log(message);
    return CryptoJS.enc.Base64.stringify(message);
}

function decrypt_core_TripleDES_CBC(key, iv, ciphertext) {
    // console.log(key);
    // console.log(iv);
    message = CryptoJS.TripleDES.decrypt({
	ciphertext: ciphertext
    }, key, {
	iv: iv,
	padding: CryptoJS.pad.NoPadding, 
	mode: CryptoJS.mode.CBC
    }); 
    //console.log(message);
    return CryptoJS.enc.Base64.stringify(message);
}

function decrypt_core_Camellia_CBC(key, iv, ciphertext) {
    // there's no camellia module in cryptojs!!
    // console.log(key);
    // console.log(iv);
    message = CryptoJS.Camellia.decrypt({
	ciphertext: ciphertext
    }, key, {
	iv: iv,
	padding: CryptoJS.pad.NoPadding, 
	mode: CryptoJS.mode.CBC
    }); 
    //console.log(message);
    return CryptoJS.enc.Base64.stringify(message);
}

function decryptFile(){
    if (localStorage['iitb-spc-dec-keys']){
	console.log('ready to decrypt');
	/* "Somehow" get the encrypted data from the server.
	 * Decrypt it. 
	 * Display it to the user.
	 */
	// Note that file_data has been loaded above.
	file_type = 'pdf'
	//file_data = '2DHTnGWbbw2onuMjTu2e9A=='
	e = document.getElementById('algo');
	key = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				     .split(',')[0]);
	iv = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				    .split(',')[1]);
	console.log(file_data.length);
	var ciphertext = CryptoJS.enc.Base64.parse(file_data);
	var dec = ''
	if (e.options[e.selectedIndex].value == 'aes'){
	    dec = decrypt_core_AES_CBC(key, iv, ciphertext);
	} else if (e.options[e.selectedIndex].value == '3des'){
	    dec = decrypt_core_TripleDES_CBC(key, iv, ciphertext);
	} else if (e.options[e.selectedIndex].value == 'camellia'){
	    dec = decrypt_core_Camellia_CBC(key, iv, ciphertext);
	}
	console.log("decryption successful");
	console.log(typeof(dec));
	// console.log(dec);
	document.getElementById('download-anchor').href
	    = "data:application/octet-stream;"
	// = "data:application/mp4;" // for videos
	    + "charset=utf-16le;base64,"
	    + dec; // assume application/octet-stream
	// + file_data.slice(28);

    } else {
	console.log('No decryption keys found.');
    }
}




/********* Reference: ***********/
// https://stackoverflow.com/questions/31680986/how-to-achieve-cryptojs-decryption-using-aes-128-cbc-algorithm
// http://jsfiddle.net/fyodgw58/1/

// ReactDOM.render(<MyDocument />, document.getElementById('pdf'));
