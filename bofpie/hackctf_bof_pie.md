hackctf bofpie



ASLR이 적용 된 것 같았다 이름 보니까..

다이나믹이 적용되어있었고 libc를 구해줘서 rop처럼 풀어줘야 하는 문제 같았다. 

![image-20190730164654093](/Users/dani/Library/Application Support/typora-user-images/image-20190730164654093.png)

main은 welcome을 곧바로 부르는데 welcome의 실행시 주소값을 노출 시켜준다.

그러므로 간단하게 libc를 구해서 풀 수 있다. 



gdb로 분석하며 scanf에서 ret까지의 거리를 구해보았다.

![image-20190730163020881](/Users/dani/Library/Application Support/typora-user-images/image-20190730163020881.png)

이부분을 덮으면 된다! 

여기까지의 거리를 덮어봐야겠다.

![image-20190730163221755](/Users/dani/Library/Application Support/typora-user-images/image-20190730163221755.png)



![image-20190730163509157](/Users/dani/Library/Application Support/typora-user-images/image-20190730163509157.png)

24개에 저 의문의 7000을 뺀 22개를 넣어주면 될거같다.

저 흰색 하이라이트 된 부분이 ret주소 이다. 

그럼 이제 대충 오프셋을 빼주고 오프셋을 이용해서 원하는 원샷 함수에 접근 해보기로 했다. 

페이로드 구성은

"a"*22+(flagfunctionoffset+libcbase)

![image-20190730163906564](/Users/dani/Library/Application Support/typora-user-images/image-20190730163906564.png)

Libc base 주소값을 구했다.

![image-20190730164208883](/Users/dani/Library/Application Support/typora-user-images/image-20190730164208883.png)

flag 

![image-20190730164216927](/Users/dani/Library/Application Support/typora-user-images/image-20190730164216927.png)

함수에서 원하는 조건까지 만들어주면 끝! 

![image-20190730164502105](/Users/dani/Library/Application Support/typora-user-images/image-20190730164502105.png)

끝 ! 

