title: SaferSearch - iOS & Android Applications
published: 2020-8-10
tags: [iOS, Android, JavaScript, Apache Cordova]
descr: Built in JavaScript / Apache Cordova as a proof of concept and use case example for SaferWebAPI.com. SaferSearch allows users to search for FMCSA & SMS data based on a USDOT number.

SaferSearch is an example of unit-testing via dog-fooding. I didn't have a very good way to express the API's usefulness to developers that were not necessarily in the specialized transportation space.  

The application was developed in JavaScript / Apache Cordova, with cordova you can basically run it through it's own compiler and it will give you Xcode and Android Studio projects to compile to device for. It's the closest thing I've experienced to the promise of "Write once, compile everywhere" 

As an additional benefit of building this app, I was able to add Node.js documentation to the site.

```js
var request = require('request');

var headers = {
    'x-api-key': 'YOUR-API-KEY'
};

var options = {
    url: 'https://saferwebapi.com/v2/usdot/snapshot/US-DOT-NUMBER',
    headers: headers
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
}

request(options, callback);
```

The app is priced at $0.99 and it's available [https://ios.saferwebapi.com](https://ios.saferwebapi.com) or [https://android.saferwebapi.com](https://android.saferwebapi.com)

