in_a=Element("in_a")
in_b=Element("in_b")
lb_c=Element("lb_c")
sel_math=Element("sel_math")

def equal(*args):
    a=(int)(in_a.element.value)
    b=(int)(in_b.element.value)
    math=sel_math.element.value

    if math=="+":
        c=a+b
    elif math=="-":
        c=a-b
    elif math=="x":
        c=a*b
    elif math=="/":
        c=a/b

    lb_c.element.innerText=c