class DatabaseException(Exception):
    """Exception class for raising exceptions regarding the database side"""
    
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code