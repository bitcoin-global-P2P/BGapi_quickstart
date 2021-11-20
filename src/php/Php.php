<?php

$apiKey = ''; //put here your public key
	$apiSecret = ''; //put here your secret key
	$request = '/api/v1/ads'; //put here request path. For obtaining ads use: /api/v1/ads
	$params = 'currency=USD';
	$baseUrl = ''; //domain without last slash. Do not use https://api.bitcoin.global/
	//If the nonce is similar to or lower than the previous request number, you will receive the 'too many requests' error message
	$nonce = (int) (microtime(true) * 1000); //nonce is a number that is always higher than the previous request number
	$message = $nonce . $apiKey . $request . $params;

	//preparing request URL
	$signature = strtoupper(hash_hmac('sha256', $message, $apiSecret));

	//preparing headers
	$headers = [
	    'Apiauth-Key:'.$apiKey,
	    'Apiauth-Signature:'.$signature,
	    'Apiauth-Nonce:'.$nonce
	];

	$completeUrl = $baseUrl . $request . '?' . $params;

	$connect = curl_init();
	curl_setopt($connect, CURLOPT_URL, $completeUrl);
	curl_setopt($connect, CURLOPT_CUSTOMREQUEST, "GET");
	curl_setopt($connect, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($connect, CURLOPT_RETURNTRANSFER, true);
	$apiResponse = curl_exec($connect);
	curl_close($connect);

	//receiving data
	$jsonArrayResponse = json_decode($apiResponse);
	
	print_r($jsonArrayResponse);
