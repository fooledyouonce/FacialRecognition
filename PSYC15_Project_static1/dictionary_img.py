import os 

def getKey(pyimage):
    trial_dict = {'pyimage1':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage2':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage3':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage4':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage5':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage6':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\
              
              'pyimage7':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage8':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage9':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage10':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage11':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage12':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\
              
              'pyimage13':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage14':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage15':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage16':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage17':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage18':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\
              
              'pyimage19':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage20':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage21':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage22':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage23':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage24':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage25':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage26':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage27':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage28':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage29':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage30':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage31':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage32':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage33':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage34':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage35':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage36':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage37':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage38':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage39':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage40':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage41':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage42':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage43':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage44':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage45':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage46':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage47':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage48':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage49':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage50':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury'],\
              'pyimage51':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage52':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage53':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage54':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted'],\

              'pyimage55':['afraid','scared','fear','frightened','nervous','terrified','terror','alarm','dread','fright','fearful','alarmed'],\
              'pyimage56':['angry','anger','mad','frustrated','upset','rage','enraged','furious','hate','hatred','fury','frustration','irritated','irritation','seething','infuriated','livid','pissed','pissed off'],\
              'pyimage57':['disgust','disgusted','repulsed','horror','sickened','revulsion','detest','nausea','distaste','grossed out','contempt'],\
              'pyimage58':['happy','glad','joyful','joy','content','satisfied','cheer','cheerful','smile','smiling','merry','elated','delighted','amused','enjoy','enjoyment','enjoyed','jublient'],\
              'pyimage59':['sad','unhappy','depressed','down','gloomy','miserable','anguish','sorrowful','regret','desolate','inconsolable','sorrow','sadness','defeated','upset','grief','grieving','distraught','devastated','disheartened','heartbroken','downcast','despair'],\
              'pyimage60':['surprise','surprised','shock','shocked','amazed','astonished','astound','stunned','startled','speechless','unbelievable','disbelief','realization','realize','dumbfounded','flabbergasted']}

    values = trial_dict[pyimage]
    return values
       
if __name__ == "__main__":
    dictionary_img()
              
