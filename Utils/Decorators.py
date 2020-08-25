def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        profileId = None
        sessionToken = None

        if(request.json != None):
            profileId = request.json.get('profileId')
            sessionToken = request.json.get('sessionToken')

        elif(len(request.args) > 0):
            sessionToken = request.args.get('sessionToken')
            profileId = request.args.get('profileId')

        if(sessionToken == None):
            return {"error": "Invalid session token"}, 401

        if(profileId == None):
            return {'error': 'Invalid profileId'}, 401

        return f(*args, **kwargs)

    return decorated_function