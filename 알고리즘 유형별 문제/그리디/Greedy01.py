import sys
input = sys.stdin.readline

N = int(input()) #회의수
timeTable = []

for i in range(N):
    timeTable.append(list(map(int, input().split())))
#[[A회의 시작시간, A회의 끝나는 시간],[B회의 시작시간,B회의 끝나는 시간]...]
#전체 회의를 위의 형태로 만들어서 사용하려고 함

timeTable.sort() #회의 시작 시간 기준으로 오름차순 정렬
#이때 회의 시작 시간이 같으면 끝나는 시간을 기준으로 오름차순

meeting = timeTable[0] #시작 시간이 가장 빠른 회의를 meeting으로 설정
meetingCnt = 1 #첫회의에 대한 카운트 1, 이후 달음 회의로 넘어갈 때마다 += 1

for i in range(1, N): #두 번째 회의부터 마지막 회의까지, 첫번째 회의는 meeting
    if meeting[0] < timeTable[i][0]:
        if meeting[1] <= timeTable[i][0]: #[0,4][5,10]처럼 meeting의 끝나는 시간이 다음 회의의 시작 시간보다도 빠르면 다음 회의를 meeting에 넣어주고 meetingCnt += 1을 해준다
            meeting = timeTable[i]
            meetingCnt += 1
        elif meeting[1] >= timeTable[i][1]: #[0.5][1,4]처럼 meeting 끝나는 시간이 다음 회의 끝나는 시간보다 늦으면 meeting을 다음 회의값으로 바꾸어준다. 이때는 [0,5]가[1,4]로 대체되는 것이기떄문에 카운트 해주지 않는다
            meeting = timeTable[i]
    elif meeting[0] == meeting[1]: # 예시로 [3,3][4,4]처럼 회의시작시간과 끝나는 시간이 같은 경우
        meeting = timeTable[i] # 다음회의를 meeting에 넣어주고
        meetingCnt += 1 #카운트 해주는 코드

print(meetingCnt)
