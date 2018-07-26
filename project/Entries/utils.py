from functools import wraps

def token_required(f):
	def decorated(*args, **kwargs):
		token = request.args.get('token')
		if not token:
			return jsonify({'message':'token is missing!'}), 403
		try:
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message':'token is invalid'}), 403
		return f(*args, **kwargs)
	return decorated