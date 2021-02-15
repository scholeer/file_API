# file_API

curl http://localhost:5000/create_file -d "file=dir1/z0.txt" -X PUT

curl http://localhost:5000/create_directory -d "file=dir13/dir14" -X PUT

curl http://localhost:5000/delete_file/a1.txt -X DELETE

curl http://localhost:5000/file_info/dir1/dirA/c3.txt