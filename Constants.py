
# Constants for Music Generation
notes = ['c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5', 'd5', 'e5', 'f5', 'g5', 'a5', 'b5']  # C大调音符
advancedNotes=notes+['c6', 'd6', 'e6', 'f6', 'g6', 'a6', 'b6','c7', 'd7', 'e7', 'f7', 'g7', 'a7', 'b7']
notesForBass= ['c1','d1', 'e1', 'f1', 'g1', 'a1', 'b1','c2','d2', 'e2', 'f2', 'g2', 'a2', 'b2', 'c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3']+notes  # 低音阶音符
advancedNotes+=notesForBass
melodyLength = 16  # 旋律长度（音符数量）
totalDuration = 16  # 总持续时间
FPS=44100
BPM=120

# 定义节奏型
rhythms = [
    (4,),       # 四分音符
    (8, 16, 16),  # 前八后十六（一个八分音符 + 两个十六分音符）
    (8, 8),     # 二八（两个八分音符）
    (16, 16, 16, 16), # 四个十六分音符
    (4,8,4)#附点
] 