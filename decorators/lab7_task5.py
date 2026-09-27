from functools import wraps

is_logged_in = False


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper
@require_login
def view_profile():
    print("Profile is displayed.")
# When user is not logged in
print("When logged in = False:")
view_profile()
# When user is logged in
is_logged_in = True
print("\nWhen logged in = True:")
output:
view_profile()
When logged in = False:
Access denied. Please log in.

When logged in = True:
Profile is displayed.
