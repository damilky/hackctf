![image-20190720214456995](/Users/dani/Library/Application Support/typora-user-images/image-20190720214456995.png)

![image-20190720214532667](/Users/dani/Library/Application Support/typora-user-images/image-20190720214532667.png)



버퍼오버플로우가 아니라 포맷스트링이 취약점 이었다.

![image-20190720220146984](/Users/dani/Library/Application Support/typora-user-images/image-20190720220146984.png)

포맷스트링 %n특징



Snprintf (name,sizeof(name2),name2)

snprintf() 함수는 name2 배열에 있는 값을 name2 사이즈만큼 name에 출력하는 함수입니다. 

%n은 %n이 사용되기 직전에 사용된 형식에 의해 출력된 문자들의 개수가 다음 변수에 저장된다.

%n은 stack에서 pop해서 pop된 주소에 현재까지의 문자들의 개수를 저장할 것이다. <- 이 점을 이용해서 attack할 수 있다.

근데 이 때 만약 이 주소가 어떤 함수의 복귀 주소가 저장되어 있다면 ? 

![image-20190720235903687](/Users/dani/Library/Application Support/typora-user-images/image-20190720235903687.png)

이렇게 잘 바뀌는데 저 빨간줄은 어떤 지역변수 함수의 주소값임 저기에 300바이트를 더 더해주니 %n때문에 

%n이 stack에서 pop 했는데 저 주소 값이 나와버렸고 저 주소값에다가 문자들의 개수를 저장해버린 것이다.

그니까 이 문제에서는 

만약 특정 함수의 got를 스택에 넣으면 그 got를 %n이 불러와 내서 자기 할일(그 전 바이트 카운트 해서 저장) 하는 것을 하겠다고 got의 내용을 수정하는 것 이다. 그렇다면 우리가 원하는 주소값을 바이트 수로 셀 수 있게하여 저장하면 된다.

![image-20190721001620424](/Users/dani/Library/Application Support/typora-user-images/image-20190721001620424.png)



![image-20190721001636061](/Users/dani/Library/Application Support/typora-user-images/image-20190721001636061.png)

Print got로 스택에 넣어줬고 어떤 값을 더해서 %n으로 인해 내가원하는 flag값이 나오는지 생각해보면 

134514100 이 것은 flag함수의 16진수 형식 주소값을 10진수로 바꾼것이고

%100d하면 -> %n 으로 출력할시 100으로 뜨는데 

이처럼 %134514100를 하면 이 만큼 더해져 바이트가 계산된다. 



또한 이때 중요한 것이 앞선 printgot크기를 계산하여 (4바이트) + 134514100 -4를 해서 바이트 계산을 해주어야 다음 %n 작업 때 내가 원하는 값으로 정확히 바꿀 수 있다. 