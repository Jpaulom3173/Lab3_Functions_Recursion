def audit_log(func):
    """Decorator to log authorization start and completion."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control):
    return control * 3 + 10

@audit_log
def validate_access(level):
    threshold = 5 * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"