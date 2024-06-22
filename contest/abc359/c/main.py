def main():
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    fee = 0

    #タイルの左側に合わせる
    if (sx + sy) % 2 == 1:
        sx -= 1
    if (tx + ty) % 2 == 1:
        tx -= 1

    tx -= sx
    ty -= sy
    
    tx = abs(tx)
    ty = abs(ty)

    #縦の移動回数よりも横の移動回数が多い場合のみたす
    print(ty + max(0, tx - ty) // 2)


main()