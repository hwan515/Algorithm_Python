def solution(video_len, pos, op_start, op_end, commands):
    # 동영상 길이, 재생위치, 오프닝 시작 시간, 오프닝 엔딩 시간, 사용자 입력
    def to_second(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s
    
    video_len = to_second(video_len)
    pos = to_second(pos)
    op_start = to_second(op_start)
    op_end = to_second(op_end)
    
    for command in commands:
        # 오프닝 스킵(끝나는 위치로)
        if op_start <= pos <= op_end:
            pos = op_end
        if command == "prev":
            pos -= 10
            # 10초 미만이면 처음 위치로 이동
            if pos < 10:
                pos = 0
        elif command == "next":
            pos += 10
            # 남은 시간이 10초 미만일때 마지막 위치
            if video_len - pos < 10:
                pos = video_len
    # 오프닝 스킵(끝나는 위치로)
    if op_start <= pos <= op_end:
        pos = op_end
        
    mm = str(pos // 60).zfill(2)
    ss = str(pos % 60).zfill(2)
    return f'{mm}:{ss}'