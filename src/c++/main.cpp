#include <string>
#include <chrono>
#include <curl/curl.h>
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <iostream>
#include <iomanip>

using namespace std;
using namespace std::chrono;
using namespace boost::archive::iterators;

constexpr string_view public_key = ""; // put here your public key
constexpr string_view secret_key = ""; // put here your secret key

string hmac_hex(const string &msg) {
    unsigned char hash[64];
    HMAC_CTX *hmac = HMAC_CTX_new();
    HMAC_Init_ex(hmac, secret_key.data(), secret_key.length(), EVP_sha256(), nullptr);
    HMAC_Update(hmac, reinterpret_cast<const unsigned char *>(msg.data()), msg.length());
    unsigned int len = 32;
    HMAC_Final(hmac, hash, &len);
    HMAC_CTX_free(hmac);
    std::stringstream ss;
    ss << std::hex << setfill('0');
    for (int i = 0; i < len; i++) {
        ss << std::setw(2) << static_cast<unsigned int> (hash[i]);
    }
    return ss.str();
}

string calculate_message(const string &params, string request, string nonce ) {
   //$nonce . $apiKey . $request . $params
   string message = nonce + public_key + request + params
   return message
}

int main() {
    static const string_view request= R"(/api/v1/ads)"; // request
    static const string_view currency = "USD"; // I want to get ads with USD currency
    auto nonce_base = duration_cast<milliseconds>(
            system_clock::now().time_since_epoch()
    ); // nonce is a number that is always higher than the previous request number
    string nonce = string(nonce_base);

    string params = string(R"({"currency":")").append(currency).
                       append(R"("})");

    // payload and signature
    string payload = calculate_payload(params, request, nonce);
    string signature = hmac_hex(payload);

    /* get a curl handle */
    CURL *curl = curl_easy_init();
    if (!curl) {
        cerr << "Failed to initialize curl";
        return -1;
    }

    static const string url = "";
    curl_easy_setopt(curl, CURLOPT_URL, string(url).append(method).c_str());

    curl_slist *chunk = nullptr;

    const string headers[] = {
            "Content-Type:application/json",
            (string("Apiauth-Key:").append(public_key)),
            ("Apiauth-Signature:" + signature),
            ("Apiauth-Nonce:" + nonce )
    };

    for (auto &header: headers) {
        chunk = curl_slist_append(chunk, header.c_str());
    }


    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, chunk);
    //curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data_json.c_str()); //to do


    CURLcode result_code = curl_easy_perform(curl);
    curl_slist_free_all(chunk);
    /* Check for errors */
    if (result_code != CURLE_OK)
        cout << "curl_easy_perform() failed: \n" << curl_easy_strerror(result_code);

    /* always cleanup */
    curl_easy_cleanup(curl);

    return 0;
}