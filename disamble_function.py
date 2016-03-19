import dis
def add(a,b):
    c=a+b
    return c

dis.dis(add)
#dis.code_info(add(a,b))
