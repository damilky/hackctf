![image-20190731184030587](/Users/dani/Library/Application Support/typora-user-images/image-20190731184030587.png)

ret 에 브레이크 걸면 

![image-20190731184042892](/Users/dani/Library/Application Support/typora-user-images/image-20190731184042892.png)

버퍼 사이 차이는 140 

그럼 136개를 더미로 채우고 나머지 4를 원하는 주소값으로 채우면 된다.

그럼 다시 돌아가서 

![image-20190731184220861](/Users/dani/Library/Application Support/typora-user-images/image-20190731184220861.png)

첫번째 입력때 A를 넣고 두번째 입력때 b를 넣으니 b가 a를 어느정도 덮어쓴다 같은 주소값에 저장해서 그렇다

그럼 첨에 페이로드를 작성해놓고 함수 값을 뛰면 되겠다. 

![image-20190731185352551](/Users/dani/Library/Application Support/typora-user-images/image-20190731185352551.png)

첨에 저 위에 주소값으로 ret해주니까 안됐는데 이유를 알겠따

매번 실행때마다 버퍼주소값이 다르다 .

![image-20190731193841857](/Users/dani/Library/Application Support/typora-user-images/image-20190731193841857.png)

이렇게..



0xffffcf20

![image-20190731201646790](/Users/dani/Library/Application Support/typora-user-images/image-20190731201646790.png)



그래서 매번 버퍼 위치가 달라지는걸 고려해서 먼저 버퍼위치를 확인하고 다음 입력때 쉘코드를 넣어서 ret쉘코드로 덮어주면 끝 !  

