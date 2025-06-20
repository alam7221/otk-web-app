import streamlit as st
from scipy.stats import hypergeom

FIXED_DRAW_COUNT = 5

astaroth_probs = {
    10: 50.00,
    11: 45.45,
    12: 41.66,
    13: 38.46,
    14: 35.71,
    15: 33.33,
    16: 31.25,
    17: 29.41,
}

def calc_quon_prob(deck_size, quon_count):
    rv = hypergeom(deck_size, quon_count, FIXED_DRAW_COUNT)
    prob = 1 - rv.pmf(0)
    return prob * 100

st.title("Shadowverse: Worlds Beyond")
st.title("クオンorアスタロト 確率比較")

st.markdown("10ppディメンション前にクオンかサタンどちらをプレイするか迷ったときに使ってください。")
st.markdown("2枚目のディメンション等の細かい確率は含まず、％表記も大体です。ほぼgpt製")


hand = st.number_input("現在の手札の枚数(クオンorサタンを使う直前の数値)", min_value=0, step=1)
deck = st.number_input("現在のデッキの枚数(ディメンションで戻す前の数値)", min_value=0, step=1)
quon = st.number_input("クオンの残りの枚数（ディメンションで戻した時のデッキに入っている枚数）", min_value=1, max_value=2, step=1)

if st.button("確率を計算して比較"):
    quon_deck = hand + deck - 2
    astaroth_deck = hand + 8

    if quon_deck < FIXED_DRAW_COUNT or quon_deck < quon:
        st.error("クオンのデッキ枚数が不正です。")
    elif astaroth_deck not in astaroth_probs:
        st.error("手札の枚数が不正です。")
    else:
        quon_prob = calc_quon_prob(quon_deck, quon)
        astaroth_prob = astaroth_probs[astaroth_deck]

        st.markdown(f"### 結果")
        st.write(f"通常デッキ枚数: {quon_deck} 枚")
        st.write(f"アポカリプスデッキ枚数: {astaroth_deck} 枚")
        st.write(f"クオンを引く確率: {quon_prob:.2f}%")
        st.write(f"アスタロトを引く確率: {astaroth_prob:.2f}%")

        if abs(quon_prob - astaroth_prob) < 0.01:
            st.success("両者の引く確率は同じです。")
        elif quon_prob > astaroth_prob:
            st.success("クオンの方が引く確率が高いです。")
        else:
            st.success("アスタロトの方が引く確率が高いです。")
