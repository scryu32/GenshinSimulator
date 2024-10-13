import random

def getCharacter(dolpa, nowdolpa, pickup):
    sangsi = ['다이루크', '각청', '치치', '타이나리', '진', '모나', '데히야']
    time = 0
    alltime = 0
    yourcharacters = []
    hwakchun = False
    while nowdolpa <= dolpa:
        time += 1
        alltime += 1
        num = random.randint(1, 1000)
        if time < 74:
            hwakryul = 6
        if time >= 74:
            hwakryul = 6 + (time-73)*60
        if num <= hwakryul:
            if hwakchun == False:
                num2 = random.randint(1, 2)
                if num2 == 1:
                    yourcharacters.append([pickup, time, '일반'])
                    nowdolpa += 1
                    time = 0
                    hwakchun = False
                else:
                    num3 = random.randint(1, 100)
                    if num3 <= 5:
                        yourcharacters.append([pickup, time, '개지리는5퍼센트'])
                        nowdolpa += 1
                        time = 0
                        hwakchun = False
                    else :
                        yourcharacters.append([random.choice(sangsi), time, '픽뚫'])
                        time = 0
                        hwakchun = True
            else:
                yourcharacters.append([pickup, time, '일반'])
                nowdolpa += 1
                time = 0
                hwakchun = False
    return {"yourcharacters" : yourcharacters, "times" : alltime}

def getProbability(times, pickupcharacter, checkSangwi, nowdolpa, wantdolpa):
    nowjjang = {"yourcharacters" : [], "times" : 10000}
    gaebitic = 0
    alltimesss = 0
    for i in range(times):
        data = getCharacter(wantdolpa, nowdolpa, pickupcharacter)
        alltimesss += data['times']
        if data["times"] < checkSangwi:
            gaebitic += 1
        if nowjjang['times'] > data['times']:
            nowjjang = data
        if i%10000 ==0:
            print(i)
    return {"Probability" : gaebitic/(times/100), "ProbabilityMiddle" : alltimesss/times, "best" : nowjjang['times'], "bestlist" : nowjjang['yourcharacters']}

def getFinalProbability(times, pickupCharacterName, nowdolpa, wantdolpa, yourtime):
    if yourtime == "NULL":
        yourtime = 1
    if pickupCharacterName == "NULL":
        pickupCharacterName = "픽업"
    if nowdolpa == "NULL":
        nowdolpa = 0
    if wantdolpa == "NULL":
        nowdolpa = 6
    if times == "NULL":
        times = 1000
    array = getProbability(times, pickupCharacterName, yourtime, nowdolpa, wantdolpa)
    print(f"나보다 비틱할 확률: {array['Probability']}%")
    print(f"평균 기댓값: {array['ProbabilityMiddle']}")
    print(f"최고비틱: {array['best']}")
    print(f"{array['bestlist']}")
    return array
    
#시뮬 돌릴횟수, 픽업캐이름, 현재 캐릭터 갯수(1돌이면 2), 원하는 돌파(6돌이면 6), 상위몇퍼인지 계산할거면 돌린가챠수
getFinalProbability(3000000, "치오리", 0, 5, 10)


