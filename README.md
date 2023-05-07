# CS361_Project
Term Project for CS 361


The files in the folder Microservices will act as the microservices for the hash database.

The hash database is a simeple two header table named "hashes" with the following headers in order: hashes, file_name

To make a connection with the microservices, use ZeroMQ module for python and connect to "tcp://localhost:5555". An example is given in the client.py file.

To make a request use the function send() to send text converted to binary. The text should be a SQL statement. Examples are given below.

To send request: socket.send(sql_request.encode())

Example SQL statement: SELECT hash FROM hashes WHERE file_name = 'some file'

The SQL statements that can be handled are: SELECT, INSERT and DELETE.

To receive data from the microservices use the recv() function from the ZeroMQ module. Once a request is made the resulting data will be sent back.
For an INSERT or DELETE request the response "Success" will be sent. For a SELECT request, the results of the SQL will be sent.
Each line returned will be a single entry from the table.

If 'exit' is sent as a request then the connection will close.
