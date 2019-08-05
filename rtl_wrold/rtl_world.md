rtl



![image-20190805144408689](/Users/dani/Library/Application Support/typora-user-images/image-20190805144408689.png)

hidden이 있어서 골드를 쉽게 얻을 수 있고

나머지도 그럼 쉽게 살 수 있다. 

![image-20190805144430084](/Users/dani/Library/Application Support/typora-user-images/image-20190805144430084.png)

코드에 나와있는 내용이다.

![image-20190805144505640](/Users/dani/Library/Application Support/typora-user-images/image-20190805144505640.png)

그럼 익스플로잇을 짜면 되겠다.

![image-20190805144737439](/Users/dani/Library/Application Support/typora-user-images/image-20190805144737439.png)

리턴 위치까지 계산해주기

144개 차이가난다.

![image-20190805152512254](/Users/dani/Library/Application Support/typora-user-images/image-20190805152512254.png)

간단하게 얻을 수 있었다.! 



return to libc 할때 return 의 인자값은 4바이트 뒤에 전달해야함 ! 

그래서 system +aaaa+binsh

요 형태로 작성해줬다. 

저 aaaa를 

하는 이유는 그 다음 리턴 어드레스를 가르키고 있는 용도.

![image-20190805153336049](/Users/dani/Library/Application Support/typora-user-images/image-20190805153336049.png)

이렇게 되기때문이당

wj poppopret가 쓰레기를 가르키게 해야한다.! 



그래서 인자값은 ret +8 맞나 해튼 한칸 뛰어서 놓으면 된다 ! 