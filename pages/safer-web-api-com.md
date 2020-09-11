title: SaferWebAPI.com  
published: 2020-8-11  
tags: [Python, Flask, PostgreSQL, REST, API, SaaS]  
descr: A subscription based platform that gives rest api access to a publicly available federal transportation database that does not have a native API. Leverages google cloud and python to crawl, scrape abd store results. Returns them to authenticated users in json format with very low latency.  1.6 million USDOT queries so far.



### A very un-sexy, very useful project.
SaferWebAPI.com exists because it was a tool I needed for my day job. The company I work for requires validation against all of the "Company Snapshot" data from [FMCSA SaferWeb](https://safer.fmcsa.dot.gov/). Basically it's a dataset that is related to a unique identifier for a US based trucking company. Before I developed this product this information was manually collected by a call center employee as needed.
<div class='row'>
    <div class='col-sm'>
        <img class='img-fluid' src='/static/img/safer_1.png'>
    </div>
    <div class='col-sm'>
        <img class='img-fluid' src='/static/img/safer_2.png'>
    </div>
</div>
I started with a pretty dormant github project that did some scraping from the CLI, forked it, and contributed several patches upstream. 
You can see my build on [github](https://github.com/justJay-dev/python-safer).

From there it was a matter of standing up user authentication with Flask-Login, SQLAlchemy, and Google CloudSQL (PostgreSQL driver), and then testing ways for it to scale. 

It's deployed on CloudRun which is managed docker containers that bill per-second, scaling out automatically as large as you'll allow it to. This gave me huge advantages in cost management and availability. Because CloudSQL is the only place storing userstate the app itself is totally indifferent to how many instances are running concurrently.

The app uses several SQLAlchemy models to track usage and activation status for each users API key, we support users having unlimited access keys, and alias/friendly naming of each key. Users can start, pause, and delete keys without destroying usage data.

It's monetized using Stripe and the checkouts API, it is currently profitable.

For accounting and other alerting I use several zapier hooks to connect and synchronize records Stripe, Wave Accounting, and Google Sheets.

You can test out the product by starting a free trial [here](https://saferwebapi.com/signup).

