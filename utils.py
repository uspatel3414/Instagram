def validate_env():
    required_vars = [
        'INSTAGRAM_USERNAME',
        'INSTAGRAM_PASSWORD',
        'INSTAGRAM_APP_ID',
        'INSTAGRAM_APP_SECRET'
    ]
    
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")
