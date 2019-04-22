print('''
- 다운 로드 : docker pull continuumio/miniconda3
- 실행 : docker run -it continuumio/miniconda3 /bin/bash
- 파이썬 실행해보기 : python -c 'print(3*5)'
- 빠져나오기 : exit

- 새로운 이미지 생성 ( 컨테이너 상태 저장하기 )
 > docker run -it continuumio/miniconda3 /bin/bash
 > pip install beautifulsoup4
 > pip install requests
 > exit
 > docker ps -a
 > docker commit <컨테이너 ID> <이름>:<태그>
 > docker commit c63b5b00d942 melearn:init
 > docker run -it melearn:init

- 홈폴더를 마운틴해서 사용하기
 > docker run -it -v <폴더이름>:<컨테이너의폴더> <이미지이름>:<태그이름>
 > docker run -it -v /volumn2/docker/aircomix:/park parka

- synology 설정
 > LANG  C.UTF-8  LC_ALL C.UTF-8
 > /docker/aircomix

''')