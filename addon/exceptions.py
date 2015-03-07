InvalidUserAddException = Exception("Insufficient data to save user")
DuplicateUserException = Exception("Username already present in database")
InvalidStateVariableException = Exception("Submitted state variable does not match program state variable")