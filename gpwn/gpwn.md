gpwn

![image-20190805160106099](/Users/dani/Library/Application Support/typora-user-images/image-20190805160106099.png)

gihadra에서 진짜 아무것도 안보여서 

ida로 분석하기 시작했다.

![image-20190805163137568](/Users/dani/Library/Application Support/typora-user-images/image-20190805163137568.png)

Gihandra![image-20190805163212516](/Users/dani/Library/Application Support/typora-user-images/image-20190805163212516.png)

에서는 이렇게 나와서..잘모르겠었다..

사용법이 잘못된걸까 ㅠㅠ fgets엔 정확한 버퍼입력받아서 취약점없고 I를 you로 바꿀때 세글자로 치환돼서 취약점이 발생하는 듯 하다. 

어쨋든 ida로 보면 I를 ->YOU로 치환해주는 코드를 바로 볼 수 있어서 익스플로잇을 시도할 수 있었다.

![image-20190805163314728](/Users/dani/Library/Application Support/typora-user-images/image-20190805163314728.png)

이런식이니까 ret에 브레이크걸고 똑같이 rtl했던것처럼 해주면 될듯

64개 차이난다 

I -> 3글자로 치고 

21개 I a한개

한 후 리턴 덮으면 될거같은데 원샷함수도 있다 그럼 그함수로 바로 리턴시키면 끝일것같다.

![image-20190805171838949](/Users/dani/Library/Application Support/typora-user-images/image-20190805171838949.png)

끝:)

