from turtledemo.forest import doit1

from flask import Flask, render_template, request, redirect
import os, datetime, random
# from flask_sslify import SSLify

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='')
# sslify = SSLify(app)

# If you have SSL
"""
@app.before_request
def force_https():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)
"""


@app.route('/')
def hello_world():  # put application's code here
    if os.path.exists("days.wte") and os.path.isfile("days.wte"):
        with open("days.wte", 'r+', encoding='utf-8') as f:
            liveddates = f.readlines()
        td = str(datetime.date.today())
        if td in liveddates:
            pass
        else:
            s = datetime.date.today() - datetime.timedelta(datetime.date.weekday(datetime.date.today()))
            for i in [0, 1, 2, 3, 4, 5, 6]:
                with open("days.wte", 'a+', encoding='utf-8') as f2:
                    f2.write(str(s + datetime.timedelta(days=i)))
            with open("menu.lst", "w+", encoding="utf-8") as f:
                menu = []
                meat = ['照烧鸡排', '照烧猪颈肉', '白灼虾', '红烧肉/排骨', '手撕鸡', '煎三文鱼', '炸鸡块', '炸鳕鱼块', '滑蛋牛肉', '清蒸鲈鱼', '蘑菇炖鸡', '滑蛋虾仁', '烤羊排', '洋葱炒猪肝', '蟹柳虾仁炒蛋', '咖喱鸡', '青椒炒肉丝', '夫妻肺片']
                vegt = ['生菜', '菠菜', '西兰花', '娃娃菜', '荷兰豆', '秋葵', '丝瓜炒蛋', '番茄炒蛋', '香菇炒青菜', '炒木耳菜', '竹笋香菇面筋', '黄瓜木耳炒蛋', '韭黄炒蛋', '肉末茄子', '青椒炒蛋', '芦笋炒蛋', '炒空心菜', '芹菜鸡蛋干', '拍黄瓜']
                soup = ['丝瓜蛋汤', '番茄蛋汤', '紫菜蛋汤', '娃娃菜一锅炖', '蒸蛋', '牛肉豆腐锅', '竹荪鸡汤', '萝卜香菇排骨汤', '玉米山药排骨汤', '皮蛋豆腐', '素鸡', '腐皮卷', '卤鹌鹑蛋', '土豆泥色拉', '/', '/', '/', '/', '/', '/', '/']
                rice = ['鲜虾鸡蛋面', '红烧鸡腿面', '番茄鸡蛋面', '猪排饭', '亲子饭', '蛋包饭', '菜饭', '三文鱼意面', '鸡胸肉意面', '小馄饨', '饺子', '生菜牛肉拌饭', '三文鱼菌菇饭', '烤肠芦笋意面', '牛排意面', '塔塔配烤肠', '虾仁鸡肉碗']
                metu = ['照烧鸡排饭-食其家', '汉堡王套餐', '麦当劳套餐', '振鼎鸡拌面套餐', '小杨生煎套餐', '寿司-酯士道/雪盈', '猪排饭-花火', '叉烧饭套餐-富荣祥', '拌将麻辣烫', '大米先生套餐']
                random.shuffle(meat)
                random.shuffle(vegt)
                random.shuffle(soup)
                random.shuffle(rice)
                random.shuffle(metu)
                for i in range(7):
                    if random.randint(0, 1) == 0:
                        d = [meat[i], vegt[i], soup[i], meat[-i], vegt[-i], metu[i]]
                        menu.append(d)
                    else:
                        d = [rice[i], '/', '/', meat[-i], vegt[-i], metu[i]]
                        menu.append(d)
                f.writelines(str(menu))
    else:
        s = datetime.date.today() - datetime.timedelta(datetime.date.weekday(datetime.date.today()))
        for i in [0, 1, 2, 3, 4, 5, 6]:
            with open("days.wte", 'a+', encoding='utf-8') as f2:
                f2.write(str(s + datetime.timedelta(days=i)))
        with open("menu.lst", "w+", encoding="utf-8") as f:
            menu = []
            meat = ['照烧鸡排', '照烧猪颈肉', '白灼虾', '红烧肉/排骨', '手撕鸡', '煎三文鱼', '炸鸡块', '炸鳕鱼块',
                    '滑蛋牛肉', '清蒸鲈鱼', '蘑菇炖鸡', '滑蛋虾仁', '烤羊排', '洋葱炒猪肝', '蟹柳虾仁炒蛋', '咖喱鸡',
                    '青椒炒肉丝', '夫妻肺片']
            vegt = ['生菜', '菠菜', '西兰花', '娃娃菜', '荷兰豆', '秋葵', '丝瓜炒蛋', '番茄炒蛋', '香菇炒青菜',
                    '炒木耳菜', '竹笋香菇面筋', '黄瓜木耳炒蛋', '韭黄炒蛋', '肉末茄子', '青椒炒蛋', '芦笋炒蛋',
                    '炒空心菜', '芹菜鸡蛋干', '拍黄瓜']
            soup = ['丝瓜蛋汤', '番茄蛋汤', '紫菜蛋汤', '娃娃菜一锅炖', '蒸蛋', '牛肉豆腐锅', '竹荪鸡汤',
                    '萝卜香菇排骨汤', '玉米山药排骨汤', '皮蛋豆腐', '素鸡', '腐皮卷', '卤鹌鹑蛋', '土豆泥色拉', '/',
                    '/', '/', '/', '/', '/', '/']
            rice = ['鲜虾鸡蛋面', '红烧鸡腿面', '番茄鸡蛋面', '猪排饭', '亲子饭', '蛋包饭', '菜饭', '三文鱼意面',
                    '鸡胸肉意面', '小馄饨', '饺子', '生菜牛肉拌饭', '三文鱼菌菇饭', '烤肠芦笋意面', '牛排意面',
                    '塔塔配烤肠', '虾仁鸡肉碗']
            metu = ['照烧鸡排饭-食其家', '汉堡王套餐', '麦当劳套餐', '振鼎鸡拌面套餐', '小杨生煎套餐',
                    '寿司-酯士道/雪盈', '猪排饭-花火', '叉烧饭套餐-富荣祥', '拌将麻辣烫', '大米先生套餐']
            random.shuffle(meat)
            random.shuffle(vegt)
            random.shuffle(soup)
            random.shuffle(rice)
            random.shuffle(metu)
            for i in range(7):
                if random.randint(0, 1) == 0:
                    d = [meat[i], vegt[i], soup[i], meat[-i], vegt[-i], metu[i]]
                    menu.append(d)
                else:
                    d = [rice[i], '/', '/', meat[-i], vegt[-i], metu[i]]
                    menu.append(d)
            f.writelines(str(menu))

    return render_template("ui.html")

@app.route('/daily')
def daily():
    with open("menu.lst", 'r+', encoding='utf-8') as f:
        menu = eval(f.read())
    tb = """<table border="1">
  <tr>
    <td>日期</td>
    <td>荤菜</td>
    <td>素菜</td>
    <td>汤/凉菜</td>
    <td>备选荤</td>
    <td>备选素</td>
    <td>外卖</td>
  </tr>
    """
    for i in range(7):
        tb += """  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
        """.format(menu[i][0], menu[i][1], menu[i][2], menu[i][3], menu[i][4], menu[i][5], menu[i][6])
        tb += "</table>"
    return render_template("show.html", food_lst=tb)

@app.route('/weekly')
def weekly():
    tb = """<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>
    """
    tb = "???"
    return render_template("show.html", food_lst=tb)


if __name__ == '__main__':
    app.run()
