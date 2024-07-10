class ErrorReporter:
    def __init__(self):
        self.errors = []

    def report_error(self, error_type, message, location=None):
        error = {
            'type': error_type,
            'message': message,
            'location': location
        }
        self.errors.append(error)

    def get_errors(self):
        return self.errors

    def has_errors(self):
        return len(self.errors) > 0

    def clear_errors(self):
        self.errors = []