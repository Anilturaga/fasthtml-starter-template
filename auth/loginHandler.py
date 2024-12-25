def loginHandler(email: str, password: str):
    # dummy credential check
    if email == "admin" and password == "admin":
        return True
    else:
        return False
