

def valid_user_input_check(username, password):
    if len(username) < 5:
        return ["Username must be at least 5 characters"]
    elif len(username) > 20:
        return ["Username must be less than 20 characters"]
    elif len(password) < 5:
        return ["Password must be more than 5 characters"]
    elif len(password) > 20:
        return ["Password must be less than 20 characters"]
    else:
        return False