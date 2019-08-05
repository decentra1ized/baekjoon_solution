a=input()
num=a.count('dz=')  #dz의 개수를 센다.
a=''.join(list(filter(('').__ne__, a.split('dz=')))) #dz를 리스트 내에서 모두 삭제
k=['c=','c-','d-','lj','nj','s=','z=']
c=len(a)
for i in range(len(k)):
    num=num+a.count(k[i]) #특정 문자열의 개수를 풀력
    c=c-(len(k[i]))*(a.count(k[i])) #원래의 문자열 길이에서 해당하는 문자열 길이만큼 뺀다(순수 알파벳의 갯수)   
print(num+c) #순수 알파벳의 개수와 특정 문자열의 개수를 더한다

#굳이 이렇게 복잡하게 할 필요가 없다. 간단하게 하면 해당하는 문자열을 다른 문자열로 대체해서 풀면 된다. 

k=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
for ch in k:
    a = a.replace(ch,'*') #해당 문자열을 찾고 하나의 문자로 인식할 수 있게 바꾼다
print(len(a))
