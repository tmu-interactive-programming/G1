"""
testing 垃圾車時間 — W07 的功能，W08 合併進小組 Bot
"""
from linebot.v3.messaging import TextMessage

NAME = "垃圾車時間"
AUTHOR = "@b101113063-hsiaoeric"
KEYWORDS = ["垃圾車", "倒垃圾"]


def handle(text, user_id):
    # text 是使用者輸入的文字；把你 W07 的程式邏輯放在這裡
    return [
        TextMessage(text="🚛 今晚 7:30 在 A 棟門口收垃圾"),
        TextMessage(text="♻️ 週二、四、六收回收"),
    ]
