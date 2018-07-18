class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'relapse92'

class TestConfig(BaseConfig):
	DEBUG = True
	Testing = True
	WTF_CSRF_ENABLED = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProcuctionConfig(BaseConfig):
	DEBUG = False