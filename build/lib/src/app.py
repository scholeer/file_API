from flask import Flask
from flask_restful import Api
from file_api.resources import ListRootDirectory, ListDirectory, FileInfo, DeleteFile, CreateFile, CreateDirectory
from optparse import OptionParser
from file_api.config import Config

app = Flask(__name__)
api = Api(app)


api.add_resource(ListRootDirectory, '/')
api.add_resource(ListDirectory, '/<path:path>')
api.add_resource(FileInfo, '/file_info/<path:path>')
api.add_resource(DeleteFile, '/delete_file/<path:path>')
api.add_resource(CreateFile, '/create_file')
api.add_resource(CreateDirectory, '/create_directory')


def main():
    parser = OptionParser()
    parser.add_option("-p", "--port", type="int", dest="port",
                      help="set server port number", metavar="PORT")
    parser.add_option("-d", "--directory", type="string", dest="directory",
                      help="set base directory", metavar="DIRECTORY")

    (options, args) = parser.parse_args()
    Config.BASE_PATH = options.directory

    app.run(debug=True, port=options.port)

if __name__ == "__main__":
    main()

#  curl http://localhost:5000/create_file -d "file=dir1/z0.txt" -X PUT
#  curl http://localhost:5000/create_directory -d "file=dir13/dir14" -X PUT
#  curl http://localhost:5000/delete_file/a1.txt -X DELETE
#  curl http://localhost:5000/file_info/dir1/dirA/c3.txt
