import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', default='minhdua@1234567890')

    BLOB_ACCOUNT = os.getenv('BLOB_ACCOUNT', default='minhduablob')
    BLOB_STORAGE_KEY = os.getenv('BLOB_STORAGE_KEY', default='iJb6WpBAoC737vxlC27+cNFvCXQe9qf5zWxFJkn8sruv1YMbD0ZtpwoPaudgw35Jec2L1ddrKwp3+AStsbtP2A==')
    BLOB_CONTAINER = os.getenv('BLOB_CONTAINER', default='images')

    SQL_SERVER = os.getenv('SQL_SERVER', default='minhdua-sql-server.database.windows.net')
    SQL_DATABASE = os.getenv('SQL_DATABASE', default='minhdua-db')
    SQL_USER_NAME = os.getenv('SQL_USER_NAME', default='mdadmin')
    SQL_PASSWORD = os.getenv('SQL_PASSWORD', default='minhdua_12345')
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', default='Vbn8Q~uaF1-42hkKOkioaX~F7ACdVa49WHB_Dc-M')
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = os.getenv('AUTHORITY', default='https://login.microsoftonline.com/common')  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = os.getenv('CLIENT_ID', default='c9969ba4-9dd5-45cd-b0e6-8b58e6f9cb78')

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session