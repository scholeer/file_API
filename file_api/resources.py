import os
from flask_restful import Resource
from flask_restful import reqparse
from file_api.config import Config


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
            path_final = Config.BASE_PATH
        else:
            path_final = os.path.join(Config.BASE_PATH, path)

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
        path_final = os.path.join(Config.BASE_PATH, path)
        file_props = file_info(path_final)

        return file_props


class DeleteFile(Resource):
    def delete(self, path):
        fn = os.path.join(Config.BASE_PATH, path)
        os.remove(fn)
        return '', 204


class CreateFile(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('file')


    def put(self):
        args = self.parser.parse_args()
        filename = args['file']
        try:
            fn = os.path.join(Config.BASE_PATH, filename)
            f = open(fn, "w")
            f.close()
            return f"File '{filename}' created", 201
        except:
            return f"File '{filename}' not created", 400


class CreateDirectory(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('directory')

    def put(self):
        args = self.parser.parse_args()
        directory = args['directory']
        try:
            path = os.path.join(Config.BASE_PATH, directory)
            os.makedirs(path)
            return f"Directory '{directory}' created", 201
        except OSError:
            return f"Directory '{directory}' not created", 400
