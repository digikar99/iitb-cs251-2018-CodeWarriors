var CryptoJS = require('crypto-js');
var axios = require('axios');
var $ = require('jquery');

/************************ LOADING KEYS **************************************/
if (localStorage['iitb-spc-dec-keys']!=null){
    $('dec-key-cache').innerHTML 
	= "Keys are present in browser cache. Choose the new file, only if "
	+ "you want to update the decryption keys. Note that this will "
	+ "overwrite the existing keys present in browser cache.";
    
} else {
    $('#dec-key-cache').innerHTML
	= "Please select the file containing decryption keys.";
}

$('#load-key').click(function(){
    var file = $('#dec-key').prop('files')[0];
    var reader = new FileReader();
    reader.readAsText(file, "UTF-8");
    reader.onload = function(e) {
	// $('#hello').innerHTML = reader.result;
	console.log('file read');
	console.log(reader.result);
	e = $('#algo');
	if (e.val() == 'rsa'){
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

$('#load-enc-file').click(function(){
    var file = $('#enc-file').prop('files')[0];
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
	// $('#pdf').src = file_data;
    }
});

message = ''
host='http://127.0.0.1:8000/download_file'
var current_folder = ''

/*************************** LOADING FILE FROM SERVER ***********************/

function listFolder(fold_name){
    if (typeof(fold_name) != 'string'){
	fold_name = $(fold_name.target).text().slice(1);
	// note the space added/removed
    }
    current_folder = current_folder + fold_name + '/';
    axios.get(host+current_folder).then(function(response){
	console.log(current_folder);
	var item_list = response.data;
	var dest = $('#directory-contents');
	dest.empty();
	var dir_node = '';
	for(var item in item_list){ // first display the directories
	    if (item_list[item] == 'dir'){
		dir_node = '<li class="folder"><i class="fa fa-folder" aria-hidden="true"></i> '
		    + item + '</li>';
		dest.append(dir_node);
		//$('#directory-contents:last-child').click(listFolder(item));
	    }
	}
	for(var item in item_list){ // then display the files
	    if (item_list[item] == 'file'){
		dir_node = '<li class="file"><i class="fa fa-file" aria-hidden="true"></i> '
		    + item + '</li>';
		dest.append(dir_node);
		//$('#directory-contents:last-child').click(downloadFile(item));
	    }
	}
	$('.folder').click(listFolder);
	$('.file').click(downloadFile);
    });
}

function downloadFile(file){
    file_name = $(file.target).text().slice(1);
    axios.get(host+current_folder+file_name).then(function(response){
	// console.log(response.data);
	file_data = response.data;
	decryptFile();
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
	e = $('#algo').val();
	key = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				     .split(',')[0]);
	iv = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				    .split(',')[1]);
	console.log(file_data.length);
	var ciphertext = CryptoJS.enc.Base64.parse(file_data);
	var dec = ''
	if (e == 'aes'){
	    dec = decrypt_core_AES_CBC(key, iv, ciphertext);
	} else if (e == '3des'){
	    dec = decrypt_core_TripleDES_CBC(key, iv, ciphertext);
	} else if (e == 'camellia'){
	    dec = decrypt_core_Camellia_CBC(key, iv, ciphertext);
	}
	console.log("decryption successful");
	console.log(typeof(dec));
	// console.log(dec);
	$('#download-anchor')
	    .prop('href',
		  "data:application/octet-stream;"
		  // = "data:application/mp4;" // for videos
		  + "charset=utf-16le;base64,"
		  + dec); // assume application/octet-stream
	// + file_data.slice(28);

    } else {
	console.log('No decryption keys found.');
    }
}

listFolder(current_folder);


/********* Reference: ***********/
// https://stackoverflow.com/questions/31680986/how-to-achieve-cryptojs-decryption-using-aes-128-cbc-algorithm
// http://jsfiddle.net/fyodgw58/1/

// ReactDOM.render(<MyDocument />, $('#pdf'));
