from json import loads


class ObjToDict:
    def __init__(self):
        pass

    @staticmethod
    def object_as_dict(obj):
        data = None
        if isinstance(obj, list):
            data = [
                {
                    'id': row.id,
                    'movie_name': row.movie_name,
                    'movie_duration': row.movie_duration,
                    'movie_rating': float(row.movie_rating),
                    'movie_release': str(row.movie_release),
                    'movie_description': loads(row.movie_desc).get('description')
                } for row in obj
            ]
        else:
            data = {
                    'id': obj.id,
                    'movie_name': obj.movie_name,
                    'movie_duration': obj.movie_duration,
                    'movie_rating': float(obj.movie_rating),
                    'movie_release': obj.movie_release,
                    'movie_description': loads(obj.movie_desc).get('description')
                }
        return data