import os
from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

BASE_PATH = "/home/rrr/Documents/test_dir"

parser = reqparse.RequestParser()
parser.add_argument('file')
parser.add_argument('directory')


def file_info(filepath):
    mtime = os.path.getmtime(filepath)
    size = os.path.getsize(filepath)
    file_props = {}
    file_props['time_modified'] = mtime
    file_props['file_size'] = size
    return file_props


class ListDirectory(Resource):
    def get(self, path=None):
        if path is None:
            path_final = BASE_PATH
        else:
            path_final = os.path.join(BASE_PATH, path)

        response = []
        result = os.listdir(path_final)
        for res in result:
            if os.path.isfile(os.path.join(path_final, res)):
                file = {}
                filepath = os.path.join(path_final, res)
                file[res] = file_info(filepath)
                response += [file]
            else:
                response += [res]
        return response


class ListRootDirectory(ListDirectory):
    pass


class FileInfo(Resource):
    def get(self, path):
        path_final = os.path.join(BASE_PATH, path)
        file_props = file_info(path_final)

        return file_props


class DeleteFile(Resource):
    def delete(self, path):
        fn = os.path.join(BASE_PATH, path)
        os.remove(fn)
        return '', 204


class CreateFile(Resource):
    def put(self):
        args = parser.parse_args()
        filename = args['file']
        try:
            fn = os.path.join(BASE_PATH, filename)
            f = open(fn, "w")
            f.close()
            return f"File '{filename}' created", 201
        except:
            return f"File '{filename}' not created", 400


class CreateDirectory(Resource):
    def put(self):
        args = parser.parse_args()
        directory = args['directory']
        try:
            path = os.path.join(BASE_PATH, directory)
            os.makedirs(path)
            return f"Directory '{directory}' created", 201
        except OSError:
            return f"Directory '{directory}' not created", 400


api.add_resource(ListRootDirectory, '/')
api.add_resource(ListDirectory, '/<path:path>')
api.add_resource(FileInfo, '/file_info/<path:path>')
api.add_resource(DeleteFile, '/delete_file/<path:path>')
api.add_resource(CreateFile, '/create_file')
api.add_resource(CreateDirectory, '/create_directory')


if __name__ == '__main__':
    app.run(debug=True)

#  curl http://localhost:5000/create_file -d "file=dir1/z0.txt" -X PUT
#  curl http://localhost:5000/create_directory -d "file=dir13/dir14" -X PUT
#  curl http://localhost:5000/delete_file/a1.txt -X DELETE
#  curl http://localhost:5000/file_info/dir1/dirA/c3.txt
