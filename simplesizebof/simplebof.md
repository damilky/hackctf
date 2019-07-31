![image-20190730224727431](/Users/dani/Library/Application Support/typora-user-images/image-20190730224727431.png)

버퍼의 주소를 알려준다.



![image-20190731153104181](/Users/dani/Library/Application Support/typora-user-images/image-20190731153104181.png)



sfp 다음 옆에있는 주소가 ret주소일 것이다. 

여기엔 원샷 함수가 없어서 페이로드를 직접 넣어줘야한다.

페이로드는 그럼 

![image-20190731155949007](/Users/dani/Library/Application Support/typora-user-images/image-20190731155949007.png)

sfp까지 계산한 값에서 /bin/sh ->31바이트값을 빼서 

31바이트 쉘코드 + 더미값27929 + 덮어쓸ret값

으로 하면 끝! 

![image-20190731155934995](/Users/dani/Library/Application Support/typora-user-images/image-20190731155934995.png)



성공! 

