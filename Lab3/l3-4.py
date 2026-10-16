def most_balls(football, basketball, volleyball):
    if football >= basketball and football >= volleyball:
        return "Football"
    elif basketball >= football and basketball >= volleyball:
        return "Basketball"
    else:
        return "Volleyball"

print("=== โปรแกรมเปรียบเทียบจำนวนลูกบอล ===")
fb_count = int(input("กรุณากรอกจำนวนลูก Football: "))
bb_count = int(input("กรุณากรอกจำนวนลูก Basketball: "))
vb_count = int(input("กรุณากรอกจำนวนลูก Volleyball: "))

most_popular = most_balls(fb_count, bb_count, vb_count)

print(f"กีฬาที่มีจำนวนลูกมากที่สุดคือ: {most_popular}")