#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    dir_var = dir(hidden_4)
    for name in dir_var:
        if not name.startswith("__"):
            print(name)
