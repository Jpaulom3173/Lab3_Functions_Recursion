import access_control as ac
import media_engine as me
CONTROL_NUM = "5"
FAVORITE_ARTIST = "Bruno Mars"
ARTIST_LEN = len(FAVORITE_ARTIST)
def signal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@signal_decorator
def signal_shutdown(power, count=0):
    if power <= 0:
        return count
    print(f"Current signal strength: {power}")
    return signal_shutdown(power - 1, count + 1)

def run_exercises():
    print("--- Exercise 1: Secure Access System ---")
    access_lvl = ac.compute_access_level(CONTROL_NUM)
    decision = ac.validate_access(access_lvl)
    print(f"Access Level: {access_lvl}")
    print(f"Decision: {decision}\n")

    print("--- Exercise 2: Recursive Signal Shutdown ---")

    initial_power = CONTROL_NUM + ARTIST_LEN
    total_calls = signal_shutdown(initial_power)
    print(f"Total recursive calls: {total_calls}\n")

    print("--- Exercise 3: Streaming Analytics ---")

    limit = CONTROL_NUM + ARTIST_LEN
    total_plays, num_records, generated_list = me.run_analytics(limit)
    print(f"Generated Counts: {generated_list}")
    print(f"Total Plays: {total_plays}")
    print(f"Records Processed: {num_records}")