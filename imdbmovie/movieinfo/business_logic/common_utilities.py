from imdbmovie import app
from json import loads
from datetime import timedelta
from flask_jwt_extended import create_access_token


class Authorization:

    def validate_credentials(self, data):
        """
        Method to Prepare JWT token using credential
        :param data: data contain credentials
        :return: Token with status code
        """
        try:
            boolean_param_list = []
            get_service_data = app.config.get('JWT_CONFIG').get('CREDENTIAL')
            token_identity_param = app.config.get('JWT_CONFIG').get('TOKEN_IDENTITY_PARAM')
            expires_delta = app.config.get('JWT_CONFIG').get('TOKEN_EXPIRY')
            expires_delta = eval(expires_delta) if isinstance(expires_delta, str) else expires_delta
            credentials = data.get('credentials')
            identity_credentials_keys = list(get_service_data.keys())
            for key in identity_credentials_keys:
                if get_service_data[key] != credentials[key]:
                    boolean_param_list.append(False)
                else:
                    boolean_param_list.append(True)

            if False in boolean_param_list:
                return {'msg': "Incorrect Credentials"}, 401
            else:
                access_token = self.auth_token_generate(
                    identity_param_val=credentials[token_identity_param], expires_delta=expires_delta)
                return {'access_token': access_token}, 200
        except Exception as e:
            print(e)
            return {'msg': "Incorrect Credentials"}, 401

    @staticmethod
    def auth_token_generate(identity_param_val, expires_delta=False):
        """
        Method to generate token using valid identity parameter received
        :param identity_param_val: value to the identity parameter using which token will be generated
        :param expires_delta: expires_time
        :return: access token if generated else empty string
        """
        access_token = ''
        try:
            if expires_delta is not False:
                expires_delta = timedelta(minutes=expires_delta)
            access_token = create_access_token(identity=identity_param_val, expires_delta=expires_delta)
        except Exception as e:
            print(e)

        return access_token


class ObjToDict:

    @staticmethod
    def object_as_dict(obj):
        """
        Convert Database data object to dictionary
        :param obj: object as a list or object
        :return: List contain dictionary if object is list or Dictionary
        """
        data = None
        try:
            data = {
                'id': obj.id,
                'movie_name': obj.movie_name,
                'movie_duration': obj.movie_duration,
                'movie_rating': float(obj.movie_rating),
                'movie_release': str(obj.movie_release),
                'movie_description': loads(obj.movie_desc).get('description')
            }
        except Exception as e:
            print(e)
        return data
