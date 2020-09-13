title: Docs.Permit-Data.com
published: 2020-7-4
tags: [Python, Flask, Microsoft SQL Server, REST, API]
descr: A custom REST API using Flask to consume data stored in an on premise Microsoft SQL Server. 


### An attempt to bring forward data from a legacy application.
This was a custom REST API designed and built by myself to decode and serve PDF documents stored in blobs on an on premise installation of Microsoft SQL Server. 

It's used primarily to provide customer facing documents to both a WordPress installation and an Apache Cordova app (iOS and Android).  
I built a custom view inside of SQL Server and use Flask-SQLAlchemy to map that as a python object.  
Flask serves the document with BytesIO to decode it and the send_file method.  
It's running in a compute engine instance on GCP with Stack Driver monitoring.  
