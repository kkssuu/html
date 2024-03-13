#예외 처리
'''
try:
    print('나누기 전용 계산기입니다.')
    nums=[]
    nums.append(int(input('첫 번째 숫자를 입력하세요 :')))
    nums.append(int(input('두 번째 숫자를 입력하세요 :')))
    #nums.append(int(nums[0]/nums[1]))

    print('{0}/{1}={2}'.format(nums[0],nums[1],nums[2]))
except ValueError:
    print('에러! 잘못된 값을 입력하셨습니다.')
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print('알 수 없는 에러가 발생하였습니다.')
    print(err)
'''


#에러 발생시키기
'''
class Bignumbererror(Exception):
    def __init__(s,m):
        s.m=m

    def __str__(s):
        return s.m 

'''
try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    n1=int(input('첫 번째 숫자를 입력하세요 :'))
    n2=int(input('두 번째 숫자를 입력하세요 :'))
    if n1>=10 or n2>=10:
        raise Bignumbererror('입력값 : {0}, {1}'.format(n1,n2))
    print('{0}/{1}={2}'.format(n1,n2,int(n1/n2)))
except ValueError:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
except Bignumbererror as err:               #사용자 정의 예외처리
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
    print(err)
finally:                                    #finally
    print('계산기를 이용해 주셔서 감사합니다.')

