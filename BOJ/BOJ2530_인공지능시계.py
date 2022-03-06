def time_to_seconds(hour, minute, seconds):
    return hour*3600 + minute*60 + seconds


def seconds_to_time(seconds):
    r, s = divmod(seconds, 60)
    h, m = divmod(r, 60)
    if h >= 24:
        _, h = divmod(h, 24)
    return '%d %d %d' % (h, m, s)


h, m, s = map(int, input().split())
# _, duration = divmod(int(input()), 24*3600)  # 어차피 24시간이 지나면 그 시간이므로
duration = int(input())
start = time_to_seconds(h, m, s)
end = seconds_to_time(start + duration)
print(end)
