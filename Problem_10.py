t = int(input())
for i in range(t):
    target, score, ball_left = map(int, input().split())
    target += 1
    ball_played = 300 - ball_left
    need = target - score
    cr = (int(score) / float(ball_played)) * 6
    rr = (int(need) / float(ball_left)) * 6
    print("%.2f %.2f" % (cr, rr))
