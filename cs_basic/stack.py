def stack_empty(st):
    if len(st) == 0:
        return True
    else:
        return False


def push(st, x):
    st.append(x)


def pop_(st):
    if stack_empty(st):
        return "Underflow"
    else:
        return st.pop()
