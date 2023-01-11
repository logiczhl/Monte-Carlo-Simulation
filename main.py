import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from tqdm import trange
from matplotlib import rcParams

# Set Font
config = {
    "font.family": 'Times New Roman',
    "mathtext.fontset": 'stix',
    'axes.unicode_minus': False
}
rcParams.update(config)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# data processing
def data_processing(file_path):
    df = pd.read_csv(file_path, encoding='gbk')
    print(df.columns)
    city_list = df[' City ']
    production_list = df['Average daily medical waste production in 2019 (tonnes/day) ']
    disposal_list = df['Total (emergency+centralized) medical waste disposal capacity (tonnes/day) ']
    disposal_list = np.array(disposal_list)
    city_list = np.array(city_list)
    production_list = np.array(production_list)
    return city_list, production_list, disposal_list


def random_list(n, production, disposal, loc, scale):
    pert_num1 = np.random.normal(loc=loc, scale=scale, size=n)
    load_ratio = production * (1.0 + pert_num1 / 100.0) / disposal
    ans = load_ratio
    ans.sort()
    ans = np.array(ans)
    ans_2f = np.round(ans, 1)
    ans_2f_unique = np.unique(ans_2f)
    ans_2f_on = pd.Series(ans_2f)
    ans_2f_on = ans_2f_on.value_counts()
    ans_2f_on.sort_index(inplace=True)
    a = ans_2f_on.index
    a = np.array(a)
    b = ans_2f_on
    b = np.array(b)
    y_num = b
    y_num_gailv = y_num / n
    return ans_2f_unique, y_num, y_num_gailv, ans_2f


def Monte_draw(n, production, disposal, city, letter):
    loc1 = 1442
    loc2 = 700
    loc3 = 325.9
    loc4 = 197.7
    scale = 96.3
    ans_2f_unique1, y_num1, y_num_gailv1, ans_2f1 = random_list(n, production, disposal, loc=loc1, scale=scale)
    ans_2f_unique2, y_num2, y_num_gailv2, ans_2f2 = random_list(n, production, disposal, loc=loc2, scale=scale)
    ans_2f_unique3, y_num3, y_num_gailv3, ans_2f3 = random_list(n, production, disposal, loc=loc3, scale=scale)
    ans_2f_unique4, y_num4, y_num_gailv4, ans_2f4 = random_list(n, production, disposal, loc=loc4, scale=scale)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    max_num = find_max(y_num1, y_num2, y_num3, y_num4)
    lin1 = ax.plot(ans_2f_unique1, y_num_gailv1 * 100, color=(189 / 255, 215 / 255, 238 / 255))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f%%'))
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.xlabel('Load rate', weight='bold')
    plt.ylabel('Probability', weight='bold')
    ax1 = ax.twinx()
    ax1.plot(ans_2f_unique1, y_num1, color=(189 / 255, 215 / 255, 238 / 255))
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
    ax1.plot(ans_2f_unique2, y_num2, color=(248 / 255, 203 / 255, 173 / 255))
    ax1.plot(ans_2f_unique3, y_num3, color=(151 / 255, 200 / 255, 141 / 255))
    ax1.plot(ans_2f_unique4, y_num4, color=(255 / 255, 192 / 255, 0 / 255))
    plt.ylabel('Frequency (times)', weight='bold')
    plt.title('({}) {}'.format(letter, city), fontsize=15, weight='bold')
    plt.savefig('./pic/{0}.jpg'.format(city), dpi=300, bbox_inches='tight', pad_inches=0.0)


def col_ration():
    n = 50000
    loc1 = 1442
    loc2 = 700
    loc3 = 325.9
    loc4 = 197.7
    scale = 96.3
    file_path = 'data.csv'
    city_list, production_list, disposal_list = data_processing(file_path)
    gailv1 = list()
    gailv2 = list()
    gailv3 = list()
    gailv4 = list()
    gailv5 = list()
    gailv6 = list()
    gailv7 = list()
    gailv8 = list()
    gailv9 = list()
    gailv10 = list()
    gailv11 = list()
    gailv12 = list()
    gailv13 = list()
    gailv14 = list()
    gailv15 = list()
    gailv16 = list()
    for i in trange(len(city_list)):
        ans_2f_unique1, y_num1, y_num_gailv1, ans_2f1 = random_list(n, production_list[i], disposal_list[i], loc=loc1,
                                                                    scale=scale)
        gailv1.append(col_gailv(ans_2f1, 50))
        gailv2.append(col_gailv(ans_2f1, 75))
        gailv3.append(col_gailv(ans_2f1, 100))
        gailv4.append(col_gailv(ans_2f1, 150))
        ans_2f_unique2, y_num2, y_num_gailv2, ans_2f2 = random_list(n, production_list[i], disposal_list[i], loc=loc2,
                                                                    scale=scale)
        gailv5.append(col_gailv(ans_2f2, 50))
        gailv6.append(col_gailv(ans_2f2, 75))
        gailv7.append(col_gailv(ans_2f2, 100))
        gailv8.append(col_gailv(ans_2f2, 150))
        ans_2f_unique3, y_num3, y_num_gailv3, ans_2f3 = random_list(n, production_list[i], disposal_list[i], loc=loc3,
                                                                    scale=scale)
        gailv9.append(col_gailv(ans_2f3, 50))
        gailv10.append(col_gailv(ans_2f3, 75))
        gailv11.append(col_gailv(ans_2f3, 100))
        gailv12.append(col_gailv(ans_2f3, 150))
        ans_2f_unique4, y_num4, y_num_gailv4, ans_2f4 = random_list(n, production_list[i], disposal_list[i], loc=loc4,
                                                                    scale=scale)
        gailv13.append(col_gailv(ans_2f4, 50))
        gailv14.append(col_gailv(ans_2f4, 75))
        gailv15.append(col_gailv(ans_2f4, 100))
        gailv16.append(col_gailv(ans_2f4, 150))
    data = {
        'city': city_list,
        '1': gailv1,
        '2': gailv2,
        '3': gailv3,
        '4': gailv4,
        '5': gailv5,
        '6': gailv6,
        '7': gailv7,
        '8': gailv8,
        '9': gailv9,
        '10': gailv10,
        '11': gailv11,
        '12': gailv12,
        '13': gailv13,
        '14': gailv14,
        '15': gailv15,
        '16': gailv16,
    }
    data1 = pd.DataFrame(data)
    data1.to_csv('new_result.csv')


def col_gailv(gailv_list, gailv):
    ans = 0
    for i in range(len(gailv_list)):
        if gailv_list[i] >= gailv:
            ans += 1
    return ans / len(gailv_list)


def all_city_pic(n):
    file_path = 'data.csv'
    city_list, production_list, disposal_list = data_processing(file_path)
    le = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    count = 0
    for i in trange(len(city_list)):
        count += 1
        letter = le[int(i / 26)] + le[i % 26]
        Monte_draw(n, production_list[i], disposal_list[i], city_list[i], letter)


def find_max(y_num1, y_num2, y_num3, y_num4):
    y1 = max(y_num1)
    y2 = max(y_num2)
    y3 = max(y_num3)
    y4 = max(y_num4)
    ans = max(y1, y2, y3, y4)
    return ans


if __name__ == '__main__':
    col_ration()
    all_city_pic(50000)
