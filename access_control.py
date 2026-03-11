def audit_log(func):
    """Decorator to log start and completion of authorization."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, artist_name):
    # Calculation: CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    return (control * 3) + len(artist_name)

@audit_log
def validate_access(level, control):
    # Threshold: CONTROL_NUM * 5
    threshold = control * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"