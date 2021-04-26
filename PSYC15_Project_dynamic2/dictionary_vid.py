import os

def getKey(video):
    trial_dict = {'vid111.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
                  'vid112.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
                  'vid113.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
                  'vid114.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
                  'vid115.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
                  'vid116.mp4':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\

                  'vid117.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
                  'vid118.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
                  'vid119.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
                  'vid120.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
                  'vid121.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
                  'vid122.mp4':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\

                  'vid123.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\
                  'vid124.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\
                  'vid125.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\
                  'vid126.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\
                  'vid127.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\
                  'vid128.mp4':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful'],\

                  'vid129.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\
                  'vid130.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\
                  'vid131.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\
                  'vid132.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\
                  'vid133.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\
                  'vid134.mp4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoyed','enjoyment','enjoy','jublient'],\

                  'vid135.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\
                  'vid136.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\
                  'vid137.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\
                  'vid138.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\
                  'vid139.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\
                  'vid140.mp4':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sadness','defeated','upset','grief','grieving','distraught','sorrow','devastated','disheartened','heartbroken','downcast','despair'],\

                  'vid141.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted'],\
                  'vid142.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted'],\
                  'vid143.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted'],\
                  'vid144.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted'],\
                  'vid145.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted'],\
                  'vid146.mp4':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','dumbfounded','realize','flabbergasted']}

    values = trial_dict[video]
    return values

if __name__ == "__main__":
    dictionary_vid()
