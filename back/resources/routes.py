from .auth import RegisterApi,LoginApi,GetAllElementApi,getuserbylist


def initialize_routes(api):

    api.add_resource(RegisterApi,'/api/auth/signup')
    api.add_resource(LoginApi,'/api/auth/login')
    api.add_resource(GetAllElementApi,'/api/getalluser')
    api.add_resource(getuserbylist,'/api/getusers/<string:listid>/<int:id>')

