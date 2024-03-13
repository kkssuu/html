in_id=Element("in_id")
in_pw=Element("in_pw")
lg=Element("lg")
lgss=Element("lgss")
lb_fail=Element("lb_fail")
in_save=Element("in_save")

def login(*args):
    id=in_id.element.value
    pw=in_pw.element.value
    
    cid="abcd"
    cpw="1234"

    if id==cid and pw==cpw:
        lg.element.style.visibility="collapse"
        lgss.element.style.visibility="visible"
        lb_fail.element.innerText=""

    else:
        lb_fail.element.innerText="로그인 실패"
        
def logout(*args):
    save=in_save.element.checked

    if save==False:
        in_id.element.value=""
    in_pw.element.value=""
    lg.element.style.visibility="visible"
    lgss.element.style.visibility="collapse"
