// console.log('{{user.username}}')
var CryptoJS = require('crypto-js');
var axios = require('axios');
var $ = require('jquery');

/************************ LOADING KEYS **************************************/
if (localStorage['iitb-spc-dec-keys']!=null){
    $('#dec-key-cache').html( 
	"Keys are present in browser cache. Choose the new file, only if "
	    + "you want to update the decryption keys. Note that this will "
	    + "overwrite the existing keys present in browser cache.");
    
} else {
    $('#dec-key-cache').html(
	"Please select the file containing decryption keys.");
}

$('#dec-key-change').click(function() {
    $('#dec-key').show();
});

$('#dec-key').change(function(){
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
file_name = ''
file_type = ''

$('#load-enc-file').click(function(){
    var file = $('#enc-file').prop('files')[0];
    var reader = new FileReader();
    reader.readAsDataURL(file); // for non text files
    //reader.readAsText(file, "UTF-8");
    reader.onload = function(e) {
	console.log('encrypted file loaded');
	// console.log(reader.result);
	console.log(typeof(reader.result));
	file_data = reader.result;
	console.log(file_data);
	console.log(file_data.length);
	console.log('file reloaded');
	// $('#pdf').src = file_data;
    }
});

message = ''
var username = $('#username').html()
var host='http://127.0.0.1:8000'
// host='http://10.42.0.1/download_file'
var current_folder = '';
var server_data = '/download_file/data/'

/*************************** LOADING FILE FROM SERVER ***********************/

function listFolder(fold_name){
    if (typeof(fold_name) != 'string'){
	fold_name = $(fold_name.target).text().slice(1);
	// console.log("Folder name: " + fold_name);
	// note the space added/removed
    }
    if (fold_name == ' ..'){
	current_folder = current_folder.split('/').slice(0,-2).join('/') + '/';
	// console.log("One folder up: " + current_folder);
    } else {
	current_folder = current_folder + fold_name + '/';
    }
    console.log(current_folder);
    axios.get(host+server_data+current_folder).then(function(response){
	// console.log(current_folder);
	var item_list = response.data;
	var dest = $('#directory-contents');
	dest.empty();
	var dir_node = '';
	if (current_folder != username+'/')
	    dir_node = '<li class="folder"><i class="fa fa-folder" aria-hidden="true"></i> '
	    + ' ..' + '</li>';
	dest.append(dir_node);
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
    fname = $(file.target).text().slice(1);
    $('#decryption-status').html("Decryption started...");
    $('#download-anchor').hide();
    $('#view-button').hide();
    axios.get(host+server_data+current_folder+fname).then(function(response){
	// console.log(response.data);
	file_data = response.data.replace(/ /g, '+');
	file_name = fname;
	decryptFile();
    });
    axios.get(host+'/download_file/file_type/'+current_folder+fname)
	.then(function(response){
	    console.log(response.data);
	    file_type = response.data;
	})
}

/*************************** DECRYPTING FILES ********************************/

function decrypt_core_AES_CBC(key, iv, ciphertext) {
    // console.log(key);
    // console.log(iv);
    message = CryptoJS.AES.decrypt({
	ciphertext: ciphertext
    }, key, {
	iv: iv,
	padding: CryptoJS.pad.ZeroPadding, 
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

function decrypt_core_DES_CBC(key, iv, ciphertext) {
    // there's no camellia module in cryptojs!!
    // console.log(key);
    // console.log(iv);
    
    message = CryptoJS.DES.decrypt({
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
	$('#decryption-status').html("Decryption started...");
	e = $('#algo').val();
	key = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				     .split(',')[0]);
	iv = CryptoJS.enc.Hex.parse(localStorage['iitb-spc-dec-keys']
				    .split(',')[1]);
	console.log(file_data.length);
	// console.log(file_data);
	var ciphertext = CryptoJS.enc.Base64.parse(file_data);
	var dec = ''
	if (e == 'aes'){
	    dec = decrypt_core_AES_CBC(key, iv, ciphertext);
	} else if (e == '3des'){
	    dec = decrypt_core_TripleDES_CBC(key, iv, ciphertext);
	} else if (e == 'des'){
	    dec = decrypt_core_DES_CBC(key, iv, ciphertext);
	}
	console.log("decryption successful");
	console.log(file_type);
	$('#view-name').html(file_name);
	// console.log(typeof(dec));
	//console.log(dec);
	if (file_type == 'png'){
	    $('#view-image-anchor')
		.prop('src', "data:image/png;base64,"+ dec);
	    $('#decryption-status').html('Decryption completed. ');
	    $('#view-button').show()
	}else if (file_type == 'svg'){
	    $('#view-image-anchor')
		.prop('src', "data:image/svg+xml;base64,"+ dec);
	    $('#decryption-status').html('Decryption completed. ');
	    $('#view-button').show()
	}else if (file_type == 'jpg' || file_type == 'jpeg'){
	    $('#view-image-anchor')
		.prop('src', "data:image/jpeg;base64,"+ dec);
	    $('#decryption-status').html('Decryption completed. ');
	    $('#view-button').show()
	// }else if (file_type == 'mp4'){
	//     $('#view-video-anchor')
	// 	.prop('src', "data:video/mp4;base64,"+ dec);
	//     $('#view-video-anchor')
	// 	.prop('type', 'video/mp4');
	//     $('#decryption-status').html('Decryption completed. ');
	//     $('#view-button').show()
	}else{
	    $('#download-anchor')
		.prop('href',
		      // "data:application/octet-stream;"
		      "data:;"
		      // = "data:application/mp4;" // for videos
		      + "charset=utf-16le;base64,"
		      + dec); // assume application/octet-stream
	    $('#download-anchor').prop('download', file_name);
	    $('#decryption-status').html('Decryption completed. ');
	    $('#download-anchor').show();
	}

    } else {
	console.log('No decryption keys found.');
    }
}

// console.log(listFolder);
listFolder(username);
$('#download-anchor').hide();
$('#dec-key').hide();
$('#view-button').hide();

/********* Reference: ***********/
// https://stackoverflow.com/questions/31680986/how-to-achieve-cryptojs-decryption-using-aes-128-cbc-algorithm
// http://jsfiddle.net/fyodgw58/1/

// ReactDOM.render(<MyDocument />, $('#pdf'));
