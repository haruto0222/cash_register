#釣り銭計算プログラム
#　Written by Ida Haruto

from prettytable import PrettyTable
money = [10000,5000,2000,1000,500,100,50,10,5,1]
kazu = [0,10,10,10,20,20,20,20,20,20]

while True:
    oturi_min_maisuu = []
    shiharai = []
    goukei = 0
    while True:
        try:
            kingaku=int(input("商品の合計金額を入力してください。>>"))
            if kingaku>0:
                break
            else:
                print("入力された金額に不備があります。もう一度入力してください。")
        except:
            print("入力された金額に不備があります。もう一度入力してください。")

    #金額の入力
    while True:
        print("支払金額を入力してください")
        for n in money:
            while True:
                try:
                    maisuu=int(input(str(n)+("円札"if n>=1000 else "円硬貨")+"の枚数入力＞＞"))
                    if maisuu >= 0:
                        shiharai.append(maisuu)
                        break
                    else:
                        print("入力された金額に不備があります。もう一度入力してください。")
                except:
                    print("入力された金額に不備があります。もう一度入力してください。")

        for s,t in zip(money,shiharai):
            goukei +=s*t
        oturi=goukei-kingaku
        if oturi<0:
            print("支払金額が",abs(oturi),"円","不足しています。")
            print("もう一度入力してください")
        else:
            break

    #支払い
    kazu=[x+y for(x,y) in zip(kazu,shiharai)]

    #最小枚数の計算
    for k,v in zip(money,kazu):
        if k<=oturi:
            need=oturi//k
            comp=v-need
            if comp>=0:
                oturi_min_maisuu.append(need)
                oturi=oturi-(k*need)
            else:
                oturi_min_maisuu.append(v)
                oturi=oturi-(k*v)
        else:
            oturi_min_maisuu.append(0)
    if oturi>0:
        print("レジ内のお金が不足しておりお釣りを出すことができません")
        print("レジのお金を追加してください")
    else:
        kazu=[x-y for (x,y) in zip(kazu,oturi_min_maisuu)]

        #お釣りの表示
        print("払戻金額")
        pt_oturi=PrettyTable()
        pt_oturi.field_names=money
        pt_oturi.add_row(oturi_min_maisuu)
        print(pt_oturi)


        #レジ内のお金の表示
        print("レジ残高")
        pt_kazu=PrettyTable()
        pt_kazu.field_names=money
        pt_kazu.add_row(kazu)
        print(pt_kazu)

