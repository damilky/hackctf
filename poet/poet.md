gpwn

![image-20190806231308173](/Users/dani/Library/Application Support/typora-user-images/image-20190806231308173.png)

시를써보자~

![image-20190806231332467](/Users/dani/Library/Application Support/typora-user-images/image-20190806231332467.png)

poem에 입력을 받는다. 



![image-20190806231648592](/Users/dani/Library/Application Support/typora-user-images/image-20190806231648592.png)

저자는 poem +0x400에 저장을 하고

![image-20190806232453694](/Users/dani/Library/Application Support/typora-user-images/image-20190806232453694.png)

strtok로 잘라서 점수가 상승하기 때문에 







 ![image-20190806232445176](/Users/dani/Library/Application Support/typora-user-images/image-20190806232445176.png)

역시 된다 그럼 이걸로 10000000점을 만들어 버려야겠다. 



![image-20190806233144855](/Users/dani/Library/Application Support/typora-user-images/image-20190806233144855.png)



아 이렇게 하면 안되는구나 .. 

이렇게하면

flag

flag

이런식으로 입력된다.



gdb로 다시 돌아가서 

poem부분을 찾아서 살펴보기로 했다.

![image-20190806234454236](/Users/dani/Library/Application Support/typora-user-images/image-20190806234454236.png)

poem을 찾았다.



![image-20190807083242755](/Users/dani/Library/Application Support/typora-user-images/image-20190807083242755.png)

![image-20190807105000075](/Users/dani/Library/Application Support/typora-user-images/image-20190807105000075.png)

get author 





![image-20190807105346137](/Users/dani/Library/Application Support/typora-user-images/image-20190807105346137.png)

rate poem 부분을 살펴보면 strcpy에 첫번째 enter에 입력했던 내용을 copy함 

![image-20190807105602801](/Users/dani/Library/Application Support/typora-user-images/image-20190807105602801.png)

Rsp 보면 전에 enter에서 입력한 값과 author에서 입력한 값이 보인다.

![image-20190807105702841](/Users/dani/Library/Application Support/typora-user-images/image-20190807105702841.png)

좀더 내려가다보면 비교하는 부분이 보이고 

![image-20190807110104804](/Users/dani/Library/Application Support/typora-user-images/image-20190807110104804.png)

그럼 이번엔 일치시켜서 100점을 더해줄 땐 어떻게 진행되는지 살펴봄. 



![image-20190807112631066](/Users/dani/Library/Application Support/typora-user-images/image-20190807112631066.png)

오잉 여기에 100을 더해줫네

![image-20190807112650452](/Users/dani/Library/Application Support/typora-user-images/image-20190807112650452.png)아 -저 위치에서 -0x100해보니까 author에 입력한 값이 나온다 그럼 저 64를 덮어씌우기만 하면 될거같은데 

64자리를 a로 채우고 나머지는 '0xf4240'이거로 채우면 될거같은데 

![image-20190807113035883](/Users/dani/Library/Application Support/typora-user-images/image-20190807113035883.png)

음 뭐 된거같긴 하다! 

![image-20190807113228129](/Users/dani/Library/Application Support/typora-user-images/image-20190807113228129.png)

remote로 돌리니까 상받았ㄸ!ㅏ 